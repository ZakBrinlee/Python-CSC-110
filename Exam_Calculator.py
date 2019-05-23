# North Seattle College, CSC 110
# Week 2 Personal Assignment
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# Your overall course grade will be calculated as follows:
# Lab Assignments	10%
# Homework Quizzes	15%
# Programming Assignments	30%
# Midterm Exam	20%
# Final Exam	25%

# This program that calculates the average score you need across the midterm and the final exams to achieve a certain
# overall grade in the course. The program will prompt the user to end four pieces of data via user input:
# current grade in homework quizzes, current grade in lab assignments, current grade in programming assignments,
# & your target course grade. The program will calculate the score needed to earn on the midterm and final exams
# (assume you get the same score across both exams) to achieve the target course grade based on the values provided.


def main():
    # A main function which controls the flow of the program including:
    # User Input
    # current overall grade from homework assignments
    homework_grade = float(input("Enter your current grade (out of 100) on homework quizzes: "))
    # current overall grade from weekly labs
    lab_grade = float(input("Enter your current grade (out of 100) on lab assignments: "))
    # current overall grade from programming assignments
    pa_grade = float(input("Enter your current grade (out of 100) on programming assignments: "))
    target_grade = float(input("Enter your target grade (out of 100): "))

    print("\nCalculating...\n")
    # Process:
    current_grade = calculate_current_grade(homework_grade, lab_grade, pa_grade)
    exam_score = calculate_exam_score(current_grade, target_grade)

    # Output
    print("Your current grade (out of 55) is", current_grade)
    print("To get a", target_grade, "(out of 100) in the course, you must score an average of", exam_score, "percent across the two exams.")


# This function calculates & returns overall score from the 3 non exam categories with their individual grading weights
# parameter: hw_score, current grade of homework assignments
# parameter: lab_score, current grade of lab assignments
# parameter: pa_score, current grade of programming assignments
def calculate_current_grade(hw_score, lab_score, pa_score):
    return hw_score * .15 + lab_score * .1 + pa_score * .3


# This function calculates & returns the minimum average score for both final and midterm exams to achieve target grade
# parameter: current_grade, current overall grade of assignments to date
# parameter: target_grade, minimum grade wanting to be achieve at end of quarter
def calculate_exam_score(current_grade, target_grade):
    grade_difference = target_grade - current_grade
    return grade_difference / 0.45


main()