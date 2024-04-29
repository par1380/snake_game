import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

squares = []
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("brown")
screen.title("my snake game")

screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")




#print(squares[1].pos())

snake_game = True
#screen.update()
while snake_game:
    screen.update()
    time.sleep(0.1)
    #squares[0].forward(20)
    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.increase_snake()
        food.refresh()
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380 :
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    for square in snake.squares[1:]:

        if  snake.head.distance(square) < 10:
            scoreboard.game_over()
            scoreboard.reset()
            snake.reset()




screen.exitonclick()
