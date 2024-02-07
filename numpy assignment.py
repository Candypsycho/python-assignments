#!/usr/bin/env python
# coding: utf-8

# q1: what is a python library? why do we use them?
# A Python library is a collection of pre-written code that can be used to perform common tasks, such as working with data, manipulating images, connecting to web servers, or downloading videos. Libraries save time and effort by allowing programmers to use existing code instead of writing everything from scratch.
# Here are some reasons why we use Python libraries:
# Code reuse: Python libraries provide reusable code that can be used in multiple projects. This saves time and effort in writing and testing code.
# Increased productivity: Libraries provide ready-to-use functions and methods that can be directly used in programs, increasing productivity.
# Standardization: Libraries ensure that certain tasks are performed in a standard way, which helps maintain consistency across different projects.
# Easier collaboration: By using common libraries, developers can easily understand and contribute to each other's code, facilitating teamwork.
# Access to complex functionality: Libraries often provide access to complex functionality that would be difficult or time-consuming to implement from scratch, such as machine learning algorithms or web scraping tools.
# 
# 

# In[1]:


# 3. Find the shape, size and dimension of the following array?
import numpy as np 
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
print(arr.ndim)
print(arr.shape)
print(arr.size)


# 2. What is the difference between Numpy array and List?
# NumPy arrays are faster and more memory-efficient for numerical operations, with a homogeneous data type requirement, while Python lists offer flexibility for mixed data types and general-purpose use.

# In[2]:


# 4. Write python code to access the first row of the following array?
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
print(arr[0])


# In[3]:


# 5. How do you access the element at the third row and fourth column from the given numpy array?
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
print(arr[2,3])


# In[12]:


# 6. Write code to extract all odd indexed elements from the given numpy array?
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
print(arr[arr % 2 != 0])


# In[5]:


# 7. How can you generate a random 3x3 matrix with values between 0 and 1?
arr1 = np.random.rand(3,3)
print(arr1)


# 8. Describe the difference between np.random.rand and np.random.randn?
# the key differences between these two are:
# np.random.rand() generates random numbers from a uniform distribution between 0 (inclusive) and 1 (exclusive).
# np.random.randn() generates random numbers from a normal (Gaussian) distribution with mean 0 and standard deviation 1.
# np.random.rand() returns a scalar or an array of random values, while np.random.randn() returns an array of random values with a specific shape and data type.

# In[6]:


#9. Write co^e to increase the ^imension of the following array?
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
np.expand_dims(arr,axis=1)


# In[7]:


# 10. How to transpose the following array in NumPy?
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
arr.T


# In[8]:


# 11
import numpy as np

# Define matrices A2 and B2
A2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Addition
addition_result = A2 + B2
print("Addition Result:")
print(addition_result)

# Subtraction
subtraction_result = A2 - B2
print("\nSubtraction Result:")
print(subtraction_result)

# Matrix Multiplication
matrix_multiplication_result = B2.T @ A2  # Transpose B2 to match dimensions
print("\nMatrix Multiplication Result:")
print(matrix_multiplication_result)

# Element-wise Division (Divide B by A)
element_wise_division_result = np.divide(B2, A2)
print("\nElement-wise Division Result (Divide B by A):")
print(element_wise_division_result)


# In[9]:


# 12. Which function in Numpy can be used to swap the byte order of an array?
"""In NumPy, you can use the byteswap() function to swap the byte order of an array. This function swaps the byte order of the elements in the array without changing the data type or the memory layout of the array."""
import numpy as np

# Create an example array
arr = np.array([1, 2, 3, 4], dtype=np.int32)
print("Original array:", arr)

# Swap the byte order of the array
arr_swapped = arr.byteswap()
print("Array with swapped byte order:", arr_swapped)



# # 13
# The np.linalg.inv function in NumPy computes the inverse of a square matrix. Its significance lies in solving linear systems of equations, computing determinants, performing singular value decomposition, enabling least squares solutions, and facilitating regularization techniques in fields like linear algebra, statistics, optimization, and machine learning. It's a fundamental tool for numerical computing, although computationally expensive for large or ill-conditioned matrices.
# 
# 
# 
# 
# 
# 

# In[10]:


# 14. What does the np.reshape function do, and how is it used?
"""The np.reshape() function is used to change the shape of an given array below is the example"""
import numpy as np 
arr = np.random.randint(1,10,(3,4))
print(f'before changing the shape {arr}')
arr1 =arr.reshape(6,2)
print(f'{arr1} after changing the shape of {arr} ')


# In[11]:


# 15. What is broa^casting in Numpy?
"""Broadcasting in NumPy is a mechanism where arrays with different shapes are automatically aligned and operated upon element-wise during arithmetic operations, enabling concise and readable code without explicit looping."""
import numpy as np

# Define a 3x3 array
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Define a 1D array
y = np.array([1, 2, 3])

# Add the 1D array to each row of the 2D array
result = x + y

print(result)


# In[ ]:




