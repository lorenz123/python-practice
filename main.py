import keyword

print("hello lance burat")

name, age = "Lance", 20
pi = 3.14
numbers = [1, 2, 3, 4]

print(name)
print(age)
print(pi)
print(numbers)

fullName = "Lance Ratbu"
PI = 3.14
isAdult = True

print(type(name))
print(type(age))
print(type(pi))
print(type(PI))
print(type(fullName))
print(type(numbers))
print(type(isAdult))

brand: str = "lance"
isAdult: bool = False


def hello():
    return "hello"


def helloWithDataType() -> str:
    return "hello"


# Comment
"""
Test1
test2
test3
"""

tester = ("Lance Test 1"
          "l;l;l;"
          "'p'p'p"
          "'p'p'p"
          "'p'p'p'p'")
print(tester.replace("L", "l"))
print(len(tester))
print(brand == "Last Test")
print(brand != "amigoscode")
print("Test" in tester)

email = """
hello {},
how are you?
"""

print(email.format(name))

email2 = f"""
hello {name},
how are you?
age {age}
"""

print(email2)


# indentation
def my_function():
    name2 = "Maria"
    surname = "Test"


# Reserved keywords
# def, and, is
print(keyword.kwlist)

# aritmethic operators
print(1 + 1)
print(2 * 2)
print(2 / 2)
print(2 ** 5)
print(10 % 2)

# comparison operators
print(10 > 2)
print(10 >= 2)
print(10 < 2)
print(10 <= 2)
print(10 != 2)
print(10 == 2)

# logical operators
print((10 > 2) and (5 > 1))
print((10 > 2) or (5 > 1))
print(10 > 2
      or 5 > 1
      and "A" == "c")
print(not("Test" == "Teste2"))

#assignment operators
number3 = 4
number3 += 2
number3 -= 2
number3 *= 2
number3 /= 2
number3 **= 2
print(number3)

#if statement

no = 1
if no > 0:
    print(f"number {no} is positive")
elif no == 0:
    print(f"number {no} is Zero")
else:
    print(f"number {no} is negative")

if not (no == 0):
    print(f"number {no} is equals to zero")

#ternary if statement
message = "positive" if no > 0 else "negative"
print(message)

#data structures
number_list = [1, 2, 3, 4, 0, -5, 0]
print(number_list)
print(number_list[0])
print(number_list[5])

# number_list.sort()
# number_list.reverse()
# number_list.append(1000)
# print(len(number_list))
# number_list.clear()
# print (0 in number_list)
# number_list.remove(1)
# number_list.pop()
# del number_list[0]
del number_list[0:3]
print(number_list)


numbersList = [1, 1] #can be duplicated, ordered
numbersSet = {1, 1}
lettersSet = {"A", "A", "B", "C", "C"} #no duplicate, unordered
print(numbersList)
print(numbersSet)
print(lettersSet)

lettersA = {"A", "B", "C", "D"}
lettersB = {"E", "F", "G", "D"}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB
print(union)
print(intersection)
print(f"Union = {union}")
print(f"Intersection = {intersection}")
print(f"Difference = {difference}")

person = {
    "name": "Lorenz",
    "age": 27,
    "address": "Prq"
}
print(person["name"])
print(person["age"])
print(person["address"])
print(person.keys())
print(person.values())
# person.clear()
print(person.get("age"))

person["age"] = 100
print(person)


namesList = ["Le", "La", "Lu", "Li", "Lo"]
namesSet = ["Le", "La", "Lu", "Li", "Lo"]
for name in namesSet:
    print(name)

for key in person:
    print(f"key = {key}, value = {person[key]}")

for key, value in person.items():
    print(f"key = {key}, value = {value}")

print(person.items())

# Exercise
result = 0
numberExercise = [1, 3, 5, 6, 7, 9]
for number in numberExercise:
    result += number

print(f"Result = {result}")
