#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_LINE_LENGTH 100

typedef struct {
    int x;
    int y;
} Coordinates;

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <coordinates_file> <blast_radius>\n", argv[0]);
        return 1;
    }
    
    char *filename = argv[1];
    int blast_radius = atoi(argv[2]);
    
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Error opening file.\n");
        return 1;
    }
    
    Coordinates target;
    Coordinates optimal_point = {0, 0};
    int num_targets = 0;
    
    while (fscanf(file, "%d, %d\n", &target.x, &target.y) == 2) {
        double distance = sqrt(pow(target.x, 2) + pow(target.y, 2));
        printf("Point: (%d, %d)\n", target.x, target.y);
        if (distance <= blast_radius) {
            num_targets++;
            if (distance > sqrt(pow(optimal_point.x, 2) + pow(optimal_point.y, 2))) {
                optimal_point = target;
            }
        }
    }
    
    printf("Optimal launch point: (%d, %d)\n", optimal_point.x, optimal_point.y);
    printf("Number of targets hit: %d\n", num_targets);
    
    fclose(file);
    
    return 0;
}
