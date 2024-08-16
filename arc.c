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
    int numRolls = performSimulations(numSim, maxAttempts, minRollRel, minRollArc);
    int avgAttempts = numRolls / numSim;
    // if (numRolls % numSim > 0){
    //     avgAttempts++;
    // }
    return costInit + (avgAttempts * costFail);
}

