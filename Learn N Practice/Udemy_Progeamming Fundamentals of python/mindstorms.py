import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    # Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    # Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(2)
    angie.circle(100)

    # Create the turtle Yasi - Draws a Triangle
    yasi = turtle.Turtle()
    yasi.shape("arrow")
    yasi.color("green")
    yasi.speed(2)
    for i in range(0,3):
        yasi.forward(250)
        yasi.left(120)

    # Create the turtle Jogi - Draws a R
    jogi = turtle.Turtle()
    jogi.shape("turtle")
    jogi.color("blue")
    jogi.speed(800)
    jogi.left(90)
    jogi.forward(120)

    for i in range(0,36*4):
        jogi.forward(75)
        jogi.right(70)
        jogi.forward(75)
        jogi.right(110)
        jogi.forward(75)
        jogi.right(70)
        jogi.forward(75)
        jogi.right(3)
    
    window.exitonclick()
    
draw_art()
