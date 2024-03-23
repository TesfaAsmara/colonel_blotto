#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fp, *outputFile;
    char path[1035];
    char command[256];
    int castles[] = {2, 3}; // Example castle numbers
    int troops[] = {5, 10, 20, 30 ,40, 50, 60, 70, 80, 90, 100}; // Example troop numbers
    int num_castles = sizeof(castles) / sizeof(castles[0]);
    int num_troops = sizeof(troops) / sizeof(troops[0]);

    // Open output file
    outputFile = fopen("directory_sizes.txt", "w");
    if (outputFile == NULL) {
        perror("Unable to open output file");
        exit(1);
    }

    for (int i = 0; i < num_castles; ++i) {
        for (int j = 0; j < num_troops; ++j) {
            // Format the command with the current castle and troop numbers
            snprintf(command, sizeof(command), "du -s /home/jovyan/data3/results/C%02d_T%03d/", castles[i], troops[j]);

            // Open the command for reading
            fp = popen(command, "r");
            if (fp == NULL) {
                printf("Failed to run command\n");
                continue; // Skip this iteration
            }

            // Read the output a line at a time - output it
            while (fgets(path, sizeof(path)-1, fp) != NULL) {
                // Extract directory size and path
                char *size = strtok(path, "\t");
                char *directoryPath = strtok(NULL, "\n");

                // Write directory name and size to output file
                if (size && directoryPath) {
                    fprintf(outputFile, "%s: %s bytes\n", directoryPath, size);
                }
            }

            // Close the command file pointer for the current command
            pclose(fp);
        }
    }

    // Close the output file
    fclose(outputFile);

    printf("Directory sizes have been written to directory_sizes.txt\n");

    return 0;
}
