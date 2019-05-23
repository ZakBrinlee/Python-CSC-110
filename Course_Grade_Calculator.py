# North Seattle College, CSC 110
# Week 4 Lab
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# This program will ask the user to enter their course grade (out of 100), and then based on the
# grade will display what numerical grade that is equivalent to (out of 4.0).

def main():
    # gather input
    course_grade = float(input("Please enter your course grade (out of 100): "))

    # validate the data: course_grade must be greater than 0
    while course_grade < 0:
        print("ERROR: The course grade cannot be negative.")
        course_grade = float(input("Please enter your course grade (out of 100): "))

    # call function and save to variable
    numerical_grade = return_numerical_grade(course_grade)
    # print the user's imputed course grade and the numerical grade
    print("A", course_grade, "out of 100 is a", numerical_grade, "out of 4.0")


# This function determines the numerical grade (4.0) scale based on your percentage grade
# parameter: grade_out_of_100, the course percentage grade out of 100
# returns a floating point value that is the numeric score between 0.0 and 4.0
def return_numerical_grade(grade_out_of_100):
    if grade_out_of_100 >= 95:
        return 4.0
    elif grade_out_of_100 >= 90:
        return 3.5
    elif grade_out_of_100 >= 85:
        return 3.0
    elif grade_out_of_100 >= 80:
        return 2.5
    elif grade_out_of_100 >= 75:
        return 2.0
    elif grade_out_of_100 >= 70:
        return 1.5
    elif grade_out_of_100 >= 65:
        return 1.0
    else:
        return 0.0


main()


