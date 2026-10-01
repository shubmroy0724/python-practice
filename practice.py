# Q1 write a pogram to input marks in five subjects and calculate the total , percentage and grade.

# english = int(input("enter your marks"))
# hindi = int(input("enter your marks"))
# science= int(input("enter your marks"))
# history = int(input("enter your name"))
# sanskrit = int(input("enter your name"))

# total = english+ hindi+ science+ history+sanskrit
# percentage = total/5
# print(percentage)

# if percentage >= 90:
#    print ("grade B")
# elif percentage >= 75:
#     print ("grade B")
# elif percentage >= 60:
#     print ("grade C")
# elif percentage >= 40:
#     print ("grade D")
# else:
#     print ("grade F")


#Q2 is Leap Year. The key is learning the condition, not just memorizing the code.

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap Year")
# elif year % 100 == 0:
#     print("Not a Leap Year")
# elif year % 4 == 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

#Q3 is Largest & Second Largest — find the largest and second-largest number among three numbers.
 
# num1= int(input("enter your first number"))
# num2 =int(input("enter your second name"))
# num3  =int(input("enter your third number"))


# if num1>= num2 and num1 >= num3:
#     print("largest num1")
# elif num2 >= num1 and num2 >= num3:
#     print("largest num2")

# else:
#     print("largest num3")

#Q4 is Electricity Bill — calculate the bill according to different slab rates.
 
# unit = int(input("enter unit is consume:"))

# if unit <= 100:
#     bill=unit*5
# elif unit <= 200:
#     bill=100*5+(unit-100)*7
# elif unit <= 300:
#     bill=100*5+100*7+(unit-200)*10
# else: 
#     bill=100*5+100*7+100*10+(unit-300)*15

# print("enter bill:",bill)    Q5 — Armstrong Number

#Q5: Write a program to check whether a number is an Armstrong number.

# num=int(input("enter a number:"))
# original=num
# total=0

# while num > 0:
#     digit = num % 10
#     total = total+ digit**3
#     num =num//10

# if total==original:
#     print("armstrong number")
# else:
#     print("not an armstrong number")  

#06. String Slicing
## Input a string and print the first 3 characters, last 3 characters, every alternate character, and the reversed string.

# s = input("Input the string:") 
# print("First 3 characters:", s[:3]) 
# print("Last 3 characters:", s[-3:]) 
# print("Alternate characters:", s[::2]) 
# print("Reversed string:", s[::-1])

# 07. Character Classification
# Count the number of vowels, consonants, digits, and special characters in a string.

# string = input('Enter string:')
# vowels = consonants = digits = specials = 0

# for i in string:
#     if i.isdigit():
#         digits += 1
#     elif i.isalpha():
#         if i.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
#     else:
#         specials += 1

# print('Vowels:', vowels)
# print('Consonants:', consonants)

# 08. Palindrome Using Slicing
# Check whether a string is a palindrome using slicing.

# string = input("Enter a string:")

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 09. Character Frequency
# Find the frequency of each character in a string.

# s = input('Enter string:')
# frequency = {}

# for i in s:
#     frequency[i] = frequency.get(i, 0) + 1

# print(frequency)

# 10. Spaces & Word Count 
## Remove all spaces from a string and count the number of words.

# s = input("Enter string:")
# no_spaces = s.replace(" ", "")
# word_count = s.split()

# print("String without spaces:", no_spaces)
# print("Number of words:", len(word_count))

# 11. Prime Numbers 
# Remove all spaces from a string and count the number of words.

# n = int(input("Enter Number:"))

# for num in range(2, n + 1):
#     is_prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num, end=" ")

## 12. Fibonacci Sequence 
## Generate the Fibonacci sequence up to N terms using loops.

# n = int(input("Enter number of terms:"))

# a, b = 0, 1

# for i in range(0, n):
#     print(a, end=' ')
#     a, b = b, a + b

# 13. Factors of a Number 
## Find all factors of a given number.

# number = int(input("Enter number:"))

# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i, end=" ")

# 14 Factors Practice

num = int(input("Enter number: "))
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print("Factors:", factors)

# 15 Floyd's Triangle

n = int(input("Enter rows: "))
number = 1

for i in range(1, n + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()

# 16 List Statistics

numbers = list(map(int, input("Enter numbers: ").split()))

print("Largest:", max(numbers))
print("Smallest:", min(numbers))
print("Average:", sum(numbers) / len(numbers))

# 17 Remove Duplicates

numbers = list(map(int, input("Enter numbers: ").split()))
new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print("Without duplicates:", new_list)

# 18 Second Largest and Smallest

numbers = list(map(int, input("Enter numbers: ").split()))
numbers.sort()

print("Second smallest:", numbers[1])
print("Second largest:", numbers[-2])

# 19 Even and Odd Lists

numbers = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)

# 20 List Rotation

numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter K: "))

rotated = numbers[k:] + numbers[:k]

print("Rotated list:", rotated)

# 1 Squares using list comprehension

squares = [x * x for x in range(1, 51)]
print(squares)

# 2 Prime numbers using list comprehension

prime_numbers = []

for num in range(2, 101):
    check = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            check = False
            break

    if check:
        prime_numbers.append(num)

print("Prime numbers:", prime_numbers)

# 3 Convert strings to uppercase

words = ["python", "java", "html", "css"]

upper_words = [word.upper() for word in words]

print(upper_words)

# 4 Word Lengths

sentence = input("Enter sentence: ")

lengths = [len(word) for word in sentence.split()]

print(lengths)

# 5 Remove Empty Strings

data = ["Python", "", "Java", " ", "HTML", "", "CSS"]

result = [item for item in data if item.strip()]

print(result)

# 6 Prime Function

def is_prime(number):
    if number < 2:
        return False

    i = 2

    while i <= number ** 0.5:
        if number % i == 0:
            return False
        i += 1

    return True

num = int(input("Enter number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not Prime Number")

# 7 GCD Function

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD:", gcd(num1, num2))

# 8 Second Largest Function

def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

nums = [10, 5, 30, 20, 15]

print("Second largest:", second_largest(nums))

# 9 Longest Word

def longest_word(sentence):
    words = sentence.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

sentence = input("Enter sentence: ")

print("Longest word:", longest_word(sentence))

# 10 Merge and Remove Duplicates

def merge_lists(list1, list2):
    answer = []

    for item in list1 + list2:
        if item not in answer:
            answer.append(item)

    return answer

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

print("Merged:", merge_lists(list1, list2))

# 11 Common Elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

common = []

for x in list1:
    if x in list2:
        common.append(x)

print("Common:", common)

# 12 Missing Number

numbers = [1, 2, 3, 5, 6]
n = 6

total = n * (n + 1) // 2
list_total = sum(numbers)

missing = total - list_total

print("Missing number:", missing)

# 13 Element Frequency

numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}

for n in numbers:
    frequency[n] = frequency.get(n, 0) + 1

print("Frequency:", frequency)

# 14 Sort without sort()

numbers = [5, 3, 8, 1, 2]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print(numbers)

# 15 Diamond Pattern

n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

# 16 Safe Division

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter numbers only")

# 17 Valid Integer

while True:
    try:
        num = int(input("Enter integer: "))
        print("Valid integer:", num)
        break

    except ValueError:
        print("Invalid input")

# 18 Index Error

numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except IndexError:
    print("Index is out of range")

except ValueError:
    print("Enter a number")

# 19 File Not Found

try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found")

# 20 Menu Calculator

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Exiting...")
        break

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)

        elif choice == "2":
            print("Result:", a - b)

        elif choice == "3":
            print("Result:", a * b)

        elif choice == "4":
            print("Result:", a / b)

        else:
            print("Wrong choice")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    except ValueError:
        print("Invalid input")

# 1 Factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

number = int(input("Enter number: "))

print("Factorial:", factorial(number))

# 2 Fibonacci using recursion

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")

print()

# 3 Sum of Digits using recursion

def sum_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)

num = int(input("Enter number: "))

print("Sum of digits:", sum_digits(num))

# 4 Reverse String using recursion

def reverse_string(s):
    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0]

s = input("Enter string: ")

print("Reverse:", reverse_string(s))

# 5 Tower of Hanoi

def tower(n, source, destination, helper):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower(n - 1, source, helper, destination)

    print("Move disk", n, "from", source, "to", destination)

    tower(n - 1, helper, destination, source)

disks = int(input("Enter number of disks: "))

tower(disks, "A", "C", "B")

# 6 Recursive Palindrome

def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

s = input("Enter word: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")

# 7 Prime numbers using helper function

def prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

numbers = [n for n in range(1, 101) if prime(n)]

print(numbers)

# 8 Numbers until stop

numbers = []

while True:
    value = input("Enter number or stop: ")

    if value.lower() == "stop":
        break

    try:
        numbers.append(float(value))

    except ValueError:
        print("Invalid input")

if numbers:
    numbers.sort()

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    middle = len(numbers) // 2

    if len(numbers) % 2 == 0:
        median = (numbers[middle - 1] + numbers[middle]) / 2
    else:
        median = numbers[middle]

    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", average)
    print("Median:", median)
else:
    print("No numbers entered")

# 9 Flatten Nested List

def flatten(lst):
    result = []

    for item in lst:
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)

    return result

nested_list = [1, [2, 3], [4, [5, 6]], 7]

print("Flattened:", flatten(nested_list))

# 10 Student Record Management System

students = []

def add_student():
    try:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        student = [roll, name, age, course]
        students.append(student)

        print("Student added")

    except ValueError:
        print("Please enter valid details")

def view_students():
    if len(students) == 0:
        print("No student records")
    else:
        print("\nStudent Records")

        for student in students:
            print("Roll No:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("----------------")

def search_student():
    name = input("Enter name to search: ")

    found = False

    for student in students:
        if student[1].lower() == name.lower():
            print("Student found")
            print("Roll No:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            found = True

    if not found:
        print("Student not found")

def save_students():
    try:
        file = open("students.txt", "w")

        for student in students:
            file.write(
                str(student[0]) + "," +
                student[1] + "," +
                str(student[2]) + "," +
                student[3] + "\n"
            )

        file.close()
        print("Records saved")

    except Exception as e:
        print("Error:", e)

def load_students():
    try:
        file = open("students.txt", "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                student = [
                    int(data[0]),
                    data[1],
                    int(data[2]),
                    data[3]
                ]

                students.append(student)

        file.close()

    except FileNotFoundError:
        print("No previous records found")

    except Exception as e:
        print("Error:", e)

load_students()

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Save Students")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            save_students()

        elif choice == 5:
            save_students()
            print("Thank you")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a number from 1 to 5")




















    


