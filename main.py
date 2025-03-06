from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Py Snake Game")
screen.tracer(0)


starting_segments = 3
difficulty_level = 2

my_snake = Snake(starting_segments)
my_snake.set_difficulty(difficulty_level)

food = Food()
my_score = ScoreBoard()


screen.listen()
screen.onkey(my_snake.move_snake_up, "Up")
screen.onkey(my_snake.move_snake_down, "Down")
screen.onkey(my_snake.move_snake_left, "Left")
screen.onkey(my_snake.move_snake_right, "Right")
screen.onkey(my_score.end_game, "q")


def lost_game():
    my_score.game_over()
    screen.update()
    time.sleep(2)
    my_snake.reset_snake()
    screen.update()
    my_snake.new_snake(starting_segments)
    my_score.refresh_scoreboard()


while my_score.game_is_on:
    screen.update()
    time.sleep(my_snake.difficulty)
    my_snake.move_snake()

    # detect collision with food
    if my_snake.snake_head.distance(food) < 15:
        my_score.score_up()
        my_snake.add_segment()
        food.new_drop()

    #detect collision with wall
    if my_snake.snake_head.xcor() > 290 or my_snake.snake_head.xcor() < -290 or \
       my_snake.snake_head.ycor() > 290 or my_snake.snake_head.ycor() < -290:
        lost_game()
    #detect collision with tail
    else:
        for segment in my_snake.snake[1:]:
            if segment.distance(my_snake.snake_head) < 10:
                lost_game()


screen.exitonclick()
