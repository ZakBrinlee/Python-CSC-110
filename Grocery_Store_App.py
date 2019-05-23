# North Seattle College, CSC 110
# Week 6 Programming Assignment
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# This program is for a mock grocery store with basic user functions
# See items, get average prices of all items, get total number of items and add a product.
#


def main():
    print("Welcome to Guido's Grocery's Item Database")
    cont_trigger = True

    products = [["Milk", 95520, 3.27, 20],
                ["Eggs", 55504, 2.97, 15],
                ["Bread", 57971, 2.78, 20],
                ["Apples", 19791, 0.78, 70],
                ["CheeseBits", 32510, 2.99, 25],
                ["CheeseBytes", 84159, 23.92, 10]]

    while cont_trigger:
        # user prompts
        choice = int(input("\nEnter 1 to display the table of our products\n"
                       "Enter 2 to add a product\n"
                       "Enter 3 to caclulate the average cost of the items\n"
                       "Enter 4 to caclulate the total number of individual items\n"
                       "Enter 0 to exit the program\n"
                       "What would you like to do? "))

        # conditionals for user choice
        if choice == 1:
            display_table(products)
        elif choice == 2:
            new_product = add_product()
            products.append(new_product)
            print(new_product[0], "added!")
        elif choice == 3:
            price_average = avg_price(products)
            print("\nThe average cost of the items in stock is", price_average)
        elif choice == 4:
            print("\nThe total number of items currently in stock is", total_stock(products))
        else:
            cont_trigger = False

    print("Good bye!")


# This function displays the full list of inventory
# parameters: 2d list of products
def display_table(products):
    print('\n{:<15} {:<15} {:<15} {:<15}'.format('Product Name', 'UPC', 'Price', 'Number in Stock'))

    for product in products:
        new_strings = []
        for item in product:
            new_strings.append(str(item))
        print('{:<15} {:<15} {:<15} {:^15}'.format(new_strings[0], new_strings[1], new_strings[2], new_strings[3]))


# This function prompts the user to provide information for adding a product
# returns the list of product information
def add_product():
    new_product = [input("Please enter the product name: "), int(input("Please enter UPC: ")),
                   float(input("Please enter the price: ")), int(input("Please enter the number in stock: "))]
    return new_product


# This function calculates the avg price for all the products
def avg_price(products):
    product_prices = []
    total_prices = 0
    for product in products:
        product_prices.append(product[2])
    for price in product_prices:
        total_prices = total_prices + price
    return total_prices / len(products)


# This function calculates the total number of items in stock
def total_stock(products):
    stock_numbers = []
    total = 0
    for product in products:
        stock_numbers.append(product[3])
    for stock_amount in stock_numbers:
        total = total + stock_amount
    return total


main()