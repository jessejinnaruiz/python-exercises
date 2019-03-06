

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(n):
    if n == '2' or n == 2:
        return True
    else:
        return False

#more clever and pythonic code
def is_two(something):
        return something == 2 or something == '2'

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(n):
    if n.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

#more concise way:
def is_vowel(n):
        return n in 'aeiou'

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(c):
    if is_vowel(c)==False:
        return True
    else:
        return False

# more concise way:
def is_consonant(something):
        return not is_vowel(something)


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def caps_if_consonant(word):
    if is_consonant(word[0])==True:
        return word[0].upper() + word[1:]
    else:
            return word

        #also we can use .capitalize() in the return statement


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percentage, bill_total):
    print('Amount to tip is...')
    return percentage*bill_total

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    print("Amount after discount is applied...")
    return (original_price)-(original_price*discount_percentage)


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(n):
        return int(str(n).replace(',', ''))
    

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(n):
        if n >= 88:
                return('A')
        elif n >= 80:
                return('B')
        elif n >= 67:
                return('C')
        elif n >= 60:
                return('B')
        elif n >= 0:
                return('F')
    

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
        edited_word = []
        for char in word:
                if is_vowel(char)==False:
                        edited_word += char
                else:
                        continue
        return ''.join(edited_word)

#more pythonic method
def remove_vowels(word):
        return ''.join([letter for letter in word if not is_vowel(letter)])

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#     * anything that is not a valid python identifier should be removed
#     * leading and trailing whitespace should be removed
#     * everything should be lowercase
#     * spaces should be replaced with underscores
#     * for example:
#         * Name will become name
#         * First Name will become first_name
#         * % Completed will become completed

# def is_special_char(name):
#         edited_word = []
#         for char in name:
#                 if char.isalpha()==False or char.isdigit()==False or char.isspace()==True:
#                         edited_word += char
#                 else:
#                         continue
#         return ''.join(edited_word)

def normalize_name(name):
        edited_word = []
        for char in name:
                if char.isalpha()==True or char.isdigit()==True or char.isspace()==True:
                        edited_word += char
                else:
                        continue
        return ''.join(edited_word).strip().replace(' ','_').lower()

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#     * cumsum([1, 1, 1]) returns [1, 2, 3]
#     * cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(list_of_numbers):
        add_up = []
        sum_of_vars = []
        result=[]
        for elements in list_of_numbers:
                add_up.append(elements)
                sum_of_vars = sum(add_up)
                result.append(sum_of_vars)
        return result


# Bonus
# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#     * col_index('A') returns 1
#     * col_index('B') returns 2
#     * col_index('AA') returns 27
