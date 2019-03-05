# 1. Conditional Basics
#     - prompt the user for a day of the week, print out whether the day is Monday or not

day = input("What day? ")
print(f'day={day}')
if day == 'Monday':
    print('It\'s Monday')
else:
    print('It\'s not Monday')

#     - prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day = input("What day? ")
# MY ANSWER
if day == 'Saturday' or 'Sunday':
    print('It\'s a weekend.')

else:
    print('It\'s a weekday.')


# Create variables and make up values for
#         - the number of hours worked in one week
#         - the hourly rate
#         - how much the week's paycheck will be
# Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked_weekly = 43
hourly_week_payrate = 90

if hours_worked_weekly > 40:
    paycheck = 40 * hourly_week_payrate + (hours_worked_weekly -40) * hourly_week_payrate*1.5
else:
    paycheck = hourly_week_payrate*hours_worked_weekly

print(paycheck)

# 2. Loop Basics
#     a. While
#         - Create an integer variable i with a value of 5.
#         - Create a while loop that runs so long as i is less than or equal to 15
#         - Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <101:
    print(i)
    i=i+2
    '/n'

# - Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i > -11:
    print(i)
    i=i-5
    '/n'

 # - Create a while loop that starts at 2, and displays the number squared on 
 # each line while the number is less than 1,000,000. Output should equal:
 # 2
# -  4
# -  16
# -  256
# -  65536

i = 2
while i < 1000000:
    print(i)
    i=i**2
    '/n'

# - Write a loop that uses print to create the output shown below.
i = 100
while i >0:
    print(i)
    i = i -5
    '/n'

# b. For Loops
#     - Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number. For example, if the user enters 7, your program should output: 

number = input('Please give me a number: ') 
for n in range (1, 11): 
    print(f'{number} x {n} = ',n*int(number)) 
# - Your output should look like this:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# Create a for loop that uses print to create the output shown below.
i = 1 
for n in range(1,10): 
    print(n*str(n)) 
# - Your output should look like this:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


# c. break and continue

# -Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user 
# if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.
'''WORKS BUT I DID NOT USE A BREAK STATEMENT IN THE WHILE STATEMENT
'''

# step 1 keep asking the user for a number checking for valid input
number = input('Number to skip is: ')

while not number.isdigit() or int(number) <1 or int(number) > 50 or int(number)%2==0:
    number = input('Number to skip is: ')

# step 2 print the number sequence according to input
number = int(number)
for n in range (1,51): 
    if n==int(number): 
        print('Yikes! Skipping number: ',number) 
        continue
    
    elif not n%2 == 0: 
        print('Here is an odd number: ', n) 



# Second method for step 1 using a break statement
# while True:
#     number = input('Enter an odd number between 0-50: ')
#     if number.isdigit() and 1 <= int(number) <= 50 and int(number) % 2 == 1:
#         break
# number = int(number)
# for n in range (1,51): 
#     if n==int(number): 
#         print('Yikes! Skipping number: ',number) 
#         continue
    
#     elif not n%2 == 0: 
#         print('Here is an odd number: ', n) 


# d. The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
number = (input('Please input a positive number: '))

if int(number) > 0:
    for n in range(0, int(number)+1):
        print(n)

elif int(number) < 0:
    print(f"{number} is not a valid number!")

else: 
    print(f"{number} is not a number!")


# e. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
number = (input('Please input a positive number: '))
user_input = input('Please enter a positive number: ')

while not user_input.isdigit():
    user_input = input('Hey! Give me a positive number! ')

if int(user_input) > 0:
    for n in range(int(user_input), 0, -1):
        print(n)

elif int(user_input) < 0:
    print(f"{user} is not a valid number!")



# 3. Fizzbuzz- One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
#     * Write a program that prints the numbers from 1 to 100.
#     * For multiples of three print "Fizz" instead of the number
#     * For the multiples of five print "Buzz".
#     * For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101): 
    if i%3 ==0 and i%5 ==0: 
        print('FizzBuzz') 
    elif i%5 == 0: 
        print('Buzz') 
    elif i%3 ==0: 
        print('Fizz') 
    else: 
        print(i) 


# Method #2

for n in range(1,101):
    output = ''
    if n%3 == 0:
        output += 'Fizz'
    if n%5 == 0:
        output += 'Buzz'
    if output == '':
        print(n)
    else:
        print(output)

    # we could also write this for the last two lines:
    # print(n i output == '' else output)

# 4. Display a table of powers.
#     * Prompt the user to enter an integer.
#     * Display a table of squares and cubes from 1 to the value entered.
#     * Ask if the user wants to continue.
#     * Assume that the user will enter valid data.
#     * Only continue if the user agrees to.

# users_integer = (input('What number would you like to go up to? '))

# for n in range(1, int(users_integer)+1): 
#     print(n**2, n**3)
#     continue
#     while input('Do you want to continue? Yes/No ')=='Yes':
#         users_integer = (input('What number would you like to go up to? '))


# users_integer = (input('What number would you like to go up to? ')) 
# print('Here is your table! \n  number  squared  cubed   \n', (('-'*6)+' ' * 3))
# for n in range(1, int(users_integer)+1):  
#     print(f'{n}', '   |   ', n**2, '   |   ', n**3) 
#     continue 
#     if input('Do you want to continue? Yes/No ')=='Yes': 
#         break 

users_integer = (input('What number would you like to go up to? ')) 
print('\nHere is your table!\n\nnumber squared cubed \n -----  -----  -----')
for n in range(1, int(users_integer)+1):  
    print('{0:<5d} | {1:<5d} | {2:<5d}'.format(n, n**2, n**3))
    continue

while input('Do you want to continue? Yes/No? \n')=='Yes': 
    users_integer = (input('What number would you like to go up to? ')) 
    print('\nHere is your table!\n\nnumber squared cubed \n -----  -----  -----')
    for n in range(1, int(users_integer)+1):  
        print('{0:<5d} | {1:<5d} | {2:<5d}'.format(n, n**2, n**3))
        continue


#5. Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

user_grade = input('Please enter a grade from 0 to 100: ')
if int(user_grade) >= 88:
    print('A')
if 80 <= int(user_grade) <= 87:
    print('B')
if 67 <= int(user_grade) <= 79:
    print('C')
if 60 <= int(user_grade) <= 66:
    print('D')
if int(user_grade) <=59:
    print('F')


while input('Do you wish to continue? Yes/No? ') == 'Yes':
    user_grade = input('Please enter a grade from 0 to 100: ')
    if int(user_grade) >= 88:
        print('A')
    if 80 <= int(user_grade) <= 87:
        print('B')
    if 67 <= int(user_grade) <= 79:
        print('C')
    if 60 <= int(user_grade) <= 66:
        print('D')
    if int(user_grade) <=59:
        print('F')



# more concise method, part a:
# grade = int(input('Please enter a grade from 0 to 100: '))
# if grade >= 88:
#     print('A')
# elif grade >= 80:
#     print('B')
# elif grade >= 67:
#     print('C')
# elif grade >= 60:
#     print('B')
# elif grade >= 0:
#     print('F')

#part b
user_wants_to_continue = 'yes'
while user_wants_to_continue == 'yes':
    grade = int(input('Please enter a grade from 0 to 100: '))
    if grade >= 88:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 67:
        print('C')
    elif grade >= 60:
        print('B')
    elif grade >= 0:
        print('F')
    user_wants_to_continue = input('Do you want to continue? ')

# 5. Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).


user_grade = input('Please enter a grade from 0 to 100: ')
if 99 <= int(user_grade) < 100:
    print('A+')
if 92<= int(user_grade) < 99:
    print('A')
if 90<= int(user_grade) < 92:
    print('A-')
if 88<= int(user_grade) < 90:
    print('B+')
if 82 <= int(user_grade) < 88:
    print('B')
if 80 <= int(user_grade) < 82:
    print('B-')
if 78 <= int(user_grade) < 80:
    print('C+')
if 72 <= int(user_grade) < 78:
    print('C')
if 70 <= int(user_grade) < 72:
    print('C-')
if 68 <= int(user_grade) < 70:
    print('D+')
if 62 <= int(user_grade) < 68:
    print('D')
if 60 <= int(user_grade) < 62:
    print('D-')
if int(user_grade) < 60:
    print('F')

while input('Do you wish to continue? Yes/No? ') == 'Yes':
    user_grade = input('Please enter a grade from 0 to 100: ')
    if 99 <= int(user_grade) < 100:
        print('A+')
    if 92<= int(user_grade) < 99:
        print('A')
    if 90<= int(user_grade) < 92:
        print('A-')
    if 88<= int(user_grade) < 90:
        print('B+')
    if 82 <= int(user_grade) < 88:
        print('B')
    if 80 <= int(user_grade) < 82:
        print('B-')
    if 78 <= int(user_grade) < 80:
        print('C+')
    if 72 <= int(user_grade) < 78:
        print('C')
    if 70 <= int(user_grade) < 72:
        print('C-')
    if 68 <= int(user_grade) < 70:
        print('D+')
    if 62 <= int(user_grade) < 68:
        print('D')
    if 60 <= int(user_grade) < 62:
        print('D-')
    if int(user_grade) < 60:
        print('F')





# 6. Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
books = [
    {'Title': "Bulletproof  Diet", 'Author': "Dave Asprey", 'Genre': "Health"},

    {'Title': "Reproductive Justice", 'Author': "Someone", 'Genre': "Nonfiction"},

    {'Title': "Bambi", 'Author': "Mickey Mouse", 'Genre': "Fiction"},
]

for book in books:
    print(' ---------------------------- ')
    print(' - title: %s' %book['Title'])
    print(' - author: %s' %book['Author'])
    print(' - genre: %s' %book['Genre'])


# 6a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

user_genre = input("Please enter a book genre: ")
for book in books:
    if book['Genre'] != user_genre:
        continue
    print(' ---------------------------- ')
    print(' - title: %s' %book['Title'])
    print(' - author: %s' %book['Author'])
    print(' - genre: %s' %book['Genre'])


# second problem with a list in genres:
books = [
    {'Title': "Bulletproof  Diet", 'Author': "Dave Asprey", 'Genre': ["Health", "Nonfiction"]},

    {'Title': "Reproductive Justice", 'Author': "Someone", 'Genre': ["Nonfiction", "Women's Rights"]},

    {'Title': "Bambi", 'Author': "Mickey Mouse", 'Genre': "Fiction"},
]
user_genre = input("Please enter a book genre: ")
for book in books:
    if user_genre not in book['Genre']:
        continue
    print(' ---------------------------- ')
    print(' - title: %s' %book['Title'])
    print(' - author: %s' %book['Author'])
    print(' - genre: %s' %book['Genre'])
