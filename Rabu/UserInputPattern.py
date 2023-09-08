import turtle
import turtle
import time 
import random

print ("This Program Draws Shapes Based On The Number You Enter In A Uniform Pattern.")
num_str = input("Enter The Side Number Of The Shape You Want To Draw: ")
if num_str.isdigit():
    squares = int(num_str)

angle = 180*(squares-2)/squares

turtle.up

x = 0
y = 0

numshapes = 8
for x in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())
    x += 5
    y += 5
    turtle.forward(x)
    turtle.left(y)
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        turtle.left(angle)
        print (turtle.pos())
        turtle.up()
        turtle.end_fill()
time.sleep(11)
turtle.bye()