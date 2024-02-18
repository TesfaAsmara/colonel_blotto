#include <stdio.h>
#include <omp.h>

// #define LIMIT 100000

int main(int argc, char *argv[]) {
    // int result[1000][1000];
    
    #pragma omp parallel for 
    for (int i = 0; i < 32; i++) {
        printf("%d\n", omp_get_thread_num());
    }

    return 0;
}


// #include <stdio.h>
// #include <omp.h>

// int main(int argc, char *argv[]) {
//     FILE *output_file = fopen("output.txt", "w");
//     if (output_file == NULL) {
//         perror("Error opening file");
//         return 1;
//     }

//     for (int i = 0; i < 10000; i++) {
//         #pragma omp parallel for 
//         for (int j = i + 1; j < 100000; j++) {
//             // fprintf(output_file, "%d, %d, \n", i, j);
//             int k = i+j;
//             printf("%d\n", k);
//         }
//     }

//     fclose(output_file);
//     return 0;
// }



// gcc -o test omp_test.c && gcc -fopenmp -o omp_test omp_test.c               
// time ./test > tmp.txt && time ./omp_test > tmp.txt
