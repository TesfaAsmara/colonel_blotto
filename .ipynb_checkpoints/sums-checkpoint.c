#include <stdio.h>

// Define the number of trenches or categories we are distributing a total sum across
#define NUM_TRENCHES 2

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
// current_sum: Sum distributed so far (used for calculating remaining sum).
// permutation: Array of integers representing the current state of the permutation.
// pos: Current position in the permutation array to fill.
//
void sums(FILE *file, int length, int total_sum, int current_sum, int permutation[], int pos) {
    if (length == 1) {
        permutation[pos] = total_sum;
        // Print the permutation to the configurations file
        printPermutationToFile(file, permutation, NUM_TRENCHES);
    } else {
        for (int value = 0; value <= total_sum; value++) {
            permutation[pos] = value;
            sums(file, length - 1, total_sum - value, current_sum + value, permutation, pos + 1);
        }
    }
}

// The main function of the program
int main() {
    // Open the configurations file for writing
    FILE *file = fopen("configurations.txt", "w");
    // Define the length of permutations and total sum to be distributed
    int length = 2;  // Example length
    int total_sum = 100;  // Example total sum
    int permutation[length];
    
    // Generate all permutations of distributing total_sum across length categories
    sums(file, length, total_sum, 0, permutation, 0);

    // Close the configurations file
    fclose(file);
 
    return 0;
}
