from turtle import Turtle, Screen 
from paddle import Paddle
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up, "Right")
screen.onkey(paddle_r.go_down, "Left")
screen.onkey(paddle_l.go_up, "d")
screen.onkey(paddle_l.go_down, "a")   
    
game_is_on = True   
# ball_x = -6
# ball_y = -6
while game_is_on:
    time.sleep(ball.ball_speed)

    ball.move(ball.x_move, ball.y_move) 
    
    screen.update()

    # Detect collision with wall - Y
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(x=False)
        

    # Detect collision with wall - X
    if ball.xcor() > 390:
        print("Left player won!")
        scoreboard.score_change("left")
        ball.reset_position()
    elif ball.xcor() < -400:
        print("Right player won!")
        scoreboard.score_change("right")
        # print(scoreboard.l_score)
        # time.sleep(0.5)
        ball.reset_position()
        
        
    # Detect collision with paddle    
    if ball.distance(paddle_r) < 50 and ball.xcor() > 350 or ball.distance(paddle_l) < 50 and ball.xcor() < -350:
        ball.bounce(x=True)
        ball.ball_speed_update()
        
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
    
screen.mainloop()

# screen.exitonclick()