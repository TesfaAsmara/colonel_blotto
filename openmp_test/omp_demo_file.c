#include <stdio.h>
#include <string.h>
#include <omp.h>

#define LIMITS 1000

int main(int argc, char *argv[]) { 
    int ends;
    if (argc == 2) {
        ends = atoi(argv[1]);
    }
    else {
        ends = LIMITS;
    }
    printf("Using %d as limits\n", ends);
   
    FILE* results_file0 = fopen("output_omp_t0.txt", "w");
    if (results_file0 == NULL) {
        printf("Error opening result file\n");
        return 1;
    }

    FILE* results_file1 = fopen("output_omp_t1.txt", "w");
    if (results_file1 == NULL) {
        printf("Error opening result file\n");
        return 1;
    }

    FILE* results_file2 = fopen("output_omp_t2.txt", "w");
    if (results_file2 == NULL) {
        printf("Error opening result file\n");
        return 1;
    }

    FILE* results_file3 = fopen("output_omp_t3.txt", "w");
    if (results_file3 == NULL) {
        printf("Error opening result file\n");
        return 1;
    }

    #pragma omp parallel for schedule(static, 512)
    for (int i = 0; i < ends; i++) {
        if (i==0) printf("Num threads: %d \n", omp_get_num_threads());
        for (int j = i+1; j < ends; j++) {
            if (omp_get_thread_num()==0) {
                fprintf(results_file0, "%d_%d_%d\n", i,j,i+2*i*j);
            }
            else if (omp_get_thread_num()==1) {
                fprintf(results_file1, "%d_%d_%d\n", i,j,i+2*i*j); 
            }
            else if (omp_get_thread_num()==2) {
                fprintf(results_file2, "%d_%d_%d\n", i,j,i+2*i*j); 
            }
            else if (omp_get_thread_num()==3) {
                fprintf(results_file3, "%d_%d_%d\n", i,j, i+2*i*j); 
            }
        }
    }  // end omp parallel for


    fclose(results_file0);
    fclose(results_file1);
    fclose(results_file2);
    fclose(results_file3);

    return 0;
}