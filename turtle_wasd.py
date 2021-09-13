import turtle

def go_up():
    if turtle.heading() != 90:
        turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def go_left():
    if turtle.heading() != 180:
        turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def go_down():
    if turtle.heading() != 270:
        turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def go_right():
    if turtle.heading() != 0:
        turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def reset():
    turtle.reset()


def turtle_wasd():
    turtle.onkey(go_up,'W')
    turtle.onkey(go_up,'w')
    turtle.onkey(go_left,'A')
    turtle.onkey(go_left,'a')
    turtle.onkey(go_down,'S')
    turtle.onkey(go_down,'s')
    turtle.onkey(go_right,'D')
    turtle.onkey(go_right,'d')
    turtle.onkey(reset,'Escape')
    turtle.listen()
    



turtle.stamp()
turtle_wasd()
