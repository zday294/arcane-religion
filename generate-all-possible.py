# generate-all-possible 
import math
import csv
from player_stats import PlayerStats

# variables

# intelligence - 0-5

# PB - 2-6

# PL - N, H, P, E

# R = I + (PB * PLr)
# A = I + (PB * PLa)

R = []
A = []

# for evey intelligence 
for int in range(0,6):
    # for every PB
    for pb in range(2,7):
        # for every PL
        for pl in [0, .5, 1, 2]:
            # calculate formula
            val = int + math.floor(pb * pl)
            # add formula to arrays for R and A
            R.append(val)
            A.append(val)

statsEntries = []

# for value in R
for r in R:
    # for value in A
    for a in A:
        # generate player_stats entry
        # just use 0 for level
        statsEntries.append(PlayerStats("bingus", 0, r, a))

with open("all-stats.csv", mode='w') as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['ame', 'level', 'religion', 'arcana'])
    for entry in statsEntries:
        csv_writer.writerow([entry.name, entry.level, entry.religion, entry.arcana])

print("Done!")
