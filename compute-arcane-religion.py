# mcgee's method
from ctypes import cdll
import csv
from spell_listing import SpellListing
from player_stats import PlayerStats
from player_level_cost import PlayerLevelCost


def gatherInputs():
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
    cost_initial, cost_failure, min_roll, simulations, attempts = gatherInputs()
    total_cost = lib.callFromPython(int(cost_initial), int(cost_failure), int(simulations), int(attempts), int(min_roll))
    print(f"Total cost: {total_cost}")

def load_spell_table(spell_table: str):
    spell_list = []
    with open(spell_table, mode='r') as file:
        csv_reader = csv.DictReader(file, fieldnames=['level','gp-init','gp-setback','time-init','time-setback','religion','arcana'])
        for row in csv_reader:
            listing = SpellListing(int(row['level']), int(row['gp-init']), int(row['gp-setback']), int(row['time-init']), int(row['time-setback']), int(row['religion']), int(row['arcana']))
            spell_list.append(listing)
    return spell_list

def load_player_stats(player_stats: str):
    player_list = []
    with open(player_stats, mode='r') as file:
        csv_reader = csv.DictReader(file, fieldnames=['name','level','religion','arcana'])
        for row in csv_reader:
            player = PlayerStats(row['name'], int(row['level']), int(row['religion']), int(row['arcana']))
            player_list.append(player)
    return player_list

def produce_csv(output_file: str, plc_list: list):
    pass

def main():
    # load spell table

    # load player stats

    # for each player, calculate the cost of each spell
        # calculate cost in gold
        # calculate cost in time
        # add PLCs to lists
    
    # output the list of PLCs to csv file



    pass

if __name__ == "__main__":
    main()