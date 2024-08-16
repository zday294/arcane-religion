# mcgee's method
import csv
import yaml
from ctypes import cdll
from spell_listing import SpellListing
from player_stats import PlayerStats
from player_level_cost import PlayerLevelCost



def gather_inputs():
    cost_initial = input("Cost of intial attempt: ")
    cost_failure = input("Cost of failure: ")
    min_religion_roll = ""
    between_1_20 = False
    while not between_1_20:
        min_religion_roll = int(input("Minimum Religion roll (1-20): "))
        if min_religion_roll >= 1 and min_religion_roll <= 20:
            between_1_20 = True
        else:
            print("Please enter a number between 1 and 20")

    min_arcana_roll = ""
    between_1_20 = False
    while not between_1_20:
        min_arcana_roll = int(input("Minimum Arcana roll (1-20): "))
        if min_arcana_roll >= 1 and min_arcana_roll <= 20:
            between_1_20 = True
        else:
            print("Please enter a number between 1 and 20")
    

    simulations = input("Simulations: ") 
    attempts = input("Max attempts per simulation: ")
    return cost_initial, cost_failure, min_religion_roll, simulations, attempts

def manual_one_time():
    lib = cdll.LoadLibrary('./arclib.so')
    cost_initial, cost_failure, min_roll, simulations, attempts = gather_inputs()
    total_cost = lib.callFromPython(int(cost_initial), int(cost_failure), int(simulations), int(attempts), int(min_roll))
    print(f"Total cost: {total_cost}")

def load_spell_table(spell_table: str) -> list[SpellListing]:
    spell_list = []
    with open(spell_table, mode='r') as file:
        csv_reader = csv.DictReader(file, fieldnames=['level','gp-init','gp-setback','time-init','time-setback','religion','arcana'])
        # skip the header
        next(csv_reader)
        for row in csv_reader:
            listing = SpellListing(int(row['level']), int(row['gp-init']), int(row['gp-setback']), int(row['time-init']), int(row['time-setback']), int(row['religion']), int(row['arcana']))
            spell_list.append(listing)
    return spell_list

def load_player_stats(player_stats: str) -> list[PlayerStats]:
    player_list = []
    with open(player_stats, mode='r') as file:
        csv_reader = csv.DictReader(file, fieldnames=['name','level','religion','arcana'])
        # skip the header
        next(csv_reader)
        for row in csv_reader:
            player = PlayerStats(row['name'], int(row['level']), int(row['religion']), int(row['arcana']))
            player_list.append(player)
    return player_list

def produce_csv(output_file: str, plc_list: list):
    with open(output_file, mode='w') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Name','Level','Cantrip','Level 1','Level 2', 'Level 3', 'Level 4', 'Level 5'])
        for plc in plc_list:
            csv_writer.writerow([plc.name, plc.level, plc.costs[0], plc.costs[1], plc.costs[2], plc.costs[3], plc.costs[4], plc.costs[5]])

def load_config(config_file: str):
    with open(config_file, mode='r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config

def main():
    # load library
    lib = cdll.LoadLibrary('./arclib.so')

    # load config.yaml
    config = load_config('config.yml')

    # load spell table
    spell_list = load_spell_table(config['spell-table-file'])

    # load player stats
    player_list = load_player_stats(config['player-stats-file'])

    # for each player, calculate the cost of each spell
    plcs_gold = []
    plcs_time = []
    for player in player_list:
        #for each spell in spell_list
        plc_gold_list = []
        plc_time_list = []
        for spell in spell_list:    
            # calculate cost in gold
            gp_cost = lib.calculateCost(spell.gp_init, spell.gp_setback, config["simulations"], config["attempts"], spell.religion - player.religion, spell.arcana - player.arcana)
            # calculate cost in time
            time_cost = lib.calculateCost(spell.time_init, spell.time_setback, config["simulations"], config["attempts"], spell.religion - player.religion, spell.arcana - player.arcana)
            # add PLCs to lists
            plc_gold_list.append(gp_cost)
            plc_time_list.append(time_cost)
        # create PLCs for each player
        plcs_gold.append(PlayerLevelCost(player.name, player.level, plc_gold_list))
        plcs_time.append(PlayerLevelCost(player.name, player.level, plc_time_list))

    
    # output the list of PLCs to csv file
    produce_csv(config['output-gold-file'], plcs_gold)
    produce_csv(config['output-time-file'], plcs_time)


if __name__ == "__main__":
    main()