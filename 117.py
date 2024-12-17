import turtle as trtl

turtles = []

shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
colors = ["red", "blue", "green", "orange", "purple", "gold", 'yellow', 'pink', 'brown', 'cyan', 'Gainsboro', 'gray', 'dimgray', 'LightSlateGray', 'AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki']

heading = 0
length = 100
increment = 10

for i in range(len(shapes)):
    t = trtl.Turtle(shape=shapes[i])

    color = colors.pop(0)
    t.color(color)

    t.penup()

    if i == 0:
        t.goto(0, 100)
    else:
        t.goto(turtles[i-1].xcor(), turtles[i-1].ycor())

    t.setheading(heading)

    t.pendown()

    t.forward(length)
    t.right(60)

    length += increment

    heading = t.heading()

    turtles.append(t)

wn = trtl.Screen()
wn.mainloop()
