import turtle
turtle.color('pink')
#перемещаем черепаху влево, чтоб цунтр квадратов был в центре
turtle.left(180)
turtle.forward(5)
turtle.left(180)
for i in range(10,110,10):
    for j in range(4):
        turtle.forward(i)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.pendown()
