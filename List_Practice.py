# North Seattle College, CSC 110
# Week 6 practice with lists
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

##
# 1. Write a function that is passed in a positive integer and returns a list loaded with the squares of the numbers 1, 2, ..., up to and including the positive integer.
# 2. Write a function that is passed in a list of strings and returns a new list with all the strings from the original list whose length is 5 or more
# 3. Write a function that is passed in a list of strings and returns the longest string (or the index of the longest string)
# 4. Write a function that is passed in a list of numbers and 2 additional numbers, low and high.  The function counts up and returns how many values in the list are between lo and high (inclusive).
# 5. Write a function that is passed in a list and 2 integers representing indexes. The function swaps the values in the list at those 2 indexes.
# 6. Write a function that is passed in a list of integers and a single integer. Return a new list with all the values from the original list that are a multiple of the single integer.

# Here are some more challenging ones
# 7. Write a function that is passed in a list and reverses its contents (nothing is returned. Remember that lists are passed by reference.) Solve this without using another list and without using the built-in reverse() method. I want you to figure out the algorithm.
# 8. Write a function that is passed in a list of numbers, sums up each pair of numbers in the list, and returns those values in a new list. If the original list had an odd number of values, then the last value in the original list is summed with 0.
# 9. Write a function that is passed in a list and returns true if the data is in sorted, non-descending order. This means that every value in the list is >= the value before it.
# 10. Write a function that is passed in a list of numbers and returns true if the list contains duplicates next to each other (in otherwords, at some index [i] and [i + 1])  Return false otherwise.


# main function definition
def main():

    # Call function 1
    print(function_1(5))
    print(function_2(["Punch it Chewie!", "Never tell me the odds", "Zak", "2019"]))
    print(function_3(["Punch it Chewie!", "Zak", "2019", "Never tell me the odds"]))
    print(function_4([65, 82, 105, 542, 15, 2019]))

    print(function_5([1,5,10,15,20], 1, 4))
    print(function_6([1, 8, 17, 12, 64, 11, 72], 3))
    function_7([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(function_8([1, 1, 2, 2, 3, 3]))
    print(function_9([1, 2, 3, 4, 5, 6]))
    print(function_10([1, 2, 3, 4, 5, 6]))


def function_10(number_list):
    for current_index in range(len(number_list) - 1):
        if number_list[current_index] == number_list[current_index + 1]:
            return True
        else:
            is_duplicate = False

    return is_duplicate


def function_9(number_list):

    for current_index in range(len(number_list)-1):
        if number_list[current_index] <= number_list[current_index+1]:
            is_sorted = True
        else:
            return False

    return is_sorted


def function_8(number_list):
    new_list = []

    for first_num in range(0, len(number_list), 2):
        if first_num == len(number_list)-1:
            pair_sum = number_list[first_num] + 0
        else:
            first_value = number_list[first_num]
            pair_sum = first_value + number_list[first_num+1]
        new_list.append(pair_sum)

    return new_list


def function_7(data_list):
    print("Original List: ", data_list)
    middle_index = len(data_list) / 2
    for index in range(int(middle_index)):
        temp = data_list[index]
        last_index = len(data_list) - 1 - index
        data_list[index] = data_list[last_index]
        data_list[last_index] = temp
    print("Reversed List: ", data_list)


def function_6(integer_list, mult_num):
    multiples_of_num = []
    for number in integer_list:
        if number % mult_num == 0:
            multiples_of_num.append(number)

    return multiples_of_num


def function_5(mixed_list, index_1, index_2):
    temp_value = mixed_list[index_1]
    mixed_list[index_1] = mixed_list[index_2]
    mixed_list[index_2] = temp_value

    return mixed_list


def function_4(number_list):
    low = min(number_list)
    high = max(number_list)
    number_list.sort()
    counter = 0

    for number in number_list:
        if low < number < high:
            counter = counter +1

    return counter


def function_3(string_list):
    longest_string = string_list[0]
    longest_index = 0

    for string in string_list:
        if len(string) > len(longest_string):
            longest_string = string

    return [longest_string, string_list.index(longest_string)]


def function_2(string_list):
    new_list = []
    for string in string_list:
        if len(string) >= 5:
            new_list.append(string)

    return new_list


def function_1(num):
    square_nums = []
    for number in range(1,num+1):
        square_nums.append(number*2)

    return square_nums


main()