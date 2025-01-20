from turtle import Turtle, Screen, colormode
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_guess = screen.textinput("Make your bet", "Which turtle will win?: (Blue/ Purple/ Red/ Orange)").lower()
colors = ["blue", "purple", "red", "orange"]

all_turtle = []
for i in range(4):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=-75+(50*i))
    all_turtle.append(turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've Lose! The {winning_color} turtle is the winner.")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()