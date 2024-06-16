#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Open input file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    // Create buffer
    BYTE buffer[512];

    // Create counter for JPEGs
    int counter = 0;

    // Create filename array
    char filename[8];

    // Create output file
    FILE *img = NULL;

    // Read 512 bytes into buffer from file
    while (fread(buffer, 512, 1, file))
    {
        // Check if start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close current JPEG, if it exists
            if (counter > 0)
            {
                fclose(img);
            }

            // Create new JPEG
            sprintf(filename, "%03i.jpg", counter);
            img = fopen(filename, "w");

            // Write to new JPEG
            fwrite(buffer, 512, 1, img);

            // Increment counter
            counter++;
        }
        else if (counter > 0)
        {
            // Write to current JPEG
            fwrite(buffer, 512, 1, img);
        }
    }

    // Close last JPEG
    fclose(img);

    // Close input file
    fclose(file);

    return 0;
}
