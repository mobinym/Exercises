// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
const unsigned int NUM_BUCKETS = 100000;

// Hash table
node *table[NUM_BUCKETS];

// Number of words in dictionary
int dictionary_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hash_value = hash(word);
    node *current_node = table[hash_value];

    while (current_node != NULL)
    {
        if (strcasecmp(word, current_node->word) == 0)
        {
            return true;
        }
        current_node = current_node->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    long sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return sum % NUM_BUCKETS;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dictionary_file = fopen(dictionary, "r");
    if (dictionary_file == NULL)
    {
        printf("unable to open %s\n", dictionary);
        return false;
    }
    char next_word[LENGTH + 1];
    while (fscanf(dictionary_file, "%s", next_word) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }
        strcpy(new_node->word, next_word);
        int hash_value = hash(next_word);

        new_node->next = table[hash_value];
        table[hash_value] = new_node;
        dictionary_size++;
    }
    fclose(dictionary_file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dictionary_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < NUM_BUCKETS; i++)
    {
        node *current_node = table[i];
        while (current_node != NULL)
        {
            node *temp_node = current_node;
            current_node = current_node->next;
            free(temp_node);
        }
        if (current_node == NULL && i == NUM_BUCKETS - 1)
        {
            return true;
        }
    }
    return false;
}
