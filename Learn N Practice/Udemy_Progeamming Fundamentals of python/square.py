import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100);
        some_turtle.right(90);

def draw_art():
    window = turtle.Screen();
    window.bgcolor("red");

    # Create the turtle Brad - Draws a square
    brad = turtle.Turtle();
    brad.shape("circle");
    brad.color("green");
    brad.shapesize(5, 5, 12);
    brad.speed(250);
    draw_square(brad);
    window.exitonclick();
    
draw_art();
