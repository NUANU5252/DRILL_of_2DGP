import turtle

count1 = 5
count2 = 5


turtle.penup()
while(count1>-1):
    turtle.left(90)
    turtle.goto(count1*100,0)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()

    turtle.right(90)
    turtle.goto(0,count1*100)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    count1 -= 1
