import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100);
        some_turtle.right(90);

def draw_triangle(some_turtle):
    for i in range(0,3):
        some_turtle.left(120);
        some_turtle.forward(100);
        
def draw_art():
    window = turtle.Screen();
    window.bgcolor("red");

    # Create the turtle Brad - Draws a square
    brad = turtle.Turtle();
    brad.shape("circle"); #turtle
    brad.color("green");
    #brad.shapesize(5, 5, 12);
    brad.speed(250);
    draw_square(brad);

    # Create the turtle angie - Draws a circle
    angie = turtle.Turtle();
    angie.shape("arrow"); #turtle
    angie.color("blue");
    angie.circle(100);

    # Create the turtle jane - Draws a triangle
    jane = turtle.Turtle();
    jane.shape("turtle"); #turtle
    jane.color("green");
    jane.speed(250);
    draw_triangle(jane);
    
    window.exitonclick();
    
draw_art();
