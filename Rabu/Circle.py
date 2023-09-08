import turtle
def tangentCircles (ttl):
    r = 10
    n = 10
    for i in range (10):
        ttl.circle ( r * i)
def concentrisCircles ( ttl ):
    r = 10
    for i in range (10) :
        ttl.circle ( r * i)
        ttl.up()
        ttl.sety (( r * i) *( -1) )
        ttl.down()

Ben = turtle . Turtle ()
Ben.up() ; Ben.goto(0 , 150)
Ben.down() ; Ben.pencolor("Blue")
tangentCircles(Ben)
Ben.up() ; Ben.goto(0 , -150)
Ben.down() ; Ben.pencolor("Red")
concentrisCircles(Ben)
turtle.done()