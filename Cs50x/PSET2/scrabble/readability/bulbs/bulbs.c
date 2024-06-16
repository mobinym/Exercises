#include <cs50.h>
#include <stdio.h>
#include <string.h>

void print_bulb(int state);

int main(void)
{
    // Prompt user for message
    string message = get_string("Message: ");

    // Convert message to binary
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        for (int j = 7; j >= 0; j--)
        {
            print_bulb((message[i] >> j) & 1);
        }
        printf("\n");
    }
}

// Prints a light bulb emoji
void print_bulb(int state)
{
    if (state == 0)
    {
        printf("⚫");
    }
    else
    {
        printf("🟡");
    }
}
