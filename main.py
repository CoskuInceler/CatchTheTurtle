# This script is written for the Catch the Turtle assignment in Python Bootcamp course by Atil Samancioglu
# Author: Y. Cosku Inceler
# Date: 05.09.2024 (Finished in 2 hours)

# Importing libraries and modules
import turtle
import random
import time

# User inputs to decide the level of difficulty and duration
TimerVar = int(input("Enter game time: "))
Difficulty = int(input("Please enter a difficulty level between 5 being easisest and 1 being hardest: "))

# Screen related code
WindowTurtle = turtle.Screen()
WindowTurtle.bgcolor("light blue")
WindowTurtle.title("Catch the Turtle - Cosku Inceler")
# Score text
t = turtle.Turtle()
t.penup()
t.teleport(0, 350)
t.pendown()
t.color("black")
style = ("Arial", 36, "normal")
Score = int()
t.write(arg = f"Your score: ", move = False, font = style, align = "center")
t.hideturtle()
tScore = turtle.Turtle()
tScore.penup()
tScore.teleport(130, 350)
tScore.pendown()
tScore.color("black")
styleScore = ("Arial", 36, "normal")
tScore.hideturtle()

# Timer text
t2 = turtle.Turtle()
t2.penup()
t2.teleport(x = 0, y = 300)
t2.pendown()
t2.color("black")
style2 = ("Arial", 24, "normal")
t2.write(arg="Time left: ", move=False, font=style2, align="center")
t2.hideturtle()
t3 = turtle.Turtle()
t3.penup()
t3.teleport(x = 75, y = 300)
t3.pendown()
t3.color("black")
style3 = ("Arial", 24, "normal")
t3.hideturtle()

# Termination
t4 = turtle.Turtle()
t4.color("black")
style4 = ("Arial", 52, "normal")
t4.hideturtle()
# turtle related code
TurtleInstance = turtle.Turtle()
TurtleInstance.shape("turtle")
TurtleInstance.shapesize(2)

# Scoring and clicking
def ScoringClick(x,y):
    global Score
    Score = Score +1
    tScore.clear()
    tScore.write(Score, move = False, font = styleScore)

TurtleInstance.onclick(ScoringClick)

# Timer and Game Generator
while TimerVar > 0:
    TimerVar = TimerVar - 1
    t3.write(arg=TimerVar, move=False, font = style3)
    x = random.randint(-450, 450)
    y = random.randint(-400, 280)
    TurtleInstance.teleport(x, y)
    time.sleep(Difficulty)
    t3.clear()

# Termination
TurtleInstance.hideturtle()
t4.write(arg= "Game Over", move=False, font=style4, align="center")

turtle.done()