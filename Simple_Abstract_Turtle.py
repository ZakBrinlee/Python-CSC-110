# North Seattle College, CSC 110
# Week 3 Lab
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# import modules
import turtle

# This is a simple program that will draw squares and triangles in an abstract way.
# Each function to draw a shape will take 4 parameters, the turtle object, size of each side, color to be drawn in
# and the starting point of the shape

# main function definition
def main():

    # initialize turtle object, named after my dog
    chica = turtle.Turtle()

    # call to draw 50x50 square
    draw_square(chica, 50, 'dark blue', [0,0])
    # call to draw triangle with sides of 95 pixels
    draw_triangle(chica, 95, 'sienna', [150,150])
    # call to draw 300x300 square
    draw_square(chica, 300, 'dark slate gray', [-300,300])
    # call to draw triangle with sides of 150 pixels
    draw_triangle(chica, 150, 'black', [-250, 200])
    # call to draw 600x600 square
    draw_square(chica, 400, 'yellow', [-50,50])
    # call to draw angled triangle of side of 95 pixels
    # set a different heading of turtle for a different angle of triangle
    chica.setheading(-10)
    draw_triangle(chica, 95, 'dark violet', [50, -50])

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
