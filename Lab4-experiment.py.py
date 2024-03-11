#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a program to create a set of user-defined functions to perform basicmathematical operations (addition, subtraction, multiplication, and division) and explore differentways of passing parameters to functions.
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))
print("Division:", divide(5, 3))


# In[2]:


# Create simple lambda functions for basic operations like addition, subtraction,multiplication, and division.Use lambda functions with built-in functions like filter() to filter elements from a list.Use lambda functions with built-in functions like map() to perform operations on each elementof a list.Use lambda functions with the sorted() function to customize sorting.
# Lambda functions for basic operations
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Cannot divide by zero"

# Using lambda functions with filter() to filter elements from a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))  # Filters even numbers
print(filtered_list)

# Using lambda functions with map() to perform operations on each element of a list
mapped_list = list(map(lambda x: x * 2, my_list))  # Doubles each element
print(mapped_list)

# Using lambda functions with sorted() to customize sorting
my_strings = ["apple", "banana", "cherry", "date"]
sorted_strings = sorted(my_strings, key=lambda x: len(x))  # Sorts by length
print(sorted_strings)


# In[4]:


def greet(name):
    print(f'Hello, {name}!')

PI = 3.14159

# main.py
import module

module.greet("Abhipsha")
print(module.PI)


# In[ ]:




