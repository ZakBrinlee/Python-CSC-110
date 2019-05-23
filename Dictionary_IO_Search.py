# North Seattle College, CSC 110
# Week 7 Lab
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com


# main function definition
def main():
    # Create an empty dictionary that will eventually hold the data
    user_data = {}

    # csv file name
    user_file = "user_data.csv"

    # Process number data from the file here
    file_data = open(user_file, "r")

    # Go through each line of the file
    for line in file_data:
        # Add the name and associated id to the dictionary
        # as key-value pair such that the key is the name and the value is the id
        this_line = line.split(",")
        user_data[this_line[0]] = this_line[1].strip()

    # close csv connection
    file_data.close()

    # User interface
    keep_running = True

    while keep_running:

        # Call display_number_info here:
        display_user_info(user_data)

        # Ask the user if they want to continue:
        # input is validated
        user_resp = validate_string_input(input("Would you like to check another user? (yes/no): "), ["yes", "no"])

        # Stop running the user interface while loop if the user doesn't want to continue
        if user_resp == "no":
            keep_running = False
            print("Goodbye")


# This funciton prompts the user for a name and displays the ID of that user
# Uses the dictionary to look up the user ID
# Instead displays a message if the username is not in the dictionary
def display_user_info(user_data):
    name = input("Please enter a name to look up: ")
    if name in user_data:
        print("The user ID for", name, "is", user_data.get(name)) #### EDIT THIS LINE for step 16
    else:
        print("Sorry, the user", name, "does not exist.")


# This function validates any input against what the options are. If not valid then will prompt again
# parameters: Same as the globals
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