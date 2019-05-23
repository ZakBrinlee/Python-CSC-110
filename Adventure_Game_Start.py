# North Seattle College, CSC 110
# Week 0 Programming Assignment
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# This program is the start of an adventure game using python
# Currently taking in 4 character attributes and a starting day of the story
# Using multiple variables in multiple places in the story

# input section
character_name = input("Please enter your character's name: ")
character_planet = input("Which of the 8 planets in our solar system is your character from? ")
character_nickname = input("Please enter your character's nickname: ")
starting_day = input("Please enter a day of the week: ")
character_career = input("What is your character's career? ")

# output section
print("\nWelcome to the great Python story teller! Where you create story elements as you go!") #using escape character \n to create new line from the prompt
print("\nOur story starts on a " + starting_day + ", just like every other day.") #using escape character \n to create a space from the story intro for cleaner formatting
print("Nothing out of the ordinary on the home planet of " + character_planet + ".")
print("The unlikely hero of our story is the humble " + character_name + ".")
print(character_name + " worked as a " + character_career + ".")
print("A very skilled " + character_career + " that was liked by everyone, always friendly, polite and welcomed everywhere around " + character_planet + ".")
print("Closest friends often called " + character_name +  " by " + character_nickname + ".")
print("An endearing nickname from childhood.")