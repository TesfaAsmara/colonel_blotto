#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Function: printPermutationToFile
// --------------------
// Writes a permutation of numbers (a way of distributing a total sum) to a file.
//
// file: Pointer to the file where the permutation will be written.
// permutation: Array of integers representing the permutation.
// length: Length of the permutation array.
//
void printPermutationToFile(FILE *file, int permutation[], int length) {
    for (int i = 0; i < length; i++) {
        fprintf(file, "%d", permutation[i]);
        if (i != length - 1) {
            fprintf(file, ", ");
        }
    }
    fprintf(file, "\n");
}

// Function: sums
// --------------------
// Recursively generates all permutations of distributing a total sum across a fixed number of categories
// and writes each permutation to a file.
//
// file: Pointer to the file where the permutations will be written.
// length: Remaining length of the permutation array to fill.
// total_sum: Remaining sum to be distributed across the remaining length.
// permutation: Array of integers representing the current state of the permutation.
// pos: Current position in the permutation array to fill.
//
void sums(FILE *file, int length, int total_sum, int permutation[], int pos) {
    if (length == 1) {
        permutation[pos] = total_sum;
        // Print the permutation to the configurations file
        printPermutationToFile(file, permutation, pos + 1);
    } else {
        for (int value = 0; value <= total_sum; value++) {
            permutation[pos] = value;
            sums(file, length - 1, total_sum - value, permutation, pos + 1);
        }
    }
}


int main(int argc, char *argv[]) {
    int numCastles = 0;
    int numTroops = 0;
    int opt;
    char filename[100];

    // Parse command-line arguments for numCastles and numTroops
    while ((opt = getopt(argc, argv, "c:t:")) != -1) {
        switch (opt) {
            case 'c':
                numCastles = atoi(optarg);
                break;
            case 't':
                numTroops = atoi(optarg);
                break;
            default:
                fprintf(stderr, "Usage: %s -c numCastles -t numTroops\n", argv[0]);
                exit(EXIT_FAILURE);
        }
    }

    if (numCastles <= 0 || numTroops <= 0) {
        fprintf(stderr, "Invalid numCastles or numTroops values.\n");
        exit(EXIT_FAILURE);
    }

    // Allocate memory for the permutation array
    int* permutation = (int*)malloc(sizeof(int) * numCastles);
    if (!permutation) {
        fprintf(stderr, "Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }

    // Create filename for the configurations file
    sprintf(filename, "configurations/C%02d_T%03d.txt", numCastles, numTroops);
    
    // Open the configurations file for writing
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        fprintf(stderr, "Unable to open file: %s\n", filename);
        exit(EXIT_FAILURE);
    }
    
    // Generate all permutations of distributing numTroops across numCastles categories
    sums(file, numCastles, numTroops, permutation, 0);

    // Close the configurations file and free the allocated memory
    fclose(file);
    free(permutation);
 
    return 0;
}
