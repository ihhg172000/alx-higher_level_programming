#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list.
* @head: a pointer to a pointer that points to the head of the linked list.
* @number: the number.
*
* Return: the address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curr, *temp;

	new = malloc(sizeof(listint_t));

	if (head == NULL || new == NULL)
	{
		free(new);
		return (NULL);
	}

	new->n = number;
	new->next = NULL;


	curr = *head;

	while (curr != NULL)
	{
		if (curr->next->n >= new->n)
		{
			temp = curr->next;
			curr->next = new;
			new->next = temp;
			return (new);
		}

		curr = curr->next;
	}

	*head = new;
	return (new);
}
