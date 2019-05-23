# North Seattle College, CSC 110
# Week 5 Lab
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# import modules
import turtle
import random


# This is a simple program that will draw squares and triangles in an abstract way.
# Each function to draw a shape will take 4 parameters, the turtle object, size of each side, color to be drawn in
# and the starting point of the shape

# Lab 05 changes. Using randrange() to randomly provide radius or side length by ultilizing the random library
# Each time the program is run the shapes will be different sizes
# Each shape will also be in a slightly different location

# main function definition
def main():
    # initialize turtle object, named after my dog
    chica = turtle.Turtle()

    # call to draw random sized square based on randrange()
    draw_square(chica, random.randrange(10, 100), 'dark blue', [0, 0])
    # call to draw triangle with sides of randomly selected from range of 75-140
    draw_triangle(chica, random.randrange(75, 140), 'sienna', [random.randrange(50, 150), random.randrange(100, 150)])
    # call to draw random sized square based on randrange()
    draw_square(chica, random.randrange(150, 300), 'dark slate gray',
                [random.randrange(-300, 100), random.randrange(-100, 300)])
    # call to draw triangle with sides of randomly selected from range of 100-200
    draw_triangle(chica, random.randrange(100, 200), 'black', [random.randrange(-100, 100), random.randrange(100, 300)])
    # call to draw random sized square based on randrange()
    draw_square(chica, random.randrange(400, 500), 'yellow', [random.randrange(-100, -1), random.randrange(-50, 75)])
    # call to draw angled triangle of side of 95 pixels
    # set a different heading of turtle for a different angle of triangle
    chica.setheading(-10)
    draw_triangle(chica, random.randrange(250, 300), 'dark violet',
                  [random.randrange(5, 100), random.randrange(-100, -50)])

    # call to hide turtle after last draw
    chica.hideturtle()
    # call of done method to prevent auto-close of turtle widget
    turtle.done()


# This function uses one turtle to draw a square
# parameter: our_turtle, the turtle we created
# parameter: width, the width of the square to be drawn
# parameter: color, the color of the square to be drawn
# parameter: pos, the X and Y coordinates for the square to start at
def draw_square(our_turtle, width, color, pos):
    our_turtle.penup()
    our_turtle.setpos(pos)
    our_turtle.pendown()
    our_turtle.color(color)
    for side in range(4):
        our_turtle.forward(width)
        our_turtle.right(90)


# This function uses one turtle to draw a triangle
# parameter: our_turtle, the turtle we created
# parameter: side_length, the length of each triangle side to be drawn
# parameter: color, the color of the triangle to be drawn
# parameter: pos, the X and Y coordinates for the triangle to start at
def draw_triangle(our_turtle, side_length, color, pos):
    our_turtle.penup()
    our_turtle.setpos(pos)
    our_turtle.pendown()
    our_turtle.color(color)
    for side in range(3):
        our_turtle.forward(side_length)
        our_turtle.right(120)


main()
