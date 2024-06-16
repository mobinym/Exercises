#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool luhn_algorithm(char *card_number)
{
    int n = strlen(card_number);
    int sum1 = 0;
    for (int i = n - 2; i >= 0; i -= 2)
    {
        int product = (card_number[i] - '0') * 2;
        sum1 += product / 10 + product % 10;
    }

    int sum2 = 0;
    for (int i = n - 1; i >= 0; i -= 2)
    {
        sum2 += card_number[i] - '0';
    }

    return (sum1 + sum2) % 10 == 0;
}

void identify_card(char *card_number)
{
    if (!luhn_algorithm(card_number))
    {
        printf("INVALID\n");
        return;
    }

    int n = strlen(card_number);
    if (n == 15 && (strncmp(card_number, "34", 2) == 0 || strncmp(card_number, "37", 2) == 0))
    {
        printf("AMEX\n");
    }
    else if ((n == 13 || n == 16) && strncmp(card_number, "4", 1) == 0)
    {
        printf("VISA\n");
    }
    else if (n == 16 &&
             (strncmp(card_number, "51", 2) == 0 || strncmp(card_number, "52", 2) == 0 || strncmp(card_number, "53", 2) == 0 ||
              strncmp(card_number, "54", 2) == 0 || strncmp(card_number, "55", 2) == 0))
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

int main()
{
    char card_number[20];
    printf("Enter a credit card number: ");
    scanf("%s", card_number);

    identify_card(card_number);

    return 0;
}
