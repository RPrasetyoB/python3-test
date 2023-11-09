# First Duplicate
# HIDE QUESTION
# And your task is to find the first element that appears more than once in the array. Implement a function find_first_duplicate(arr) that returns:
# the first duplicate element or -1 if there are no duplicates.

# input == [1,3,4,2,2,5,6]

def find_first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

result = find_first_duplicate(input())
print(result)