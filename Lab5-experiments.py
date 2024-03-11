#!/usr/bin/env python
# coding: utf-8

# In[4]:


#experiment7: Create a list of numbers and perform various operations such as adding element, removing elements, and accessing elements by index.

numbers = []
n = int(input("Enter number of elements : "))
print("enter the numbers list:")
for i in range(0,n):
    a = int(input())
    numbers.append(a)

print("Original list:", numbers)

numbers.append(6)
print("List after appending:", numbers)

# Inserting an element at a specific position
numbers.insert(2, 10)
print("List after inserting 10 at index 2:", numbers)

b = int(input("enter no. you want to remove: "))
numbers.remove(b)
print("List after removing:", numbers)

# Extending the list with another list
numbers.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", numbers)

# Sum of all elements in the list
sum_of_elements = sum(numbers)
print("Sum of all elements:", sum_of_elements)

# Sorting the list
numbers.sort()
print("Sorted list:", numbers)

# Reversing the list
numbers.reverse()
print("Reversed list:", numbers)



# In[ ]:


#Experiment-8: Create a tuple to represent an immutable collection and try accessing elements and performing basic operations.

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Sliced tuple:", my_tuple[1:4])

# Length of the tuple
print("Length of tuple:", len(my_tuple))

# Concatenating tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Repeating elements
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)

# Checking membership
print("Is 3 present in the tuple?", 3 in my_tuple)

# Counting occurrences
print("Number of occurrences of 4:", my_tuple.count(4))

# Finding index
print("Index of 4:", my_tuple.index(4))

# Iterating over the tuple
print("Iterating over the tuple:")
for element in my_tuple:
    print(element)


# In[5]:


#Experiment-9: Create a set to store unique elements and perform set operations such as union, intersection, and difference.
# Create sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference of sets (elements present in set1 but not in set2)
difference_set1 = set1.difference(set2)
print("Difference (set1 - set2):", difference_set1)

# Difference of sets (elements present in set2 but not in set1)
difference_set2 = set2.difference(set1)
print("Difference (set2 - set1):", difference_set2)


# In[7]:


#Experiment-10: Create a dictionary to represent key-value pairs and perform operations like adding, updating, and accessing values.
my_dict = {'name': 'Abhipsha', 'age': 20, 'city': 'Bhubaneswar'}

print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Adding a new key-value pair
my_dict['occupation'] = 'Student'
print("Dictionary after adding a new key-value pair:", my_dict)

# Updating a value
my_dict['age'] = 21
print("Dictionary after updating the age:", my_dict)

# Accessing values using get() method
print("Occupation:", my_dict.get('occupation'))

# Removing a key-value pair
removed_value = my_dict.pop('city')
print("Dictionary after removing 'city':", my_dict)
print("Removed value:", removed_value)

# Iterating over keys and values
print("Iterating over keys and values:")
for key, value in my_dict.items():
    print(key, ":", value)


# In[ ]:




