"""
rows = 10

for i in range(1, rows+1):
    for j in range(rows-i, 0, -1):
        print(j, end=' ')
    print('\r')
# Question: Linear Search:
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print(list1)

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
        return None

def verify(index):
    if index is not None:
        print("Target found in index: ", index)
    else:
        print("Target not fount in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 12)
verify(result)

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
def verify(index):
    if index is not None:
        print("Target found in list: ", index)
    else:
        print("Target not found in list")
numbers = [1,2,3,4,5,6,7,8,9,10,11]
result = linear_search(numbers, 12)
verify(result)

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
def verify(index):
    if index is not None:
        print("Target found in list: ", index)
    else:
        print("Target not found in list")
numbers = [1,2,3,4,5,6,7,8,9]
result = linear_search(numbers, 9)
verify(result)
"""
#02.08.2022

# Binary Search:
def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

def verify(index):
    if index is not None:
        print("Target found in list: ", index)
    else:
        print("Target not found in list")
    return None
numbers = [1,2,3,4,5,6,7,8,9]
result = binary_search(numbers, 7)
verify(result)