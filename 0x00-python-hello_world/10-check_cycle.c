#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check cycle in a linked list
 * @list:  list
 * Return: 1 or 0
*/
int check_cycle(listint_t *list)
{
	listint_t *move_one = list, *move_two = list;

	while (move_one && move_two && move_two->next)
	{
		move_one = move_one->next;
		move_two = move_two->next->next;
		if (move_one == move_two)
		{
			return (1);
		}
	}
	return (0);
}
