# North Seattle College, CSC 110
# Week 7 Programming Assignment
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# This program will be working with NASA's Open Data Portal about all known meteorite landings.
# The program will read through a csv file and load every meteorite name and details into a dictionary
# The program will prompt the user to look up a specific meteor by name or create a csv file of all
# meteors with a mass greater than selected.
# Added bonus is a nice table displayed of all meteorite data

# Create list of meteor names for input validation
METEOR_NAMES = []


# main function definition
def main():
    # Create an empty dictionary that will eventually hold the data
    met_dictionary = {}

    # csv file name
    meteorite_file = "Meteorite_Landings.csv"

    # csv TEST file name
    test_file = "Mtesting.csv"

    # Process number data from the file here
    file_data = open(meteorite_file, "r", encoding="utf8")

    table_header = file_data.readline()
    # Go through each line of the file
    for line in file_data:

        # strip each line of characters to ignore
        this_line = line.replace('(', '').replace(')', '').replace('"', '').replace("\n", '')
        this_line = this_line.split(',')

        # if Lat/Long are missing, add it to the line list
        if len(this_line) == 3:
            this_line[2] = -1
            this_line.append("-1")

        # if any values are blank, assign value of -1
        if this_line[1] == '':
            this_line[1] = -1

        if this_line[2] == '':
            this_line[2] = -1

        if this_line[3] == '':
            this_line[3] = -1

        # Add the name and associated id to the dictionary
        # as key-value pair such that the key is the name and the value is the id
        met_dictionary[this_line[0]] = int(this_line[1]), float(this_line[2]), float(this_line[3])

        # Add each name to global list for validation
        METEOR_NAMES.append(this_line[0])

    # close csv connection
    file_data.close()

    cont_trigger = True

    # prompt user and make selection
    while cont_trigger:
        # user prompts
        choice = validate_string_input(input("Enter 1 to look up information on a meteorite by name.\n"
                                             "Enter 2 to create a new csv file that contains all meteorites greater than a specified mass.\n"
                                             "Enter 3 to display all Meteor infomation.\n"
                                             "Enter 0 to exit.\n"
                                             "\nWhat would you like to do? "), ['1', '2', '3', '0'])

        # conditionals for user choice
        if choice == '1':
            get_meteorite_info(met_dictionary)
        elif choice == '2':
            create_mass_file(met_dictionary)
        elif choice == '3':
            display_table(met_dictionary)
        else:
            cont_trigger = False

    print("\nGood bye!")


# This function will prompt the user to enter a meteor name to get the info about it
def get_meteorite_info(met_dictionary):
    # this section is working how the assignment is outlined with the method being recalled if no meteorite found

    # meteor_name = input("\nPlease enter the name of the meteorite you'd like to look up: ")
    # if met_dictionary.get(meteor_name):
    #     meteor_info = met_dictionary.get(meteor_name)
    #     print("The meteorite named", meteor_name, "weighed", meteor_info[0], "grams and was found at latitude",
    #           meteor_info[1], "and longitude", meteor_info[2], "\n")
    # else:
    #     print("ERROR: no meteorite data found")
    #     get_meteorite_info(met_dictionary)

    # this section is using my validation function
    meteor_name = validate_string_input(input("\nPlease enter the name of the meteorite you'd like to look up: "),
                                        METEOR_NAMES)

    # get info from dictionary using the key: meteor name
    meteor_info = met_dictionary.get(meteor_name)
    # print info
    print("\nThe meteorite named", meteor_name, "weighed", meteor_info[0], "grams and was found at latitude",
          meteor_info[1], "and longitude", meteor_info[2])
    print()


# This function will prompt the user to enter a mass as an integer
# create a list containing all of the names of meteorites with a mass strictly greater than the mass entered by the user
# Sort the list then create new csv file that contains list of meteors
def create_mass_file(met_dictionary):
    meteor_mass_list = []
    meteor_mass = int(input("\nPlease enter a mass: "))

    # loop through dictionary and check if meteor masses greater than input
    for meteor in met_dictionary:
        meteor_info = met_dictionary.get(meteor)
        if meteor_info[0] > meteor_mass:
            meteor_mass_list.append(meteor)

    # create file name from user input AND open file for writing
    file_name = str(meteor_mass) + ".csv"
    meteor_mass_file = open(file_name, "w", encoding="utf8")  # this opens the file for writing

    # sort list
    meteor_mass_list.sort()
    # loop through list and write each to file
    for meteor in meteor_mass_list:
        meteor_mass_file.write(meteor + "\n")

    print("File", file_name, "has been created.\n")


# This function displays the full list of meteor dictionary
def display_table(met_dictionary):
    print('\n{:<25} {:<15} {:<15} {:<15}'.format('Meteor Name', 'Mass (grams)', 'Latitude', 'Longitude'))

    for meteor in met_dictionary:
        meteor_info = met_dictionary.get(meteor)
        print('{:<25} {:<15} {:<15} {:^15}'.format(meteor, meteor_info[0], meteor_info[1], meteor_info[2]))


# This function validates any input against what the options are. If not valid then will prompt again
def validate_string_input(choice, options):
    valid_trigger = False
    user_choice = choice

    while not valid_trigger:
        if user_choice in options:
            return user_choice
        else:
            print("ERROR: no meteorite data found")
            valid_trigger = False
            user_choice = input("Please enter the name of the meteorite you'd like to look up: ")


main()
