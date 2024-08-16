#ifndef ARC_H
#define ARC_H

int performSimulations(int numSim, int maxAttempts, int minRoll);

int calculateCost(int costInit, int costFail, int numSim, int maxAttempts, int minRollRel, int minRollArc);

#endif