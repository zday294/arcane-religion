#include "stdio.h"
#include "arc.h"


int main(int argc, char** argv){
    //print "Calculating cost for 1000 simulations, 10 attempts, 50% success rate"

    for (int i = 0; i < 20; i++){
        int success = (20 - i) * 5;
        printf("Cost for 1000 simulations, 10 attempts, %d%% success rate: %d\n", success, callFromPython(60, 20, 1000, 100, i + 1));
    }

}