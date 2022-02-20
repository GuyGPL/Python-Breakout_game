from turtle import *
from classes import Ball, Line, Paddle, ScorePaddle, ScoreBroad
from time import sleep, time

# set up screen
screen = Screen()
screen.setup(width=1080, height=720)
screen.bgcolor("black")
screen.tracer(0)

# add class
ball = Ball()
line = Line()
paddle = Paddle()
score_broad = ScoreBroad()

# control paddle by screen listen
screen.listen()
screen.onkey(key="a", fun=paddle.move_left)
screen.onkey(key="d", fun=paddle.move_right)

# generate score paddle
score_paddle_list = []
x_paddle_position = [-220, -155, -90, -25, 40, 105, 170, 235]
y_paddle_position = [320, 295, 270, 245, 220]
for y in y_paddle_position:
    for x in x_paddle_position:
        each_paddle = ScorePaddle(x, y)
        score_paddle_list.append(each_paddle)

game_on = True
i = True
start_time = 0
while game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    # detect collision ball with wall
    if ball.xcor() > 250 or ball.xcor() < -250:
        ball.bouncing_y()
    if ball.ycor() > 360:
        ball.bouncing_x()

    # detect collision with paddle
    if ball.distance(x=paddle) < 40 and -280 < ball.ycor() < -260:
        end_time = time()
        if end_time - start_time > 0.5:
            ball.bouncing_x()
            start_time = time()

    # detect collision with score paddle
    for paddle_clash in score_paddle_list:
        if ball.distance(paddle_clash) < 30:
            # print(f"ball distance from score paddle is {ball.distance(paddle_clash)}")
            paddle_clash.far_move()
            ball.bouncing_x()
            ball.y_move_spd *= 1
            score_broad.add_score()
            score_paddle_list.remove(paddle_clash)

    # detect game over
    if ball.ycor() < -350:
        score_broad.game_over()
        game_on = False
    # detect win game
    if len(score_paddle_list) == 0:
        score_broad.winner()
        game_on = False


screen.mainloop()
