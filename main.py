from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_player = Paddle((-390, 0)) 
paddle_computer = Paddle((380, 0))
ball = Ball((0,0))

screen.listen()
screen.onkey(paddle_player.go_up, "Right")
screen.onkey(paddle_player.go_down, "Left")
screen.onkey(paddle_computer.go_up, "d")
screen.onkey(paddle_computer.go_down, "a")    
    
game_is_on = True   
 
ball_x = -6
ball_y = 6
while game_is_on:
    screen.update()
    ball.move(ball_x, ball_y)

#Y Up --> Down
    if ball.ycor() >= 300:
        ball_y = -6
        
#X Right --> Left
    if ball.xcor() >= 400:
        ball_x = -6
        
#Y Down --> Up
    if ball.ycor() <= -300:
        ball_y = 6

#X Left --> Right 
    if ball.xcor() <= -400:
        ball_x = 6
    

screen.exitonclick()