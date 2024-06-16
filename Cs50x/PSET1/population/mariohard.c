#include <stdio.h>
#include <cs50.h>
int main() {
    int n;
    // Keep prompting the user for input until they enter a valid number
    do {
        printf("Enter a number between 1 and 8: ");
        scanf("%d", &n);
    } while (n < 1 || n > 8);

    // Print the pyramid
    for (int i = 1; i <= n; i++) {
        // Print the spaces before the # symbols on each row
        for (int j = 0; j < n - i; j++) {
            printf(" ");
        }
        // Print the # symbols on each row
        for (int k = 0; k < i; k++) {
            printf("#");
        }
        // Print two spaces between the columns
        printf("  ");
        // Print the # symbols on each row again for the second column
        for (int k = 0; k < i; k++) {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
