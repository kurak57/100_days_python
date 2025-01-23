from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snakky")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()
        snake.extend()
        score_board.add_score()

    # collision with wall
    snake_x = snake.head.xcor()
    snake_y = snake.head.ycor()
    if snake_x > 280 or snake_x < -280 or snake_y > 280 or snake_y < -280:
        game_on = False
        score_board.game_over()

    # collision with tail (any snake body)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()

screen.exitonclick()