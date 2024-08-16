#include "stdio.h"
#include "arc.h"

int main(int argc, char** argv){
    for (int i = 0; i < 20; i++){
        int success = (20 - i) * 5;
        printf("Cost for 1000 simulations, 10 attempts per simulation, %d%% success rate: %d\n", success, calculateCost(60, 20, 1000, 100, i + 5, i + 1));
    }
}