#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <omp.h>
#define MAX_FILENAME_LENGTH 100

// Function: game
// --------------------
// Determines the result of a game between two players based on their strategies.
//
// player1: Array representing the strategy of player1.
// player2: Array representing the strategy of player2.
// numCastles: Number of castles in the game.
//
// returns: 1 if player1 wins, -1 if player2 wins, 0 if it's a draw.
//
int game(int* player1, int* player2, int numCastles) {
    int p1_score = 0, p2_score = 0, n = 0;
    int p1_wbt = 0, p2_wbt = 0;

    // Loop through each castle and calculate scores based on the strategies
    while (p1_wbt < 3 && p2_wbt < 3 && n < numCastles) {
        if (player1[n] > player2[n]) {
            p1_score += n + 2;
            p1_wbt++;
            p2_wbt = 0;
        } else if (player1[n] < player2[n]) {
            p2_score += n + 2;
            p2_wbt++;
            p1_wbt = 0;
        } else {
            p1_wbt = 0;
            p2_wbt = 0;
        }
        n++;
    }

    // Handle scenarios where one player has won 3 consecutive castles
    while (p1_wbt == 3 && n < numCastles) {
        p1_score += n + 2;
        n++;
    }
    while (p2_wbt == 3 && n < numCastles) {
        p2_score += n + 2;
        n++;
    }

    // Determine the winner based on the scores
    if (p1_score > p2_score) return 1;
    if (p1_score < p2_score) return -1;
    return 0;
}

// Function: play_game
// --------------------
// Plays a game between two players and writes the result to a file.
//
// i: Index of player1's strategy.
// j: Index of player2's strategy.
// player1: Array representing the strategy of player1.
// player2: Array representing the strategy of player2.
// numCastles: Number of castles in the game.
// numTroops: Number of troops in the game.
//
void play_game(int i, int j, int* player1, int* player2, int numCastles, int numTroops) {
    int result = game(player1, player2, numCastles);
    char filename[MAX_FILENAME_LENGTH];

    // Create filename for the result file
    sprintf(filename, "/home/jovyan/data3/results/C%02d_T%03d/%d_%d_%d.txt", numCastles, numTroops, i, j, result);
    FILE* file = fopen(filename, "w");
    if (file != NULL) {
        fclose(file);
    } else {
        printf("Unable to open file: %s\n", filename);
    }
}

// function to write the results matrix to a file
void writeResultsToFile(int** results, int count, int numCastles, int numTroops) {
    char results_filename[100];
    sprintf(results_filename, "/home/jovyan/data3/results/C%02d_T%03d/results.txt", numCastles, numTroops);
    printf("%s", results_filename);
    FILE* results_file = fopen(results_filename, "w");
    if (results_file == NULL) {
        printf("Unable to open file: %s\n", results_filename);
        return;
    }

    for (int i = 0; i < count; i++) {
        for (int j = 0; j < count; j++) {
            fprintf(results_file, "%d ", results[i][j]);
        }
        fprintf(results_file, "\n");
    }

    fclose(results_file);
}

// // Function to find factorial of given number (https://www.geeksforgeeks.org/c-program-for-factorial-of-a-number/)
// long long int factorial(long long int num) {
//     long long int result = 1, i;
 
//     for(i = 1; i <= num; i++) { // Start a loop to calculate factorial.
//         result = result * i;  // Calculate factorial.
//         printf("result = %llu\n", result);
//     }
    
//     return result;
// }

int count_lines(const char* filename) {
    FILE* file = fopen(filename, "r"); // Open the file for reading
    if (!file) {
        perror("Unable to open the file");
        return -1; // Return -1 to indicate error
    }

    int lines = 0;
    int ch;
    while(!feof(file)) {
        ch = fgetc(file);
        if(ch == '\n') {
            lines++;
        }
    }

    fclose(file); // Don't forget to close the file
    return lines;
}

// Function: tournament
// --------------------
// Conducts a tournament between all pairs of strategies.
//
// numCastles: Number of castles in the game.
// numTroops: Number of troops in the game.
//
void tournament(int numCastles, int numTroops) {
    char configurations_filename[100];
    // long long int max_configurations_numerator = factorial(numTroops+numCastles-1);
    // long long int max_configurations_denominator = factorial(numTroops)*factorial(numCastles-1);
    // long long int MAX_CONFIGURATIONS = max_configurations_numerator/max_configurations_denominator;
    // printf("MAX_CONFIGS =  %lld\n numerator = %lld\n denominator = %lld\n", MAX_CONFIGURATIONS,max_configurations_numerator,  max_configurations_denominator);
    
    // Create filename for the configurations file
    sprintf(configurations_filename, "/home/jovyan/data3/configurations/C%02d_T%03d.txt", numCastles, numTroops);

    int MAX_CONFIGURATIONS = count_lines(configurations_filename);
    int strategies[MAX_CONFIGURATIONS][numCastles];
    
    FILE* configurations_file = fopen(configurations_filename, "r");
    if (configurations_file == NULL) {
        printf("Unable to open file: %s\n", configurations_filename);
        return;
    }

    int count = 0;
    char line[1024];
    while (fgets(line, sizeof(line), configurations_file)) {
        char* token = strtok(line, ",");
        int index = 0;
        while (token != NULL && index < MAX_CONFIGURATIONS) {
            strategies[count][index++] = atoi(token);
            token = strtok(NULL, ",");
        }
        count++;
    }
    fclose(configurations_file);
    
    if (count == 0) {
        printf("No strategies read from the file.\n");
        return;
    }


        // Initialize results matrix
    int** results = (int**)malloc(MAX_CONFIGURATIONS * sizeof(int*));
    for (int i = 0; i < MAX_CONFIGURATIONS; i++) {
        results[i] = (int*)calloc(MAX_CONFIGURATIONS, sizeof(int)); // Use calloc to initialize to 0
    }

    for (int i = 0; i < MAX_CONFIGURATIONS; i++) {
        for (int j = 0; j < MAX_CONFIGURATIONS; j++) {
            if (i != j) {
                int result = game(strategies[i], strategies[j], numCastles);
                results[i][j] = result;
            }
        }
    }

    // Write results to file and free allocated memory
    writeResultsToFile(results, MAX_CONFIGURATIONS, numCastles, numTroops);
    for (int i = 0; i < MAX_CONFIGURATIONS; i++) {
        free(results[i]);
    }
    free(results);

}

int main(int argc, char *argv[]) {
    int numCastles = 0;
    int numTroops = 0;
    int opt;

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
    
    tournament(numCastles, numTroops);
    return 0;
}