import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
# count = []
# for element in a:
#     if element < 0:
#         count.append(element)
# print(len(count))

negative_numbers = a < 0
# print(negative_numbers)
print('There are ',(negative_numbers.sum()), 'negative numbers.')


# 2. How many positive numbers are there?
positive_numbers = a > 0
print(positive_numbers)
print('There are ',(positive_numbers.sum()), 'positive numbers.')


# 3. How many even positive numbers are there?
even_positive_numbers = []
# for element in a:
#     if element > 0 and element %2 ==0:
#         even_positive_numbers.append(element)
# print("Even positive numbers: ", len(even_positive_numbers))


# positive_numbers = a >= 0
# print(positive_numbers)

for element in a:
    if element % 2 == 0:
        even_positive_numbers.append(element)

b = np.array(even_positive_numbers)
# print(b)
# print(b>0)
print('There are ', sum(b>0), 'even positive numbers.')



#alternative solution to even positive numbers:
evens = a[a % 2 == 0]
positive_even = evens[evens > 0]
print('    {} positive even numbers'.format(positive_even.shape[0]))


# 4. If you were to add 3 to each data point, how many positive numbers would there be?
added_three_and_positive = a +3 > 0
print(added_three_and_positive)
print('There are ',sum(added_three_and_positive), 'positive numbers after adding 3 to each data point in a.')




# 5. If you squared each number, what would the new mean and standard deviation be?
a_squared = a*a
print(a_squared)
print('The mean of a_squared is', a_squared.mean())
print('The standard deviation of a_squared is', a_squared.std())


# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. Center the data set.

a_centered = a - (a.mean())
print('This is the centered list, a: ')
print(a_centered)


# 7. Calculate the z-score for each data point. Recall that the z-score is given by: Z=x−μ/σ

z_score_a = (a - a.mean())/a.std()
print('This is the z score of a: ')
print(z_score_a)

# 8. Copy the setup and exercise directions from More Numpy Practice into your 4.7_numpy_exercises.py and add your solutions.
 # print('----------------START----------------MORE---------------NUMPY---------------PRACTICE---------------')
import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a)/len(a)
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
total = 1
for element in a:
    total *= element
print(total)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []

for element in a:
    squares_of_a.append(element**2)

print(squares_of_a)

#alternatively:

squares_of_a = [n ** 2 for n in a]


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for element in a:
    if element % 2 == 0:
        continue
    else:
        odds_in_a.append(element)
print(odds_in_a)

#alternatively:
print(n for n in a if n % 2 == 1)



# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for element in a:
    if element % 2 == 0:
        evens_in_a.append(element)
    else:
        continue
print(evens_in_a)

#alternatively:
# print(n for n in a if n % 2 == 0)

print('------------------------------------------------------------------------------------------------------------------------------------------')
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)
print('exercise 1: ')
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(sum_of_b)

sum_of_b_sublists = []
for element in b:
    sum_of_b_sublists.append(sum(element))
# print((sum_of_b_sublists))
sum_of_b = sum(sum_of_b_sublists)
print('The sum of b is: ',sum_of_b)

print(b.sum())

print('exercise 2: ')
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print(min_of_b)
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)
# print(type(b))
# print(b.shape)
print('The min of b is: ',b.min())


print('exercise 3: ')
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(max_of_b)
print('The max of b is: ', b.max())

print('exercise 4: ')
# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(mean_of_b)
b = np.array(b)
print('The mean of b is: ',b.mean())





print('exercise 5: ')
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print(product_of_b)
print('The product of all numbers in b is: ',b.prod())

print('exercise 6: ')
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
print(squares_of_b)

print('The list of sqaures is: ',np.multiply(b,b))

#alternatively:
# b ** 2

print('exercise 7: ')
# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
# print(odds_in_b)
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)

odds = np.array([])
for x in np.nditer(b):
    # print(x)
    if x % 2 != 0:
        # odds.append(x)
        odds = np.append(odds, x)
print('The odds in b is: ',odds)

# alternatively
# odds_in_b = b[(b %2==1)]
# print(odds_in_b)

print('exercise 8: ')
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)



b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)

evens = np.array([])
for x in np.nditer(b):
    # print(x)
    if x % 2 == 0:
        # evens.append(x)
        evens = np.append(evens, x)
print('The evens in b is: ',evens)

# alternatively
# evens_in_b = b[(b %2==0)]
# print(evens_in_b)

print('exercise 9: ')
# Exercise 9 - print out the shape of the array b.
print(b.shape)

print('exercise 10: ')
# Exercise 10 - transpose the array b.
print('This is b transposed: \n',np.transpose(b))
#alternatively:
#b.T

print('exercise 11: ')
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b = b.reshape(1,6)
print('This is b reshaped to a 1 x 6: \n', b)

print('exercise 12: ')
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b = b.reshape(6, 1)
print('This is b reshaped to a 6 x 1: \n', b)


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)

# print('exercise: ')HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
print('exercise 1: ')
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)
print('This is the min of c: ',c.min())
print('This is the max of c: ',c.max())
print('This is the sum of c: ',c.sum())
print('This is the product of c: ',c.prod())


# Exercise 2 - Determine the standard deviation of c.
print('exercise 2: ')
print('This is the standard deviation of c: ',c.std())

# Exercise 3 - Determine the variance of c.
print('exercise 3: ')
print('This is the variance of c: ',c.var())
#alternatively
#c.std() ** 2

# Exercise 4 - Print out the shape of the array c
print('exercise 4: ')
print('This is the shape of c: ',c.shape)


# Exercise 5 - Transpose c and print out transposed result.
print('exercise 5: ')
print('This is the transpose of c: \n',np.transpose(c))

# Exercise 6 - Multiply c by the c-Transposed and print the result.
print('exercise 6: ')
print('This is Multiply c by the c-Transposed: ',np.transpose(c)*c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print('exercise 7: ')
c_transposed_times_c = np.transpose(c)*c
print('This is the sum of multiply c by the c-Transposed: \n',(c_transposed_times_c).sum())


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print('exercise 7: ')
c_transposed_times_c = np.transpose(c)*c
print('This is product of multiply c by the c-Transposed: ', np.product(c_transposed_times_c))

## Setup 4 ----------------------------------------------------------------------------------

import math

d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)

print('exercise 1: ')
# Exercise 1 - Find the sine of all the numbers in d
sin_of_x = []
for x in np.nditer(d):
        x = math.sin(x)
        sin_of_x = np.append(sin_of_x, x)
print('This is the sine of every number in d: ',sin_of_x)

#np.sin(d)

print('exercise 2: ')
# Exercise 2 - Find the cosine of all the numbers in d
cos_of_x = []
for x in np.nditer(d):
        x = math.cos(x)
        cos_of_x = np.append(cos_of_x, x)
print('This is the cosine of every number in d: ',cos_of_x)

#np.cos(d)

print('exercise 3: ')
# Exercise 3 - Find the tangent of all the numbers in d
tan_of_x = []
for x in np.nditer(d):
        x = math.tan(x)
        tan_of_x = np.append(tan_of_x, x)
print('This is the tangent of every number in d: ',tan_of_x)

#np.tan(d)

print('exercise 4: ')
# Exercise 4 - Find all the negative numbers in d
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)

negative_numbers = np.array([])
for x in np.nditer(d):
    # print(x)
    if x < 0:
        negative_numbers = np.append(negative_numbers, x)
print('The negative_numbers in b are: ',negative_numbers)

#d[d < 0]

print('exercise 5: ')
# Exercise 5 - Find all the positive numbers in d
positive_numbers = np.array([])
for x in np.nditer(d):
    # print(x)
    if x > 0:
        positive_numbers = np.append(positive_numbers, x)
print('The positive_numbers in b are: ',positive_numbers)
#d[d>0]


print('exercise 6: ')
# Exercise 6 - Return an array of only the unique numbers in d.
print('These are the unique numbers in d: \n',np.unique(d))


print('exercise 7: ')
# Exercise 7 - Determine how many unique numbers there are in d.
unique_numbers_in_d = np.unique(d)
print('There are ',unique_numbers_in_d.size ,'unique numbers in d.')



print('exercise 8: ')
# Exercise 8 - Print out the shape of d.
print('The shape of d is: ',d.shape)


print('exercise 9: ')
# Exercise 9 - Transpose and then print out the shape of d.
print('This is d transposed: ', np.transpose(d))

print('exercise 10: ')
# Exercise 10 - Reshape d into an array of 9 x 2
print('This is d reshaped into a 9x2: \n', d.reshape(9,2))
