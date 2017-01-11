import turtle

def draw_sshapes():
    window = turtle.Screen()

    #FLOPPY (SQUARE)
    window.bgcolor("green")
    floppy = turtle.Turtle()
    floppy.shape("square")
    floppy.color("red")
    floppy.speed(1)

    for x in range(0,4): 
        floppy.forward(100)
        floppy.right(90)

    #WING (CIRCLE)
    window.bgcolor("blue")
    wing = turtle.Turtle()
    wing.shape("circle")
    wing.color("orange")
    wing.speed(1)

    wing.circle(100)

    #BOLT (TRIANGLE)
    window.bgcolor("purple")
    bolt = turtle.Turtle()
    bolt.shape("triangle")
    bolt.color("pink")
    bolt.speed(1)

    for x in range(0,3): 
        bolt.forward(100)
        bolt.right(120)
    
    window.exitonclick()

draw_shapes()
