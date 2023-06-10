#include "lists.h"
#include <stdio.h>

/**
 * length - returns the length of a linked list.
 * @head: the head of the linked list.
 *
 * Return: the length of a linked list.
 */
size_t length(listint_t *head)
{
	int length = 0;

	if (!head)
		return (0);

	while (head)
	{
		length++;
		head = head->next;
	}

	return (length);
}

/**
 * reverse - reverses a linked list.
 * @head: a pointer to the head of the linked list.
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL, *curr = NULL, *next = NULL;

	if (!head || !(*head))
		return;

	curr = *head;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
}

/**
 * compare - compares two linked list.
 * @first: first linked list.
 * @second: second linked list.
 * @n: the number of nodes to be compered.
 *
 * Return: 1 if the two linked list are the same, 0 otherwise.
 */
int compare(listint_t *first, listint_t *second, size_t n)
{
	size_t i;

	for (i = 1; i <= n; i++)
	{
		if (first->n != second->n)
			return (0);

		first = first->next;
		second = second->next;
	}

	return (1);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: a pointer to the head of the linked list.
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	listint_t *first_half, *mid, *second_half;
	size_t len, i;

	if (!head || !(*head))
		return (1);

	len = length(*head);
	first_half = mid = *head;

	for (i = 1; i < (len % 2 == 0 ? len / 2 : (len / 2) + 1); i++)
		mid = mid->next;

	second_half = mid->next;
	mid->next = NULL;

	reverse(&second_half);

	i = compare(first_half, second_half, len / 2);

	reverse(&second_half);

	mid->next = second_half;

	return (i);
}
