from turtle import *
import tkinter as tk
from tkinter import simpledialog
import random  # for random colors


class PieChart(object):
    def __init__(self, radius=175, file="words.txt", f=" ", num_letters=3, total=0, letter_count=0, sum_freq_of_Letters = 0, sum_prob=0, file_letters={}, used_colors=[]):
        self.radius = radius
        self.file = file
        self.f = f
        self.num_letters = num_letters
        self.total = total
        self.file_letters = file_letters
        self.sum_freq_of_Letters = 0
        self.letter_count = 0
        self.sum_prob = 0
        self.used_colors = []
        self.probability()

    def probability(self):
        file_contents = self.f.readlines()
        for line in file_contents:
            print(line)
            line = line.lower()
            for letter in line:
                if letter == "\n":
                    letter = " "
                self.letter_count = line.count(letter)
                self.file_letters[letter] = self.letter_count

        for letter, self.letter_count in self.file_letters.items():
            self.sum_freq_of_Letters = self.sum_freq_of_Letters + self.letter_count

        count = 0
        for letter, self.letter_count in self.file_letters.items():
            if count < self.num_letters:
                letter_probability = self.letter_count/int(self.sum_freq_of_Letters)  # formula given in instructions
                print("Probability of", "'"+ letter +"'", 'is', str(letter_probability))
                self.sum_prob += letter_probability
                count = count + 1
            else:
                break

        for value in self.file_letters:
            self.total = self.total + self.file_letters[value]

    def get_RGB(self):

        R = random.randrange(0, 255, 7)
        G = random.randrange(0, 255, 7)
        B = random.randrange(0, 255, 7)
        RGB = (R, G, B)
        return RGB

    def random_diff_colors(self):
        while True:
            is_used = False
            currentRGB = self.get_RGB()
            for color in self.used_colors:
                if color == currentRGB:
                    is_used = True
                    break
            if not is_used:
                break
        self.used_colors.append(currentRGB)
        return currentRGB

        # The labeling for each slice
        radius_label = self.radius * 1.33
        turtle.penup()
        turtle.sety(-radius_label)

        count = 0
        current_total = 0
        for letter, self.letter_count in self.file_letters.items():
            letter_probability = self.letter_count/int(self.sum_freq_of_Letters)
            if letter == " ":
                letter = "WhiteSpace"
            if count < self.num_letters:
                turtle.circle(radius_label, self.letter_count * 360 / self.total / 2)  # circle(radius, extent, steps)
                turtle.write(letter + ', ' + str(round(letter_probability,5)), align="center", font=("Times New Roman", 10))
                turtle.circle(radius_label, self.letter_count * 360 / self.total / 2)
            else:
                turtle.circle(radius_label, 180-current_total / 2)  # circle(radius, extent, steps)
                turtle.write("All Other Letters" + ', ' + str(round(1-self.sum_prob,5)), align="center", font=("Times New Roman", 10))
                turtle.circle(radius_label, 180-current_total / 2)
                break
            count += 1
            current_total += self.letter_count * 360 / self.total

        turtle.hideturtle()
        done()

    def __str__(self):
        return "File Name: {}".format(self.file)


def main():
    while True:
        print()
        file = input("Enter the file's name with extension in the correct directory: ")
        try:
            f = open(file, 'r')
        except FileNotFoundError:
            print("Wrong file or file path. Please try again.")
        else:
            break

    app = tk.Tk()
    app.withdraw()
    num_letters = simpledialog.askinteger('Pie Chart Limit', "Please input number of letters to show on Pie Chart:", parent=app)

    pie_chart = PieChart(200, file, f, num_letters)  # Create instance using the file we entered
    pie_chart.draw_chart()


def draw_chart(self):
    turtle = Turtle()
    turtle.penup()
    turtle.sety(-self.radius)
    turtle.pendown()

    screen = Screen()
    screen.colormode(255)
    count = 0
    current_total = 0

    for value in self.file_letters:
        if count < self.num_letters:
            turtle.fillcolor((self.random_diffcolors()))
            turtle.begin_fill()
            turtle.circle(self.radius, self.file_letters[value] * 360 / self.total)
            position = turtle.position()
            turtle.goto(0, 0)
            turtle.end_fill()
            turtle.setposition(position)
        else:
            turtle.fillcolor((self.random_diffcolors()))
            turtle.begin_fill()
            turtle.circle(self.radius, 360 - current_total)
            position = turtle.position()
            turtle.goto(0, 0)
            turtle.end_fill()
            turtle.setposition(position)
            break

    count = count + 1
    current_total += (self.file_letters[value] * 360 / self.total)

    radius_label = self.radius * 1.33
    turtle.penup()
    turtle.sety(-radius_label)

    count = 0
    current_total = 0

    for letter, self.letter_count in self.file_letters.items():
        letter_probability = self.letter_count/int(self.sum_freq_of_Letters)

        if letter == " ":
            letter = "WhiteSpace"
        if count < self.num_letters:
            turtle.circle(radius_label, self.letter_count * 360 / self.total / 2)  # circle(radius, extent, steps)
            turtle.write(letter + ', ' + str(round(letter_probability,5)), align="center", font=("Times New Roman", 10))
            turtle.circle(radius_label, self.letter_count * 360 / self.total / 2)
        else:
            turtle.circle(radius_label, 180-current_total / 2)  # circle(radius, extent, steps)
            turtle.write("All Other Letters" + ', ' + str(round(1-self.sum_prob,5)), align="center", font=("Times New Roman", 10))
            turtle.circle(radius_label, 180-current_total / 2)
            break

    count += 1
    current_total += self.letter_count * 360 / self.total

    turtle.hideturtle()
    done()


main()