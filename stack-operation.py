# Stack Operation
# You are tasked with implementing a basic stack data structure in Python. Your stack should support the following operations:
# push(val: int): Push a new integer value onto the top of the stack.
# pop() -> int: Pop the top element from the stack and return its value.
# is_empty() -> bool: Return True if the stack is empty, False otherwise.
# list_to_stack(): convert list to stack

import pytest

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def list_to_stack(self, input_list):
        for val in input_list:
            self.push(val)

    def display(self):
        return self.stack


# do not modify this function call
retcode = pytest.main(['-v'])