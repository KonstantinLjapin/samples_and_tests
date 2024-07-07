#include <stdio.h>
#include <stdlib.h>
#include <math.h>


typedef struct {
    int x;
    int y;
} Coordinates;

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <coordinates_file> <blast_radius>\n", argv[0]);
        return 1;
    }
    int count_line = 0;
    char *filename = argv[1];
    int blast_radius = atoi(argv[2]);
    
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Error opening file.\n");
        return 1;
    }
    
    Coordinates target;
    Coordinates sub_target;
    Coordinates op_point;
    Coordinates points[100];
    int num_targets = 1;
    
    
    while (fscanf(file, "%d, %d\n", &target.x, &target.y) == 2) {
        points[count_line]=target;
        count_line +=1;
    }
    fclose(file);
    for (size_t i = 0; i < count_line; i++)
    {
        target = points[i];
        int temp = 0;
        for (size_t j = 0; j < count_line; j++)
        {
            sub_target = points[j];
            //(x - xk) ** 2 / r ** 2 + (y - yk) ** 2 / r ** 2 < 1
            if ( pow((target.x - sub_target.x),2) / pow(blast_radius,2) + pow((target.y - sub_target.y),2) / pow(blast_radius,2) < 1)
            {
                temp+=1;
                if (temp>=num_targets)
                {
                    num_targets=temp;
                    op_point=target;
                }
    
            }
        }
        
    }
    

    printf("Координаты оптимальной точки, куда следует произвести запуск: (%d, %d)\n", op_point.x, op_point.y);
    printf("Количество поражённых целей: %d\n", num_targets);
    
    
    return 0;
}
