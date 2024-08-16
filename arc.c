// arc.c
#include "stdlib.h"
#define TRUE 1
#define FALSE 0

int performSimulations(int numSim, int maxAttempts, int minRollRel, int minRollArc) {
    int i;
    int numAttempts = 0;
    int numRolls = 0;
    int roll;
    for (i = 0; i < numSim; i++) {
        int religionPassed = FALSE;
        int arcanePassed = FALSE;
        numAttempts = 0;
        while (numAttempts < maxAttempts && (!religionPassed || !arcanePassed)) {
            numRolls++;
            roll = (rand() % 20) + 1;
            if (roll >= minRollRel || religionPassed) {
                roll = (rand() % 20) + 1;
                if (roll >= minRollArc) {
                    break;
                }
            } 
            if (!(religionPassed && arcanePassed)){
                numAttempts++;
            }
        }
    }
    return numRolls;
}

int calcAvgAttempts(int numRolls, int numSim) {
    return numRolls / numSim;
}


int calculateCost(int avgAttempts, int costInit, int costFail) {
    return costInit + ((avgAttempts -1) * costFail);
}


int callFromPython(int costInit, int costFail, int numSim, int maxAttempts, int minRollRel, int minRollArc) {
    int numRolls = performSimulations(numSim, maxAttempts, minRollRel, minRollArc);
    int avgAttempts = calcAvgAttempts(numRolls, numSim);
    return calculateCost(avgAttempts, costInit, costFail);
}

