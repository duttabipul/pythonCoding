#03.08.2022
"""
print("Hello World")
#01:
name = input("input name: ")
age = input("enter age: ")
print(name, "is a new patient and", age,  " years old")
#02:
birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year)
print(age)

#03:
num1 = 10.5
num2 = 20
sum = num1 + num2
print(sum)

#04:
course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('a'))
print(course.replace('for', 'and'))
"""
#05:
x = 10 + 3 * 2
print(x)
y = 3 == 2
print(y)

price = 20
print(price < 15)
print(price>10)
temperature = 20
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
    print("Drink plenty of water")
elif temperature > 20:
    print("Its a normal day")
print("Done")
# 06:
weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = float(weight) / 0.45
    print("Weight in Pounds: ", converted)
else:
    converted = float(weight) * 0.45
    print("Weight in Kg: ", converted)
weight = input("Weight: ")
unit = input("(k)g or (l)bs: ")
if unit.upper() == "K":
    converted = float(weight) / 0.45
    print("Wight in Pound: ", converted)
else:
    converted = float(weight) * 0.45
    print("Weight in Kg: ", converted)
i = 1
while i <= 10:
    print(i)
    i = i + 1
"""
j = 1
while j <= 10:
    print(j * "*")
    j += 1
