# prompt user for a day of the week, print out whether or not it is Monday.

day = input("What day? ")
print(f'day={day}')
if day == 'Monday':
    print('It\'s Monday')
else:
    print('It\'s not Monday')



# prompt the user for a day of the week, print out whther the day is a weekday or a weekend
day = input("What day? ")
# MY ANSWER
if day == 'Saturday' or 'Sunday':
    print('It\'s a weekend.')

else:
    print('It\'s a weekday.')

# OTHER WAYS TO DO IT:
if day.lower().startswith('s'):
    print('It is a weekend')
else:
    print('It is a weekday')

# create variables for 
# - the number of hours worked in one week

hours_worked_weekly = 43

# - the hourly rate

hourly_week_payrate = 90

# - how much the week's paycheck will be
if hours_worked_weekly > 40:
    paycheck = 40 * hourly_week_payrate + (hours_worked_weekly -40) * hourly_week_payrate*1.5
else:
    paycheck = hourly_week_payrate*hours_worked_weekly

print(paycheck)

# def weekly_paycheck(hourly_week_payrate, hours_worked_weekly):
#     print (int(hourly_week_payrate) * (int(hours_worked_weekly))

# weekly_paycheck(10, 10)


# write the python code to calculate the weekly paycheck you get paid. you get time and a half if you work more than 40 hours.
def weekly_paycheck(hourly_week_payrate, hours_worked_weekly):
    if hours_worked_weekly <= 40:
        print (int(hourly_week_payrate) * (int(hours_worked_weekly))
    else:
        (hours_worked_weekly*1.5)*hourly_week_payrate



