# ASSIGNMENT 3:
# Module 4: Functions & Modules in Python

                #  Task 1: Calculate Factorial Using a Function
a = int(input("Enter a number : "))
n=a
def factorial(n):

    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

factorial(n)
print("factorial of",n,"is",factorial(n))



                #Task 2: Using the Math Module for Calculations




import math
num2 = int(input("Enter a number : "))
num1=num2
def square(num1):
    sr=num1**(1/2)
    return sr
def log(num1):
    l=math.log(num1)
    return l
def sine(num1):
    sin=math.sin(num1)
    return sin
square(num1)
log(num1)
sine(num1)
print("Square root :",square(num1))
print("logarithm :",log(num1))
print("Sine :",sine(num1))