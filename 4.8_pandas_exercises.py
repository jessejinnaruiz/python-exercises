import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from pydataset import data
# 1. Use pandas to convert the following list to a numeric series:
# python ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'] 


data = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

data_df = pd.Series(data).str.replace('$','').str.replace(',','')
data_df.astype('float')
data_df

# # 2. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

# fuel_econ_df = data('mpg') # load the dataset and store it in a variable
# data('mpg', show_doc=True) # view the documentation for the dataset
# fuel_econ_df

# #     * How many rows and columns are there?
# # A data frame with 234 rows and 11 variables
# fuel_econ_df.shape

# #     * What are the data types?
# fuel_econ_df.dtypes

# #     * Do any cars have better city mileage than highway mileage? NO

# (fuel_econ_df.cty > fuel_econ_df.hwy).any()


# #     * Create a column named milelage_difference this column should contain the difference between highway and 
# # city milelage for each car.

# fuel_econ_df['milelage_difference']=fuel_econ_df['hwy']-fuel_econ_df['cty']
# fuel_econ_df

# #     * On average, which manufacturer has the best miles per gallon? HONDA 28.5

# fuel_econ_df['mpg_combined'] = (fuel_econ_df['cty'] + fuel_econ_df['hwy'])/2
# fuel_econ_df

# fuel_econ_df[['manufacturer','mpg_combined']].groupby('manufacturer').agg(np.mean).sort_values(by='mpg_combined', ascending=False)



# #     * How many different manufacturers are there? 15

# fuel_econ_df[['manufacturer']].nunique()


# #     * How many different models are there? 38

# fuel_econ_df[['model']].nunique()

# #     * Do automatic or manual cars have better miles per gallon? Manual (ON AVG)

# find_t_type = lambda tran: 'auto' if tran.startswith('auto') else 'manual'
# fuel_econ_df['trans_grouped']=fuel_econ_df['trans'].apply(find_t_type)
# fuel_econ_df[['trans_grouped','mpg_combined']].groupby('trans_grouped').agg(np.mean).sort_values(by='mpg_combined', ascending=False)





# print('--------------------------------------M-A-M-M-A-L-S-------------------------------------------------')
# # 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

# mammals_df = data('mammals') # load the dataset and store it in a variable
# data('mammals', show_doc=True) # view the documentation for the dataset
# mammals_df

# #     * How many rows and columns are there? 107 rows, 4 columns
# mammals_df.shape


# #     * What are the data types? Float64, bool
# mammals_df.dtypes

# #     * What is the the weight of the fastest animal? Weight = 55.0
# mammals_df.sort_values(by='speed', ascending=False).head(1)


# #     * What is the overall percentage of specials? 9.35% specials

# mammals_df.specials = mammals_df.specials.astype(int)
# (mammals_df.specials.nunique()/mammals_df.specials.count())*100

# specials_percentage = (mammals_df.specials.sum() / mammals_df.weight.count())
# specials_percentage

# print('{:.2%} are specials'.format(specials_percentage))

# #     * How many animals are hoppers that are above the median speed? What percentage is this? 6.54%

# mammals_df.hoppers = mammals_df.hoppers.astype(int)
# hoppers = mammals_df[mammals_df.hoppers == 1]
# hoppers.speed.count()

# speedy_hoppers = hoppers[['speed']] > mammals_df.speed.median()
# speedy_hoppers = speedy_hoppers.speed.astype(int)
# speedy_hoppers.sum()

# percentage_of_speedy_hoppers = speedy_hoppers.sum()/hoppers.speed.count() *100
# percentage_of_speedy_hoppers

# # mammals_df.speed > mammals_df.speed.median()


# 4. Getting data from SQL databases
#     * Create a function named get_db_url. It should accept a username, hostname, password, and database name 
# and return a url formatted like in the examples in this lesson.

def get_db_url(user, pw, host, db):
    from sqlalchemy import create_engine
    from env import user, pw, host
    url = 'mysql+pymysql://{}:{}@{}/{}'.format(user, pw, host, db)
    return url


#     * Use your function to obtain a connection to the employees database.

import pandas as pd
from env import user, host, pw

conn = create_engine(get_db_url(user, host, pw,'employees'))


#     * Read the employees and titles tables into two separate data frames.
employees_from_employees_df = pd.read_sql('select * from employees', conn)
employees_from_employees_df
titles_from_employees_df = pd.read_sql('select * from titles', conn)
titles_from_employees_df

#     * Visualize the number of employees with each title.
# %matplotlib inline
merged_emp_with_titles = pd.merge(employees_from_employees_df, titles_from_employees_df, on='emp_no')


number_emp_titles = merged_emp_with_titles[['emp_no','title']].groupby('title').count()
number_emp_titles.plot(kind='bar')


#     * Visualize how frequently employees change titles.
emp_titles = merged_emp_with_titles[['emp_no','title']]
emp_titles
emp_titles.emp_no.value_counts().value_counts()

emp_titles.emp_no.value_counts().value_counts().plot.bar()


#     * Use the .join method to join the employees and titles data frames together.
employees_from_employees_df.join(titles_from_employees_df, lsuffix='_employees', rsuffix='_titles')


#     * For each title, find the hire date of the employee that was hired most recently with that title.

titles_grouped = merged_emp_with_titles[['emp_no', 'title', 'hire_date']].groupby('title').max()
# .sort_values(by='hire_date')
titles_grouped


# 5. Explore the data from the chipotle database. Write a python script that will use this data to answer the following questions:

#     * What is the total price for each order?
def get_db_url(user, pw, host, db):
    from sqlalchemy import create_engine
    from env import user, pw, host
    url = 'mysql+pymysql://{}:{}@{}/{}'.format(user, pw, host, db)
    return url

import pandas as pd
from env import user, host, pw

conn = create_engine(get_db_url(user, host, pw,'chipotle'))

tot_orders = pd.read_sql('select item_price, order_id from orders', conn)
tot_orders['item_price'] = tot_orders['item_price'].str.replace('$','')
tot_orders['item_price'] = tot_orders['item_price'].astype(float)
tot_orders = tot_orders.groupby('order_id').sum()
tot_orders = tot_orders.rename(columns={'item_price':'total_price'})
tot_orders

#     * What are the most popular 3 items?

popular_items = pd.read_sql('select item_name, quantity from orders', conn)
popular_items.groupby('item_name').sum().sort_values(by='quantity', ascending=False).head(3)

#     * Which item has produced the most revenue?
total_orders = pd.read_sql('select item_price, item_name from orders', conn)
total_orders['item_price'] = total_orders['item_price'].str.replace('$','')
total_orders['item_price'] = total_orders['item_price'].astype(float)

most_revenue_by_items = total_orders.groupby('item_name').sum().sort_values(by='item_price', ascending=False)
most_revenue_by_items.head(1)