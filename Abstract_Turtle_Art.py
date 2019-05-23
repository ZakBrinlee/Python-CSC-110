# North Seattle College, CSC 110
# Week 3 Programming Assignment
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# import modules
import turtle


#
# Simple program that create abstract artwork by using 3 polygons and two clusters of concentric circles
# User input provides the number of sides for each polygon, number of circles in each cluster and the shape scale.
#

# main function definition
def main():
    # user input prompts
    # initialize variables from input
    polygon_1 = int(input("Please enter a positive integer that is 3 or greater: "))
    polygon_2 = int(input("Please enter another positive integer that is 3 or greater: "))
    polygon_3 = int(input("Please enter another  positive integer that is 3 or greater: "))

    number_circles_1 = int(input("Please enter a positive integer: "))
    number_circles_2 = int(input("Please enter another positive integer: "))
    shape_scale = int(input("Finally, please enter a positive integer between 50 and 200: "))

    # initialize turtle object, named after my dog
    chica = turtle.Turtle()

    # call for first polygon
    draw_polygon(chica, polygon_1, shape_scale, 'dark olive green', [0, 0])
    # call for first polygon
    draw_polygon(chica, polygon_2, shape_scale, 'orange', [150, 300])
    # call for first polygon
    draw_polygon(chica, polygon_3, shape_scale, 'dark violet', [-200, -200])

    # call for first cluster of circles
    draw_concentric_circles(chica, number_circles_1, shape_scale, [-10, -15])

    # call for second cluster of circles
    draw_concentric_circles(chica, number_circles_2, shape_scale, [100, -150])

    # call to hide turtle after last draw
    chica.hideturtle()
    # call of done method to prevent auto-close of turtle widget
    turtle.done()


# This function uses one turtle to draw a polygon based on arguments from input
# parameter: our_turtle, the turtle we created
# parameter: num_sides, the total number of side for the polygon
# parameter: side_length, the length of each side of the polygon
# parameter: color, the color of the square to be drawn
# parameter: pos, the X and Y coordinates for the square to start at
def draw_polygon(our_turtle, num_sides, side_length, color, positon):
    our_turtle.penup()
    our_turtle.goto(positon)
    our_turtle.pendown()
    rotate = 360 / num_sides
    our_turtle.begin_fill()
    our_turtle.fillcolor(color)

    for side in range(num_sides):
        our_turtle.forward(side_length)
        our_turtle.right(rotate)
    our_turtle.end_fill()


# This function uses one turtle to draw concentric circles
# parameter: our_turtle, the turtle we created
# parameter: num_circles, the total number of circles to be drawn
# parameter: pos, the X and Y coordinates for the first circle to start at
def draw_concentric_circles(our_turtle, num_circles, starting_radius, positon):
    current_radius = starting_radius
    our_turtle.penup()
    our_turtle.goto(positon)
    our_turtle.pendown()
    our_turtle.circle(current_radius)
    for i in range(num_circles - 1):
        current_radius = current_radius + 20
        our_turtle.up()
        our_turtle.right(90)
        our_turtle.forward(20)
        our_turtle.left(90)
        our_turtle.down()
        our_turtle.circle(current_radius)


main()
