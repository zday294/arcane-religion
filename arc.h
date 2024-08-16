#ifndef ARC_H
#define ARC_H

int performSimulations(int numSim, int maxAttempts, int minRoll);

int calcAvgAttempts(int numRolls, int numSim);

int calculateCost(int avgAttempts, int costInit, int costFail);

int callFromPython(int costInit, int costFail, int numSim, int maxAttempts, int minRoll);

#endif