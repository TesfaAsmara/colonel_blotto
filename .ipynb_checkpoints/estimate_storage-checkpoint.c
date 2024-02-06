#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>

void processFolder(const char* foldername) {
    DIR *dir;
    struct dirent *entry;
    struct stat filestat;
    long long totalSize = 0;
    int fileCount = 0;

    dir = opendir(foldername);
    if (dir == NULL) {
        perror("Unable to open directory");
        return;
    }

    while ((entry = readdir(dir)) != NULL) {
        char path[1024];
        snprintf(path, sizeof(path), "%s/%s", foldername, entry->d_name);
        
        if (stat(path, &filestat) == 0 && S_ISREG(filestat.st_mode)) {
            totalSize += filestat.st_size;
            fileCount++;
        }
    }

    closedir(dir);

    if (fileCount > 0) {
        printf("Folder: %s\n", foldername);
        printf("Total Size: %lld bytes\n", totalSize);
        printf("Number of files: %d\n", fileCount);
        printf("Average file size: %lld bytes\n\n", totalSize / fileCount);
    }
}

int main() {
    DIR *dir;
    struct dirent *entry;
    char resultsFolder[] = "results/";

    dir = opendir(resultsFolder);
    if (dir == NULL) {
        perror("Unable to open results folder");
        return 1;
    }

    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_DIR && strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0) {
            char subfolderPath[1024];
            snprintf(subfolderPath, sizeof(subfolderPath), "%s%s", resultsFolder, entry->d_name);
            processFolder(subfolderPath);
        }
    }

    closedir(dir);
    return 0;
}
