## 1. Program to read three numbers (a, b, c) and count numbers between a and b divisible by c

```python
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

count = 0

for i in range(a, b + 1):
    if i % c == 0:
        count += 1

print("Numbers divisible by", c, "between", a, "and", b, ":", count)
```

---

## 2. Program to find the sum of all even numbers from 0 to 10 using while loop

```python
sum_even = 0
i = 0

while i <= 10:
    if i % 2 == 0:
        sum_even += i
    i += 1

print("Sum of even numbers from 0 to 10 is:", sum_even)
```

---

## 3. Program to check number entered by the user is prime number or not using function

```python
def prime(n):
    if n <= 1:
        print("Not a Prime number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not a Prime number")
                break
        else:
            print("Prime number")

num = int(input("Enter a number: "))
prime(num)
```

---

## 4. Program to find factorial of a number using conditional statements

```python
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial is 1")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial of", num, "is", fact)
```

---

## 5. WAP to find the greatest of three numbers entered by user using conditional statements

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number is:", a)
elif b >= a and b >= c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)
```

---

## 6. Program to check whether a number is even or odd using if-else

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
```

---

## 7. WAP to check whether a given number is prime using nested if-else

```python
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime number")
            break
    else:
        print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
```

---

## 8. Program to implement different types of operators in Python

```python
a = 10
b = 3

print("Arithmetic Operators")
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("Relational Operators")
print(a > b)
print(a < b)
print(a == b)

print("Logical Operators")
print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > b))
```

---

## 9. Program to read a text file and print words of specified length

```python
length = int(input("Enter word length: "))

file = open("sample.txt", "r")
text = file.read()
words = text.split()

print("Words of length", length, ":")
for word in words:
    if len(word) == length:
        print(word)

file.close()
```

---

## 10. Program to implement a simple calculator using functions

```python
def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    
    if b == 0:
        print("Division not possible")
    else:
        print("Division:", a / b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

calculator(a, b)
```

---

## 11. Write a Python program that takes two numbers as input and performs division. Implement exception handling to manage division by zero and invalid input errors gracefully

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Please enter valid integers")

except Exception:
    print("Something went wrong")
```

---

## 12. Write a python program to display to print the Fibonacci sequence up to n-th term using a while loop

```python
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

print("Fibonacci sequence:")

while i <= n:
    print(a, end=" ")
    a = b
    b = a + b
    i += 1
```

---
