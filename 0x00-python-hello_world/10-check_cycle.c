#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;           // Move slow pointer by one step
        fast = fast->next->next;     // Move fast pointer by two steps

        if (slow == fast)
            return (1);  // If they meet, there's a cycle
    }

    return (0);  // If they don't meet, there's no cycle
}
