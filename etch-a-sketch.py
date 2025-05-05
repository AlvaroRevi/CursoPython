from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(move_forwards, "W")
screen.onkey(move_backwards, "S")
screen.onkey(turn_left, "A")
screen.onkey(turn_right, "D")
screen.onkey(clean, "C")
screen.exitonclick()