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

# -Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# - Your output should look like this:



# d. The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
# number = (input('Please input a positive number: '))

# if int(number) > 0:
#     for n in range(0, int(number)+1):
#         print(n)

# elif int(number) < 0:
#     print(f"{number} is not a valid number!")

# else: 
#     print(f"{number} is not a number!")


# e. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
# number = (input('Please input a positive number: '))
# user_input = input('Please enter a positive number: ')

# while not user_input.isdigit():
#     user_input = input('Hey! Give me a positive number! ')

# if int(user_input) > 0:
#     for n in range(int(user_input), 0, -1):
#         print(n)

# elif int(user_input) < 0:
#     print(f"{user} is not a valid number!")



















# 3. Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
books = [{'Title': "Bulletproof  Diet", 'Author': "Dave Asprey", 'Genre': "Health"},
{'Title': "Reproductive Justice", 'Author': "Someone", 'Genre': "Nonfiction"},
{'Title': "Bambi", 'Author': "Mickey Mouse", 'Genre': "Fiction"},
]

for features in books:
    print(['Data'], 'Author', 'Genre')


# 4. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

