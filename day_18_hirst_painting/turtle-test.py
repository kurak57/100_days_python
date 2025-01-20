import turtle as t
import random

leo = t.Turtle()
leo.shape("turtle")
leo.color("blue")   

## Turtle Chal 1
# for _ in range(4):
#     leo.forward(100)
#     leo.right(90)

# # Turtle chal 2
# leo.penup()
# leo.setx(-200)
# leo.pendown()
# for _ in range(20):
#     leo.forward(10)
#     leo.penup()
#     leo.forward(10)
#     leo.pendown()


# #Turtle chal 3
# colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "cyan"]

# def make_shape(edge):
#     corner = int(360/edge)
#     for i in range(edge):
#         leo.forward(100)
#         leo.right(corner)

# for edge in range(3,11):
#     leo.color(random.choice(colors))
#     make_shape(edge)

# # Chal 4
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


# directions = [0,90,180,270] 
# leo.pensize(5)
# leo.speed(10)

# for _ in range(200):
#     leo.color(random_color())
#     leo.forward(40)
#     leo.setheading(random.choice(directions))


# chal 5
leo.speed('fastest')
def spirograph(gap):
    circle_gap = int(360/gap)
    for _ in range(circle_gap):
        leo.color(random_color())
        leo.circle(100)
        leo.left(gap)

spirograph(10)


screen = t.Screen()
screen.exitonclick()