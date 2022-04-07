# import colorgram
# rgb_color_list = []
#
# colors = colorgram.extract('image.jpeg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color_list.append(new_color)
# print(rgb_color_list)

import turtle as turtle_module
import random

terry = turtle_module.Turtle()
turtle_module.colormode(255)
terry.speed("fastest")
terry.penup()
terry.hideturtle()

color_list = [(36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234), (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166), (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0), (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98), (98, 96, 186), (244, 159, 151), (83, 34, 39), (254, 9, 13), (66, 71, 42), (9, 19, 0)]

terry.setheading(225)
terry.forward(300)
terry.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    terry.dot(20, random.choice(color_list))
    terry.forward(50)
    
    if dot_count % 10 == 0:
        terry.setheading(90)
        terry.forward(50)
        terry.setheading(180)
        terry.forward(500)
        terry.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()