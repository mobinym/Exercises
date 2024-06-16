#include <stdio.h>
#include <cs50.h>
// start
int main()
{
    int n;
    char input[3];
    // Keep prompting the user for input until they enter a valid number
    while (1)
    {
        //input number
        printf("Enter a number between 1 and 8: ");
        fgets(input, 3, stdin);
        sscanf(input, "%d", &n);
        // If the user's input is between 1 and 8, break out of the loop
        if (n >= 1 && n <= 8)
        {
            break;
        }

    }
    // Print the pyramid
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < n - i; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
