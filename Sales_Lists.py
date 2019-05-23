# North Seattle College, CSC 110
# Week 6 Lab
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# The NUM_DAYS constant holds the number of days that we will gather sales data for.
NUM_DAYS = 5


# main function definition
def main():
    # Create a list to hold the sales for each day.
    sales = []

    print("Enter the sales for each day.")

    # Get the sales for each day.
    for day in range(1, NUM_DAYS + 1):
        sale = float(input("Day " + str(day) + ": "))
        sales.append(sale)

    # Call check sales to check to make sure our sales are correctly inputted
    check_sales(sales)


# This function checks to make sure the sales were inputted correctly
# This function allows the user to edit the sales data if necessary
# parameter: sales_data, a list of sales data ordered by day
def check_sales(sales_data):
    # Display the values entered.
    print("\nHere are the values you entered:")
    for day in range(NUM_DAYS):
        print("Day", day+1, "sales: ", sales_data[day])

    # trigger variable that goes through validation function
    is_correct = validate_string_input(input("Is this correct? (Enter yes/no): ").lower(), ['yes','no'])

    if is_correct == "yes":
        print("Your sales have been saved.")
    else:
        # Get the incorrect day
        incorrect_day = int(input("Which day is incorrect? "))
        # Get the correct sales data for the incorrect day
        correct_day_value = float(input("Enter the sales for this day: "))
        # Get the value based on the day/index provided
        sales_data[incorrect_day-1] = correct_day_value
        # call method again to recheck the new list
        check_sales(sales_data)


# This function validates any input against what the options are. If not valid then will prompt again
# parameters:
# choice: user input variable 'is_correct' from check_sales
# options: the two options for the prompt to be checked against
def validate_string_input(choice, options):
    valid_trigger = False
    user_choice = choice

    while not valid_trigger:
        if user_choice in options:
            return user_choice
        else:
            print("Your input is not accurate.")
            valid_trigger = False
            print("Options: ", *options, sep="\n")
            user_choice = input("Please input your selection from the list of options provided: ")


main()
