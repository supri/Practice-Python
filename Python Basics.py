#!/usr/bin/env python
# coding: utf-8

# ### 1.Write a Python program to print the following string
# 
# Sample String: "Welcome to INSAID- International School of AI and Data Science"
# 
# 

# <img src='https://www.insaid.co/wp-content/uploads/2018/04/INSAID_Logo-1.png' height="240" width="360"/>
# <br/>
# # Python basics

# In[ ]:





# In[ ]:


print("Welcome to INSAID - International School of AI and Data Science")


# ### 1.1 In a “Hello, World!” program, a comment may look like this:

# In[ ]:


# Print “Hello, World!” to console


# In[ ]:


# Define sharks variable as a list of strings ('hammer', 'white', 'fish', 'frilled', 'bullhead', 'requiem')

list_sample=['hammer', 'white', 'fish', 'frilled', 'bullhead', 'requiem']

# For loop that iterates over sharks list and prints each string item
for sample in list_sample:
    print(sample)


# ### 2.Write a Python Program to Add Two Numbers

# In[ ]:


# initialise two varaibles


# Add two numbers


# Display the sum


# ### 3.Write a Python Program to Find the product of two numbers

# In[ ]:


# initialise two varaibles


# multiply two numbers


# Display the sum


# ### 4.Write a python program to find the area of triangle given height and base of the triangle as 3 and 10.

# In[ ]:


# Area of the triangle A= 1/2(base * height)

#given height=3 and base =10


# ### 5.Python Program to Swap Two Variables

# In[ ]:


# initialise two varaibles



# create a temporary variable and swap the values



# ## Section

# ### 1.Write a python program to print datatype of a varaible

# In[ ]:


a = 1


b = 2.0


c = 1+2j


# ### 2.Write a python program to extract an item or a range of items from a list.
# 
# 

# In[ ]:


a = [15,20,35,40,45,30,35,60]

# Print the item at index 2

# Print the first 3 items

# Print the last 3 items

# Start to third last item


# ### 3.Converting Floats to Integers
# 

# In[ ]:


b = 125.0
c = 390.8

# Print the Integer values


# ### 4.Converting Numbers to Strings

# In[ ]:


a = 10

print(a, "is of type", type(a))

# Convert the value in a to a string and then print


# ### 5.Converting Strings to Numbers

# In[ ]:


a = "50"
b = "108"

# Find the difference between a and b


# ### 6.Converting list to Tuples

# In[ ]:


myList = ['request', 'source', 'repository', 'branch']

# Print myList to a Tuple


# ### 7.Converting tuple to Lists

# In[ ]:


myTuple = ('blue', 'red', 'white')

# Print myTuple to a List


# ### 8.converting strings to lists:

# In[ ]:


myString = 'INSAID'

# Convert myString to List


# ### 9.Assign different data types to a varibles

# In[ ]:


# Try string, float, boolean, list, tuple, dictionary


# ## Section

# ### Print out a string that uses a formatter

# In[ ]:


# Print "john has 5 cars." using formatter


# ### We can also assign a variable to be equal to the value of a string that has formatter placeholders:

# In[ ]:


open_string = "john likes {}."

# Use format method to print the following output "john likes open source."


# ### Using Formatters with Multiple Placeholders

# In[ ]:


new_open_string = "john likes {} {}."                      #2 {} placeholders
# Pass 2 strings into format method, separated by a comma to get output "john likes open-source software."


# In[ ]:


sammy_string = "john loves {} {}, and has {} {}."                      #4 {} placeholders
# Pass 4 strings into method to get output "john loves open-source software, and has 5 balloons."


# ### Reordering Formatters with Positional and Keyword Arguments
# 

# In[ ]:


# Reference sample
print("john the {} has a pet {}!".format("shark", "pilot fish"))


# ### We can pass these index numbers into the curly braces that serve as the placeholders in the original string:

# In[ ]:


# Reference Sample
print("john the {0} has a pet {1}!".format("shark", "pilot fish"))

print("john is a {}, {}, and {} {}!".format("happy", "smiling", "blue", "shark"))


# ### Python Program to Get String Input from User
# 

# In[ ]:


#Enter any string and print it


# ### Python program for conditional statements
# 
# ### 1)If the student receives over 65% on her test, report that her grade passes; if not, report that her grade fails

# In[ ]:


grade = 70


# In[ ]:


# Use only if
grade = 60


# ### Write a python program calculate whether a bank account balance is below 0 and print appropriate message.

# In[ ]:


# Use if else
balance = 522


# ### Using Else if statement

# In[ ]:


balance = 522


# ### Python program to print  Fibonacci series between 0 to 50.

# In[ ]:





# ### Python program to find numbers which are divisible by 7 and multiple of 5 between a range 150 to 270

# In[ ]:





# ### Python program to Sum all the items in a list

# In[ ]:


def sum_list(items):
    # Your code here
    return # Your variable
print(sum_list([20,12,20,22]))


# ### Python program to Remove duplicates from a list.

# In[ ]:


a = [10,20,30,40,50,60,70,40,80,50,40]


# ### Python program to Get the largest number from a list.

# In[ ]:


def max_num_in_list( list ):
    # Your code
    return # Maximum value
print(max_num_in_list([1, 12, 28, 0]))


# ### Concatenation of Tuples.

# In[ ]:


# Code for concatenating 2 tuples
 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'code')
 
# Concatenating above two
print('''Your code here''')


# ### Nesting of Tuples.

# In[ ]:


# Code for creating nested tuples
 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'code')
tuple3  # Your code goes here
print(tuple3)


# ### Write a Python program to add an item in a tuple.

# In[ ]:


# Create a tuple & print


#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple

# Adding items in a specific index


# ### Write a Python program to remove an item from a tuple.

# In[ ]:


# Create a tuple and print it

# Find a way to remove an item of the tuple (Hint: Use other data types)


# ### Python Program to Check if a given key already exists in a dictionary.

# In[ ]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  # Your code goes here
  return # Your observation
is_key_present(5)
is_key_present(9)


# ### Write a Python script to merge two Python dictionaries.

# In[ ]:


d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

# Your code


# ### Write a Python function to find the Max of three numbers.

# In[ ]:


def max_of_two( x, y ):
    # Your code here
    return # Your answer
def max_of_three( x, y, z ):
    # Your code here use max_of_two
    return # Your answer
print(max_of_three(13, 26, -5))


# ### Write a Python program to reverse a string.

# In[ ]:


def string_reverse(str1):
    # Your code goes here
    return # Your answer
print(string_reverse('INSAID'))


# ### Write a Python function to calculate the factorial of a number 

# In[ ]:


def factorial(n):
    # Your code here
    return # The answer
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# ### Write a Python function to sum all the numbers in a list.

# In[ ]:


def sum(numbers):
    # Your code goes here
    return # Your Answer
print(sum((8, 2, 3, 0, 7)))


# ### Write a Python function to check whether a number is in a given range.

# In[ ]:


def test_range(n):
    # Your code
    return # Your answer 
test_range(5)


# ### Find the value of pi using math module.

# In[ ]:


# import statement example
# to import standard module math

import math


# ### Write a Python program to read an entire text file.
# 
# ### Content of text.txt.
# 
# ### What is Python language?      
# 
# #### Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.

# In[ ]:


def file_read(fname):
    # Your code goes in here
    return

file_read('test.txt')


# ### Write a Python program to read a file line by line and store it into a list.

# In[ ]:


def file_read(fname):
        # Your code goes in here
        return

file_read('test.txt')


# ### Write a Python program to calculate the discriminant value. (b <sup>2</sup> - 4ac)

# In[9]:


def discriminant():
    a_value = float(input('The a value: '))
    b_value = float(input('The b value: '))
    c_value = float(input('The c value: '))
    
    # Calculate the discriminant here
    
    return # The value


discriminant()


# In[10]:


print('Hello World')


# In[ ]:


print('What am I typing are you able to see?')

