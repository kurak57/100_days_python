from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

MAXIMUM_SCORE = screen.numinput("Maximum Score", "what score to win?")


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()      

    # ball collision with top bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ball collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # ball missed by r_paddle    
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    # ball missed by l_paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

    if scoreboard.r_score >= MAXIMUM_SCORE or scoreboard.l_score >= MAXIMUM_SCORE:
        game_on = False
        scoreboard.game_over()
    
screen.exitonclick()