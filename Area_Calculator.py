# North Seattle College, CSC 110
# Week 2 Lab 02
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# main function
def main():
    print("This program will test two functions")
    # Step 10 code
    print("Testing find_area_trapezoid...\n")

    # Step 12 code
    # Using arrays to store each shapes individual values
    # Trapezoid #1 values
    trap_1 = [4, 5, 8]
    # Trapezoid #2 values
    trap_2 = [2, 7, 9]
    # Trapezoid #3 values
    trap_3 = [6, 9, 13]
    # using an array to store the 3 areas from each Trapezoid
    trap_areas = [find_area_trapezoid(trap_1[0], trap_1[1], trap_1[2]), find_area_trapezoid(trap_2[0], trap_2[1], trap_2[2]), find_area_trapezoid(trap_3[0], trap_3[1], trap_3[2])]

    print("The area of a trapezoid with bases", trap_1[0], "and", trap_1[1], "and height", trap_1[2], "has an area of", trap_areas[0])
    print("The area of a trapezoid with bases", trap_2[0], "and", trap_2[1], "and height", trap_2[2], "has an area of", trap_areas[1])
    print("The area of a trapezoid with bases", trap_3[0], "and", trap_3[1], "and height", trap_3[2], "has an area of", trap_areas[2])

    print()

    # Step 15 code
    # Array to store the widths of both rectangles
    rect_1 = [5, 11]
    # Array to store the heights of both rectangles
    rect_2 = [11, 15]
    # Array to store the area of both rectangles
    react_areas = [find_area_rectangle(rect_1[0], rect_1[1]), find_area_rectangle(rect_2[0], rect_2[1])]

    print("The area of a rectangle with a width of", rect_1[0], "and height of", rect_1[1], "has an area of", react_areas[0])
    print("The area of a rectangle with a width of", rect_2[0], "and height of", rect_2[1], "has an area of", react_areas[1])



# This function calculates and returns the area of a trapezoid
# parameter: base1, the length of the top of the trapezoid
# parameter: base2, the length of the bottom
# parameter: height, the height of the trapezoid
# Notes: See this website for a picture  http://math.com/tables/geometry/areas.htm
def find_area_trapezoid(base1, base2, height):
    area = height / 2.0 * (base1 + base2)
    return area

# This function calculates and returns the area of a rectangle
# parameter: width, the width of the rectangle
# parameter: height, the length of the rectangle
def find_area_rectangle(width, height):
    return width * height

main()
