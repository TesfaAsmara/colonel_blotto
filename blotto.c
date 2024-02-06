#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Define the maximum number of castles and strategies
// and the maximum length of filenames for results
// create results/C02_T03/ folder
#define MAX_CASTLES 5
#define MAX_STRATEGIES 1001
#define MAX_FILENAME_LENGTH 100
#define STRATEGY_FILE "configurations.txt"

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
            p1_score += n + 1;
            p1_wbt++;
            p2_wbt = 0;
        } else if (player1[n] < player2[n]) {
            p2_score += n + 1;
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
        p1_score += n + 1;
        n++;
    }
    while (p2_wbt == 3 && n < numCastles) {
        p2_score += n + 1;
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
    sprintf(filename, "results/C%02d_T%03d/%d_%d_%d.txt", numCastles, numTroops, i, j, result);
    FILE* file = fopen(filename, "w");
    if (file != NULL) {
        fclose(file);
    } else {
        printf("Unable to open file: %s\n", filename);
    }
}

// Function: read_strategies
// --------------------
// Reads strategies from a file and stores them in an array.
//
// filename: Name of the file containing strategies.
// strategies: 2D array where the read strategies will be stored.
//
// returns: Number of strategies read from the file.
//
int read_strategies(const char* filename, int strategies[][MAX_CASTLES]) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Unable to open file: %s\n", filename);
        return 0;
    }

    int count = 0;
    char line[1024];
    while (fgets(line, sizeof(line), file)) {
        char* token = strtok(line, ",");
        int index = 0;
        while (token != NULL && index < MAX_CASTLES) {
            strategies[count][index++] = atoi(token);
            token = strtok(NULL, ",");
        }
        count++;
    }
    fclose(file);
    return count;
}

// Function: tournament
// --------------------
// Conducts a tournament between all pairs of strategies.
//
// numCastles: Number of castles in the game.
// numTroops: Number of troops in the game.
//
void tournament(int numCastles, int numTroops) {
    int strategies[MAX_STRATEGIES][MAX_CASTLES];
    int count = read_strategies(STRATEGY_FILE, strategies);
    if (count == 0) {
        printf("No strategies read from the file.\n");
        return;
    }

    for (int i = 0; i < count; i++) {
        for (int j = 0; j < count; j++) {
            if (i != j) {
                play_game(i, j, strategies[i], strategies[j], numCastles, numTroops);
            }
        }
    }
}

int main() {
    int numCastles = 5, numTroops = 10;
    tournament(numCastles, numTroops);
    return 0;
}