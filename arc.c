// arc.c
#include "stdlib.h"
#include "math.h"
#define TRUE 1
#define FALSE 0

int performSimulations(int numSim, int maxAttempts, int minRollRel, int minRollArc) {
    int i;
    int numAttempts = 0;
    int numRolls = 0;
    int roll;
    for (i = 0; i < numSim; i++) {
        int religionPassed = FALSE;
        numAttempts = 0;
        while (numAttempts < maxAttempts && !religionPassed ) {
            numRolls++;
            roll = (rand() % 20) + 1;
            if (roll >= minRollRel || religionPassed) { //move on if we pass the religion check or have previously passed the religion check
                roll = (rand() % 20) + 1;
                if (roll >= minRollArc) {
                    break;
                }
            } 
            if (!religionPassed){
                numAttempts++;
            }
        }
    }
    return numRolls;
}

int calculateCost(int costInit, int costFail, int numSim, int maxAttempts, int minRollRel, int minRollArc) {
    float numRolls = performSimulations(numSim, maxAttempts, minRollRel, minRollArc);
    float avgAttempts = numRolls / numSim;
    avgAttempts = ceil(avgAttempts) - 1;
    return costInit + (avgAttempts * costFail);
}

