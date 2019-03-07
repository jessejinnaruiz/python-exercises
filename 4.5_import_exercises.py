# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
#     * import the module and refer to the function with the . syntax
#     * use from to import the function directly
#     * use from and give the function a different name

# import function_exercises
# function_exercises.is_two(2)

# from function_exercises import is_two
# is_two(2)

# from function_exercises import is_two as is2
# is2(2)


# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.

# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# from itertools import permutations

# result_list = []
# numerical_list = [] 

# for i in permutations('123abc'):
#     numerical_list.append(i)

# print(len(numerical_list)) #720

# 2. How many different ways can you combine two of the letters from "abcd"?

# from itertools import permutations

# result_list = []
# numerical_list = [] 

# for i in permutations('abcd'):
#     numerical_list.append(i)

# print(len(numerical_list)) #24

# Save this file as profiles.json. Use the load function from the json module to open this file, it will produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:

import json

with open('profiles.json', 'r') as content: 
    data = json.load(content)
# print(data)

# * Total number of users
# for element in data:
#     print(len(element))

total_number_users =  len(data)

print(total_number_users)
#19

# * Number of active users
active_users = []
for element in data:
    if element['isActive'] == True:
        active_users.append(element)
    else:
        continue

print(len(active_users))
# 9 active

# * Number of inactive users
inactive_users  = []
for element in data:
    if element['isActive'] == False:
        inactive_users.append(element)
    else:
        continue
print(len(inactive_users))

# 10 inactive

# * Grand total of balances for all users

balances = []

for element in data:
    balances.append(element['balance'][1:])

print(balances)
print(type(balances[0]))


formatted_balances = []

for element in balances:
    formatted_balances.append(element.strip().replace(',',''))
print(formatted_balances)

print('the class type for formatted_balances is: ', type(formatted_balances[0]))

formatted_balances_2 = []

for element in formatted_balances:
    formatted_balances_2.append(float(element))

print('THIS IS THE BALANCES FORMATTED CORRECTLY: ')
print(formatted_balances_2)

print(type(formatted_balances_2[0]))

balances_grand_total = sum(formatted_balances_2)

print('The grand total is: %s ' % balances_grand_total)
# 52667.02


# * Average balance per user

avg_bal_per_user = balances_grand_total / total_number_users

print("The average balance per user is: %s" % (round(avg_bal_per_user, 2)))


# * User with the lowest balance

print("The lowest balance is: %s" % (min(formatted_balances_2))) #1214.1
user_lowest_bal = []

for element in data:
    # print(element)
    for things in element:
        if'$1,214.10' in element.values():
            # print('True')
            user_lowest_bal.append(element['name'])

print("The user with the lowest balance is {}! Yay!".format(user_lowest_bal[0]))


# * User with the highest balance
print("The highest balance is: ", (max(formatted_balances_2))) # 3919.64
user_highest_bal = []

for element in data:
    # print(element)
    for things in element:
        if'$3,919.64' in element.values():
            # print('True')
            user_highest_bal.append(element['name'])

print("The user with the highest balance is {}! Boo!".format(user_highest_bal[0]))

# * Most common favorite fruit
fav_fruits = []

for elements in data:
    fav_fruits.append(elements['favoriteFruit'])
print(fav_fruits)


# count_of_favorited_strawberry = fav_fruits.count('strawberry')
# print(count_of_favorited_strawberry)
# count_of_favorited_apple = fav_fruits.count('apple')
# print(count_of_favorited_apple)
# count_of_favorited_banana = fav_fruits.count('banana')
# print(count_of_favorited_banana)

# numb_strawberry_fans = 0
# numb_apple_fans = 0
# numb_banana_fans = 0

# for element in fav_fruits:
#     if element == 'strawberry':
#         numb_strawberry_fans += 1
#         # print('There are {} fans of strawberry!'.format(fav_fruits.count('strawberry')))
#     elif element == 'apple':
#         numb_apple_fans += 1
#         # print('There are {} fans of apple!'.format(fav_fruits.count('apple')))
#     elif element == 'banana':
#         numb_banana_fans += 1
#         # print('There are {} fans of banana!'.format(fav_fruits.count('banana')))

# print(numb_apple_fans, numb_strawberry_fans, numb_banana_fans)
print("There are {} fans of strawberry!".format(fav_fruits.count('strawberry')))
print("There are {} fans of apple!".format(fav_fruits.count('apple')))
print("There are {} fans of banana!".format(fav_fruits.count('banana')))
# Answer: strawberry

# for element in fav_fruits:
#     count_of_favorited_fruits.append(fav_fruits.count(element))
#     print(element, 'has %s fans.' % fav_fruits.count(element))


# * Least most common favorite fruit
# Answer: apple

# * Total number of unread messages for all users ---------------------------------------------------
unread_msgs = []
the_greetings = []
names = []
names_formatted = []

# captures the strings 'greetings' in a list
for element in data:
    the_greetings.append(element['greeting'])
# print(the_greetings)

# captures the names in the greetings
for element in the_greetings:
    names.append(element[6:-29])
# print(names)

# formats these names
for element in names:
    names_formatted.append(element.strip('!').strip())
# print('---------')
print(names_formatted)

# for element in the_greetings:
#     for char in element:
#         if char.isdigit():
#             unread_msgs.append(char)
# print(unread_msgs)

# captures the number of unread messages
for element in the_greetings:
    unread_msgs.append(element[-19:-17])
print(unread_msgs)

# formats the unread messages 
unread_msgs_formatted = []
for element in unread_msgs:
    unread_msgs_formatted.append(element.strip())
print(unread_msgs_formatted)

print('-----------------------')

total_unread_messages = []
for element in unread_msgs_formatted:
    total_unread_messages.append(int(element))
# print(total_unread_messages)
print('The total number of unread messages is: %s ' %sum(total_unread_messages))

# list_to_create_dict = []

# for i in range(19):
#     list_to_create_dict.append(names_formatted[i])
#     list_to_create_dict.append(unread_msgs_formatted[i])
#     # names_and_msg_dict = dict(list_to_create_dict)

# print((list_to_create_dict))

# names_and_msg_dict = {list_to_create_dict[i]: list_to_create_dict[i+1] for i in range(0, len(list_to_create_dict), 2)}
# print(names_and_msg_dict)

# print(type(names_and_msg_dict))