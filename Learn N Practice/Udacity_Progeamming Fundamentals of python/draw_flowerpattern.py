import turtle

def draw_flowerpattern():
    window = turtle.Screen()
    window.bgcolor("white")

    jogi = turtle.Turtle()
    jogi.shape("arrow")
    jogi.color("blue")
    jogi.speed(800)
    jogi.left(90)
    jogi.forward(150)

    for i in range(0,360/2):
        jogi.forward(90)
        jogi.right(70)
        jogi.forward(75)
        jogi.right(102)
        jogi.forward(75)
        jogi.right(70)
        jogi.forward(90)
        jogi.right(2)
    
    window.exitonclick()
    
draw_flowerpattern()
