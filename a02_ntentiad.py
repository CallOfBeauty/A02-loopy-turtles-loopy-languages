######################################################################
# Author: Dimitrios Ntentia
# Username: ntentiad
#
# Assignment: A02: Loopy Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes
######################################################################
# Acknowledgements:
#
# originally created by Dimitrios Ntentia
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
import turtle

wn = turtle.Screen()#creating the screen object, leaving it White

michel = turtle.Turtle() #creating my first turtle object for the flag

angelo = turtle.Turtle() #creating my second turtle object for the cross

angelo.color("gold")
angelo.penup()
angelo.goto(-300,250)
angelo.pendown()



#I am gonna create the flag of my country
michel.color("blue")
michel.penup()
michel.goto(-300,250)
michel.pendown()

for i in range(3):
  michel.begin_fill()#we will now go and create the first blue box, with the color blue
  for one in range(2):
    michel.forward(600)
    michel.right(90)
    michel.forward(100)
    michel.right(90)
  michel.end_fill()

  michel.right(90)
  michel.penup()
  michel.forward(200)
  michel.left(90)

angelo.forward(70)
angelo.forward(-35)
angelo.right(90)
angelo.forward(35)
angelo.forward(-70)
wn.exitonclick()