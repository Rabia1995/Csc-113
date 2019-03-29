import words
import random
import tkinter as tk
from tkinter import simpledialog
from turtle import Turtle, Screen

# probabilities tuple indexes
key = 0
value = 1

# opens Tkinter interface to ask for input
application_window = tk.Tk()
application_window.withdraw()
n = simpledialog.askinteger('entries', "Please input number of letters to show", parent=application_window)


# open Word.txt file and get list of probability tuples sorted from most frequent letters from word module
words_txt = open("words.txt", "r")
probabilities = words.probability(words_txt)

# create list of random colors for each segment with no repeats
colors = []
for letter in range(n):
    color = '#' + "%06x" % random.randint(0, 0xFFFFFF)

    if color in colors:
        letter = letter - 1
    else:
        colors.append(color)

# radius for drawing circle and labels
radius = -200
label_r = radius * 1.25

# pie chart
chart = Turtle()
chart.penup()
chart.sety(-radius)
chart.pendown()

# draw segments
sum_prob = 0
for letter in range(n + 1):
    chart.begin_fill()

    if letter < n:
        chart.color(colors[letter])
        chart.circle(radius, probabilities[letter][value] * 360)
        sum_prob = sum_prob + probabilities[letter][value]
    else:
        chart.color("lightblue")
        chart.circle(radius, (1 - sum_prob) * 360)

    position = chart.position()
    chart.goto(0, 0)
    chart.end_fill()
    chart.setposition(position)

# draw labels
chart.penup()
chart.sety(-label_r)

for letter in range(n + 1):
    chart.color("black")

    if letter < n:
        chart.circle(label_r, probabilities[letter][value] * 360 / 2)
        label = str(probabilities[letter][key]) + ", " + str(round(probabilities[letter][value], 4))
        chart.write(label, align="center", font="Ariel")
        chart.circle(label_r, probabilities[letter][value] * 360 / 2)
    else:
        chart.circle(label_r, (1 - sum_prob) * 360 / 2)
        label = "All other letters, " + str(round((1 - sum_prob), 4))
        chart.write(label, align="center", font="Ariel")

# reset cursor to middle and keeps window open till click
chart.goto(0, 0)
screen = Screen()
screen.exitonclick()
