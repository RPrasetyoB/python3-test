# Queue Operation
# You're tasked with implementing a queue data structure in Python.
# The queue should support operations to enqueue and dequeue elements. The main focus will be on the dequeue operation.
# enqueue(val: str): Push a new integer value onto the top of the stack.
# dequeue(count: int) -> List[str]: Remove a specified number of elements from the front of the queue and return them as a list. If the params is negative, the queue is doesnt change at all.
# list_to_queue(): convert list to queue.

import pytest

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None  # Return None when the queue is empty

    def is_empty(self):
        return len(self.queue) == 0

    def list_to_queue(self, input_list):
        self.queue.extend(input_list)

    def display(self):
        return self.queue


# do not modify this function call
retcode = pytest.main(['-v'])