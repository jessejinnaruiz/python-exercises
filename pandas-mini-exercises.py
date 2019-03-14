import numpy as np
import pandas as pd

# 1. Use the code below to generate a data frame for student. Your data frame should include the student number, student name, shoe_size, and favorite number. Store your data frame in a variable named students

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))

students_df = pd.DataFrame({'name':students,
                    'student_number':student_number,
                    'shoe_size':shoe_sizes,
                    'side_of_classroom':side_of_classroom,
                    'fav_number':favorite_number})

print(students_df)

# 2. Print out the shape of the data frame.
print(f'The shape of the dataframe is: students_df.shape == {students_df.shape}')


# 3. Print out the names of the columns in the data frame.
print('The columns in our data frame are: {}'.format(', '.join(students_df.columns)))


# 4. Rename 2 of the columns in your data frame.
students_df.rename(columns={'student_number': 'Student Number', 'name':'Student Name'})


# 5. Create a new data frame based on the one you have. 
# The new data frame should only have columns for shoe size and side of the classroom.
students_df[['shoe_size','side_of_classroom']]


# 6. Create a new data frame that has all of the columns, but only 5 rows.
students_df.iloc[0:5]

# 7. Create a new data frame that has only columns for favorite number and name, and only includes 7 rows.
students_df[['fav_number','name']].iloc[0:7]


# 8. Create a new column for the ratio of shoe size to the favorite number. Name this ss_to_fn

# def find_ratio(shoe, number):
#     for element in find_ratio:
#         return shoe/number

# ss_to_fn = students_df.apply(find_ratio)

students_df['ss_to_fn']=students_df['shoe_size']/students_df['fav_number']
students_df

# 9. Create a new column that contains the z-score for the shoe size.
# from scipy.stats import zscore
# students_df['z_score_shoe_size']=scipy.stats.zscore(students_df['shoe_size'])
# students_df


# 10. Transform the side_of_the_classroom columns such that the values are either R or L.

def abbreviate(word):
    if word == 'left':
        return 'L'
    else:
        return 'R'

abbrev_side_room = students_df.side_of_classroom.apply(abbreviate)
students_df.assign(side_of_classroom=abbrev_side_room)


# 11. Find the names of all the students that have a shoe size greater than the 3rd quartile of shoe sizes 
#(You can use the .quantile method on a series for this)


students_df.shoe_size.quantile(0.75)
students_df.shoe_size > students_df.shoe_size.quantile(0.75)
students_df[students_df.shoe_size > students_df.shoe_size.quantile(0.75)]



# students_df['value_3rd_quartile']=(students_df.shoe_size.quantile(.75))
# students_df


# def evaluate(number):
#     if i > number:
#         'True'
#     else:
#         'False'
        
# # students_greater_than_3rd = 


# students_df.assign(greater_than_3rd_q=students_df.apply(evaluate(students_df.value_3rd_quartile[0])))

# 12. Find the names of all the students that have a shoe size less than the 1st quartile of shoe sizes

students_df.shoe_size.quantile(0.25)
students_df.shoe_size < students_df.shoe_size.quantile(0.25)
students_df[students_df.shoe_size < students_df.shoe_size.quantile(0.25)]


print('-----------------------------Aggregation & Plotting-----------------------------')
# Aggregation & Plotting
# 1. Calculate the mean, median, min, and max for the shoe sizes and favorite numbers
students_df[['shoe_size','fav_number']].agg(['mean', 'median', 'min', 'max'])

# 2. Sort the data frame by the students shoe size
students_df.sort_values('shoe_size')

# 3. Sort the data frame by the side of the classroom, then by their student number
students_df.sort_values('student_number').sort_values('shoe_size')

# 4. Find the number of students on each side of the classroom
students_df[['student_number','side_of_classroom']].groupby('side_of_classroom').count()

# 5. Find the average shoe size for each side of the classroom
grouped = students_df[['shoe_size','side_of_classroom']].groupby('side_of_classroom')
grouped
print(grouped['shoe_size'].agg(np.mean))


#alternatively
students_df[['shoe_size','side_of_classroom']].groupby('side_of_classroom').mean()

# 6. Find the maximum favorite number for each side of the classroom
students_df[['fav_number', 'side_of_classroom']].groupby('side_of_classroom').max()

# 7. Create a pie chart that visualizes the number of students on each side of the classroom.
number_students_each_side = students_df[['student_number','side_of_classroom']].groupby('side_of_classroom').count()
number_students_each_side.plot.pie(subplots=True)


# 8. Create a histogram of the shoe sizes in the classroom
students_df[['shoe_size']].plot.hist()

# 9. Create a histogram of the favorite numbers in the classroom
students_df[['fav_number']].plot.hist()

# 10. Create a scatter plot of shoe size vs favorite number
students_df.plot.scatter('shoe_size', 'fav_number')

print('---------------------------------Reading & Writing Data------------------------------------------')
# Reading & Writing Data

# 1. Save the students data to a csv file.
students_df.to_csv('students_database.csv')

# 2. Read the data from the csv file back into pandas. What do you notice?
pd.read_csv('students_database.csv')


# 3. Create a data frame based on the profiles.json file. Explore this data frame's structure.
profiles_df = pd.read_json('profiles.json')
profiles_df


# 4. Write the code necessary to create a data frame based on the results of a SQL query to the numbers database.

import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from env import user, password, host

url = 'mysql+pymysql://{}:{}@{}/numbers'.format(user, password, host)

dbc = create_engine(url)

df = pd.read_sql('SELECT * FROM numbers', dbc)
df