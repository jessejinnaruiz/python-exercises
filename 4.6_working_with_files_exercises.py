# Read the contents of your last exercise file into a variable.

# with open('4.5_import_exercises.py') as f:
#     file_contents = f.read()
# print(file_contents)

# Print out every line in the file

# Print out every line in the file, but add line numbers
# with open('4.5_import_exercises.py') as f:
#     file_contents = f.readlines()

# n=1
# for line in range(0,len(file_contents)-1):
#     print('line number is ', n, file_contents[n])
#     n += 1

# Write some python code to create a grocery list. -------------------------------------

# Create a variable named grocery_list. 
# It should be a list, and the elements in the list should be a least 3 things that you need to buy from the grocery store.
grocery_list = ['zucchini', 'celery', 'avocados']

# Create a function named make_grocery_list. 
# When run, this function should write the contents of the grocery_list variable to a file named my_grocery_list.txt.

def make_grocery_list():
    with open('my_grocery_list.txt', 'w') as f:
        for elements in grocery_list:
                f.write("%s \n" %elements)
make_grocery_list()

# Create a function named show_grocery_list. When run, it should show each item on the grocery list.
def show_grocery_list():
        with open('my_grocery_list.txt') as f:
                lines = f.read()
                print(lines)
                # for line in f.readlines():     
                #         print(line)

show_grocery_list()
print('--------------')
# Create a function named buy_item. It should accept the name of an item on the grocery 
# list, and remove that item from the list.

buy_item_list_formatted = []
buy_items = []

def buy_item(item):
        with open('my_grocery_list.txt') as f:
                lines = f.readlines()
                # print(lines)
                for element in lines:
                        buy_item_list_formatted.append(element.rstrip())
                for element in buy_item_list_formatted:
                        if element == item:
                                continue
                        else:
                                buy_items.append(element)
                print(buy_items)
                # print(lines)
                # for line 
                # f.write(buy_item_list_formatted)

print('testing buy_item function ---------')
buy_item('celery')

# print(buy_items)