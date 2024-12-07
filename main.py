from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_l = Paddle((-370, 0)) 
paddle_r = Paddle((360, 0))
ball = Ball((0,0))

screen.listen()
screen.onkey(paddle_r.go_up, "Right")
screen.onkey(paddle_r.go_down, "Left")
screen.onkey(paddle_l.go_up, "d")
screen.onkey(paddle_l.go_down, "a")    
    
game_is_on = True   
 
# ball_x = -6
# ball_y = -6
while game_is_on:
    screen.update()
    ball.move(ball.x_move, ball.y_move)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(x=False)
        
    if ball.distance(paddle_r) < 50 and ball.xcor() > 350 or ball.distance(paddle_l) < 50 and ball.xcor() < -350:
        ball.bounce(x=True)
        
    if ball.xcor() > 390:
        print("Left player won!")
        time.sleep(1)
        ball.reset_position()
       
    if ball.xcor() < -400:
        print("Right player won!")
        time.sleep(1)
        ball.reset_position()
        
# #Y Up --> Down
#     if ball.ycor() >= 290:
#         ball_y = -6
        
# #X Right --> Left
#     if ball.xcor() >= 390:
#         ball_x = -6

# #Y Down --> Up
#     if ball.ycor() <= -290:
#         ball_y = 6

# #X Left --> Right 
#     if ball.xcor() <= -390:
#         ball_x = 6
    
    

        


screen.exitonclick()