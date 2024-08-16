# mcgee's method
from ctypes import cdll
import csv
from spell_listing import SpellListing


def gatherInputs():
    cost_initial = input("Cost of intial attempt: ")
    cost_failure = input("Cost of failure: ")
    min_roll = ""
    between_1_20 = False
    while not between_1_20:
        min_roll = int(input("Minimum roll (1-20): "))
        if min_roll >= 1 and min_roll <= 20:
            between_1_20 = True
        else:
            print("Please enter a number between 1 and 20")

    simulations = input("Simulations: ") 
    attempts = input("Max attempts per simulation: ")
    return cost_initial, cost_failure, min_roll, simulations, attempts

def manual_one_time():
    lib = cdll.LoadLibrary('./arclib.so')
    cost_initial, cost_failure, min_roll, simulations, attempts = gatherInputs()
    total_cost = lib.callFromPython(int(cost_initial), int(cost_failure), int(simulations), int(attempts), int(min_roll))
    print(f"Total cost: {total_cost}")

def load_spell_table(spell_table: str):
    with open(spell_table, mode='r') as file:
        csv_reader = csv.DictReader(file, fieldnames=['level','gp-init','gp-setback','time-init','time-setback','religion','arcana'])
        spell_list = []
        for row in csv_reader:
            listing = SpellListing(row['level'], row['gp-init'], row['gp-setback'], row['time-init'], row['time-setback'], row['religion'], row['arcana'])
            spell_list.append(listing)

def main():
    manual_one_time()

if __name__ == "__main__":
    main()