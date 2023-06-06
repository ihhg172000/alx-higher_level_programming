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
	listint_t *new = NULL, *curr = NULL, *temp = NULL;

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
		if (curr->n > new->n)
		{
			new->next = curr;

			if (temp == NULL)
				*head = new;
			else
				temp->next = new;

			return (new);
		}

		temp = curr;
		curr = curr->next;
	}

	if (temp != NULL)
		temp->next = new;
	else
		*head = new;

	return (new);
}
