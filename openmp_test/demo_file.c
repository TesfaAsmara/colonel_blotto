#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LIMITS 1000

int main(int argc, char *argv[]) {    
    FILE* results_file0 = fopen("output_.txt", "w");
    if (results_file0 == NULL) {
        printf("Error opening result file\n");
        return 1;
    }

    int ends;
    if (argc == 2) {
        ends = atoi(argv[1]);
    }
    else {
        ends = LIMITS;
    }

    printf("Using %d as limits\n", ends);

    for (int i = 0; i < ends; i++) {
        for (int j = i+1; j < ends; j++) {
            fprintf(results_file0, "%d_%d_%d\n", i,j,i+2*i*j);
        }
    } // end omp parallel for

    fclose(results_file0);

    return 0;
}