from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.tracer(0)

paddle_player = Paddle((-390, 0)) 
paddle_computer = Paddle((380, 0))
ball = Ball((0, 0))
    
game_is_on = True   
 
while game_is_on:
    time.sleep(0.05)
    screen.update()
    # ball.move()

    screen.listen()
    screen.onkey(paddle_player.go_up, "Right")
    screen.onkey(paddle_player.go_down, "Left")
    
    screen.onkey(paddle_computer.go_up, "d")
    screen.onkey(paddle_computer.go_down, "a")

#just a comment. test-branch
screen.exitonclick()