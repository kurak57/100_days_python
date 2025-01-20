# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)

# print(rgb_colors)

import turtle as t
import random

leo = t.Turtle()
t.colormode(255)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

leo.penup()
leo.setx(-225)
leo.sety(-225)
leo.speed('fastest')
leo.hideturtle()

def hirst_painting(p, l):
    for column in range(l):
        start_positon = leo.position()
        for row in range(p):
            random_color = random.choice(color_list)
            leo.pensize(20)
            leo.dot(20, random_color)
            leo.penup()
            leo.forward(50)
        leo.penup()
        leo.sety(start_positon[1]+50)
        leo.setx(start_positon[0])
        leo.pendown()

hirst_painting(10,10)

screen = t.Screen()
screen.exitonclick()