# North Seattle College, CSC 110
# Week 1 Programming Assignment
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# A program that estimates the amount of various supplies needed for a month based constants.
# The program will prompt the user to enter how many clients are active for the month.
# Based on number of clients, the program will calculate to estimate how many units
# of each product will be needed for the month. Finally, it will output this information.

# Constants:
#Stock information (yearly averages/ months):
PREMIUM_PAPER = 8600 / 12
LETTER_PAPER = 5400 / 12
DELUXE_PAPER = 1300 / 12
# Sheets per ream
REAM = 500
# Business cards shipped per order
BUSINESS_CARDS = 5

# User input:
number_clients = int(input("How many clients do you expect to have this month? "))

# Calculations:
# get each paper value from number of clients and monthly average per client
total_premium_paper = number_clients * PREMIUM_PAPER
total_letter_paper = (number_clients / 2) * LETTER_PAPER
total_deluxe_paper = (number_clients * 0.15) * DELUXE_PAPER
# total number of sheets by number per ream
total_reams = (total_premium_paper + total_letter_paper + total_deluxe_paper) / REAM
# 5 cards sent per order
total_buiness_cards = number_clients * BUSINESS_CARDS
# 75% orders are shipped and require two labels
total_shipping_labels = (number_clients * 0.75) * 2

# Output:
print("\nTotal number of reams of paper:", total_reams)
print("Number of reams of Premium Copy paper:", total_premium_paper / REAM)
print("Number of reams of 40-pound letter stock paper:", total_letter_paper / REAM)
print("Number of reams of Airstream Deluxe A4 paper:", total_deluxe_paper / REAM)
print("Number of business cards:", total_buiness_cards)
print("Number of shipping labels:", total_shipping_labels)