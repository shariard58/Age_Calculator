from datetime import  date

# Requesting the user to give input


birthday_input = input("Enter your Birthday like this format  : Year - month - Date \n  ")
birthday_input =birthday_input.split('-')
birth_year = int(birthday_input[0])
birth_month = int(birthday_input[1])
birth_day = int(birthday_input[2])









# storing the current date month and year

current_year = date.today().year
current_month = date.today().month
current_day = date.today().day







# initializing the result variable
calculated_day = 0
calculated_month = 0
calculated_year = 0

# Now there can be several condition the birthday day and birth month may be bigger or smaller than current date and or month

# Firstly we will check if the birth month is  greater than current  month and birthday is greater than current day
if birth_month > current_month and birth_day > current_day:
    calculated_day = (current_day+31) - birth_day
    calculated_month = ((current_month-1)+12) - birth_month
    calculated_year = (current_year-1) - birth_year
    print("The Current age  is = " + str(calculated_year) + " Years " + str(calculated_month) + " Month " + str(calculated_day) + " Days ")

# Secondly we will check if the birth_month is less than the current  month and the birthday is greater than the current  day
elif birth_month < current_month and birth_day > current_day:
    calculated_day = (current_day+31) - birth_day
    calculated_month = (current_month - 1 ) - birth_month
    calculated_year = current_year  - birth_year
    print("The current age is = " + str(calculated_year) + "  Years " + str(calculated_month) + " Month " + str(calculated_day) + " Days ")

# thirdly we will check weather the  birthmonth is greater than the current  month and the birthday is less than current date

elif birth_month > current_month and birth_day < current_day:
    calculated_day = current_day - birth_day
    calculated_month = (current_month + 12) - birth_month
    calculated_year = (current_year - 1) - birth_year
    print("The Current age  is = " + str(calculated_year) + "  Years " + str(calculated_month) + "  Month "  + str(calculated_day) + "  Days ")

# Then lastly if the both birth_month is less than the current  month and date
else:

    calculated_day = current_day - birth_day
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year

    print("The current age  is = " + str(calculated_year) + "  Years  " + str(calculated_month) + "  Month " + str(calculated_day) + " Days ")



















# birth_month < selected_month and birth_day < selected_day:




















