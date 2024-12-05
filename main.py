from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.tracer(0)

paddle_player = Paddle((-390, 0)) 
paddle_computer = Paddle((380, 0))
ball = Ball((0, 0))

def go_up():
    new_y = paddle_computer.ycor() + 20
    paddle_computer.goto(paddle_computer.xcor(), new_y)
    
    
def go_down():
    new_y = paddle_computer.ycor() - 20
    paddle_computer.goto(paddle_computer.xcor(), new_y)
    
    
game_is_on = True    
while game_is_on:
    screen.update()
    # ball.move()

    screen.listen()
    screen.onkey(go_up, "Right")
    screen.onkey(go_down, "Left")



screen.exitonclick()