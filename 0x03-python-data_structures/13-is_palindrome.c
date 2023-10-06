#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow = NULL, *second_half;
    int is_pal = 1; // Assume the list is a palindrome by default

    slow = fast = *head;

    // Find the middle of the list
    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // If the list has odd number of nodes, move slow to the next node
    if (fast)
        slow = slow->next;

    // Reverse the second half of the list
    second_half = slow;
    prev_slow->next = NULL;
    reverse_list(&second_half);

    // Compare the first half with the reversed second half
    while (*head && second_half)
    {
        if ((*head)->n != second_half->n)
        {
            is_pal = 0;
            break;
        }
        *head = (*head)->next;
        second_half = second_half->next;
    }

    // Restore the original list
    reverse_list(&second_half);
    if (prev_slow)
        prev_slow->next = slow;

    return is_pal;
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}
