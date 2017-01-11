import turtle

def design():
    window = turtle.Screen()
    window.bgcolor("red")

    kolu = turtle.Turtle()
    kolu.color("yellow")
    kolu.hideturtle()
    kolu.speed(10)

    for x in range(0,36):
        for y in range(0,4):
            kolu.forward(100)
            kolu.right(90)
        kolu.right(10)

    window.exitonclick()
    
design()
