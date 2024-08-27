#!/usr/bin/env python3

def greet_programmer():
     print("Hello, programmer!")


def greet(name):
    print(f"Hello Dear, {name}!")

def greet_with_default(name="programmer"):
   print(f"Hello Mr.Bob, {name}!")  

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number/2


greet_programmer()
greet("Liz")
greet_with_default()
greet_with_default("Charlton")
sum_value = add(6, 12)
half_value = halve(20)
