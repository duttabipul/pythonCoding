#04.08.22
"""
#01:
lengh = 10
breadth = 20
area = lengh * breadth
perimeter = 2 * lengh * breadth
print("The area of the Rectangle:", area)
print("The perimeter of the Rectangle: ", perimeter)

#02:
# Write a program to calculate the perimeter of a triangle having sides of length
# 200,300 and 500 units.
# Perimeter = a + b + c
a = 200
b = 300
c = 500
perimeter = a + b + c
print(perimeter)
"""
#03
"""
03. Write a program to add 10 to the number 1000 and then divide it by 30. Now, the
modulus of the quotient is taken with 50 and then multiply the resultant value by
15. Display the final result.

number = 10
number += 1000
print(number)
divide = number/30
print(divide)
multi = divide%50
print("The final result is: ", multi)

#04
#  01. Write a Python program to sum all odd number items in a list
list1 = [10,20,31,45,56,60,75,84,93,109]
odd = []
for number in list1:
    if number %2 == 1:
        odd.append(number)
print("The odd number is: ", odd)
print("Sum of the odd numbers: ", sum(odd))

list1 = range(2, 50)
odd = []
for number in list1:
    if number %2 == 1:
        odd.append(number)
print("The even number is: ", odd)
print("Sum of the even numbers: ", sum(odd))

#06:
# 02. Write a Python program to multiply 5 with all the items in a list.
number = [25, 32, 12, 23, 41, 52]
for item in list:
    number = item * number
print(number)

def myList(num):
    number = 1

    for x in num:
        number = number * x
    return number
list = [25, 32, 12, 23, 41, 52]
print(myList(list))

number = [25, 32, 12, 23, 41, 52]
for i in number:
    number = i * 5
print(number)

# 07:
# 03. Write a Python program to check a list is empty or not.
def inquiry(list):
    if len(list) == 0:
        return 0
    else:
        return 1
while list == []:
    print("The list is empty")
else:
    print("The list is not empty")

def inquiry(list):
    if len(list) == 0:
        return 0
    else:
        return 1

while list == 0:
    print("This is a empty list")
else:
    print("This is not a empty list")

# 04. Write a Python program to print a specified list after removing the 1st and 3rd
# elements.
list = ['P', 'Y', 'T', 'H', 'O', 'N']
list.remove('H')
print(list)

# 01. Write a Python program to accept two integers and check whether they are equal or
# not.
num1 = input("Enter value 1: ")
num2 = input("Enter value 2: ")

if num1 <= num2:
    print("Number 2 is greater than number 1")
else:
    print("Number 2 lis less than number 1")
if num1 == num2:
    print("Number1 and number 2 is equal")
"""
# 02. Write a Python program to read the value of an integer “num” and display the value
# of 100 when num is larger than 0, 0 when num is 0, and -1 when num is less than 0.

num = int(input("Enter a number: "))

if num > 0:
    print("The number is greater than zero")
elif num == 0:
    print("The number is equal to zero")
else:
    print("The number is less than zero")