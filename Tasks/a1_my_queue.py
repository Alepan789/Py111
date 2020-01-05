"""
My little Queue
"""
from typing import Any

queue = []


def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	queue.append(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue. Should return None if no elements.

	:return: dequeued element
	"""
	if queue:
		return queue.pop(0)
	return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	if len(queue) > ind:
		return queue[ind]
	return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	queue.clear()
	return None

""" tests 
enqueue(1)
enqueue(2)
enqueue(3)
print(queue)
print(queue, len(queue))
print(dequeue())
print(queue, peek(), peek(1))
# peek()
"""