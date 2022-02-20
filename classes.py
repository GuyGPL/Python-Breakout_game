from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move_spd = 2.5
        self.y_move_spd = 2.5
        self.move_speed = 0.01
        self.reset_position()
        self.shapesize(0.5)

    def move(self):
        new_x = self.xcor() + self.x_move_spd
        new_y = self.ycor() + self.y_move_spd
        self.goto(x=new_x, y=new_y)

    def bouncing_x(self):
        self.y_move_spd *= -1
        if 1 < self.y_move_spd < 4.0 or -1 > self.y_move_spd > -4.0:
            self.y_move_spd *= 1.05

    def bouncing_y(self):
        self.x_move_spd *= -1

    def reset_position(self):
        self.goto(0, 0)


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-260, -350)
        self.pendown()
        self.goto(-260, 350)
        self.penup()
        self.goto(270, -350)
        self.pendown()
        self.goto(270, 350)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setpos(0, -280)

    def move_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())


color_list = ["green", "blue", "yellow", "red"]


class ScorePaddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.color(choice(color_list))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(x_position, y_position)

    def far_move(self):
        self.goto(2000, 2000)


FONT = ("Courier", 12, "normal")


class ScoreBroad(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-320, 300)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f" ----- Game Over -----\n       Score: '{self.score}'", align="center", font=("Courier", 24, "normal"))

    def winner(self):
        self.clear()
        self.goto(0, 0)
        self.write(" ----- You Win!! -----", align="center", font=("Courier", 24, "normal"))

