#02.08.2022

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(index):
    if index is not None:
        print("Target found in list: ", index)
    else:
        print("Target not found in list")
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
result = recursive_binary_search(numbers, 20)
verify(result)

result = recursive_binary_search(numbers, 5)
verify(result)