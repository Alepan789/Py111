"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

queue_prior = []


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    queue_prior.append({"val": elem, "prior": priority})
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.
    :return: dequeued element
    """
    if queue_prior:
        prior = queue_prior[0]["prior"]
        i = 0
        rez_index = 0
        while i < len(queue_prior) - 1:
            i += 1
            if prior > queue_prior[i]["prior"]:
                prior = queue_prior[i]["prior"]
                rez_index = i
        return queue_prior.pop(rez_index)["val"]
    return


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if not queue_prior:
        return None
    if ind + 1 > len(queue_prior):
        return
    i = 0
    j = 0
    while i <= len(queue_prior) and j <= ind:
        if queue_prior[i]["prior"] == priority:
            if j == ind:
                return queue_prior[i]["val"]
            j += 1
        i += 1
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    queue_prior.clear()
    return None


""" tests
high_priority = 0
medium_priority = 5
low_priority = 10
enqueue(10, high_priority)
enqueue(0, low_priority)
print('10,5', queue_prior)
print(dequeue())
enqueue(1, low_priority)
enqueue(5, medium_priority)
print('1,5', queue_prior)
# self.assertEqual(5, priority_queue.
print(dequeue())
# self.assertEqual(0, priority_queue.
print(dequeue())
# self.assertEqual(1, priority_queue.
print(dequeue())

queue_prior.append({"val": 7, "prior": 0})
queue_prior.append({"val": 1, "prior": 5})
print(queue_prior)
print(queue_prior.pop(-1)["val"])
print(queue_prior, dequeue())
clear()
enqueue(3)
enqueue(5)
enqueue(7)
print(peek())
print(peek(1))
print(peek())
print(queue_prior)

# print(queue_prior[0]["val"])
# print(queue_prior.pop(-2)["val"])
# print(queue_prior)
# """
