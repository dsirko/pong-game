from turtle import Turtle
# from main import ball_speed_update
import random

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.x_move = 6
        self.y_move = 6
        self.ball_speed = 0.05
        # self.x_move = 6
        # self.y_move = 0
        
    def move(self, x_move, y_move):
        new_x = self.xcor() + x_move
        new_y = self.ycor() + y_move
        self.goto(new_x, new_y)
        # print(new_x, new_y)
        
    def bounce(self,x):
        if x == True:
            self.x_move *= -1            
        else:
            self.y_move *= -1

        
    # def rand_shot(self):
    #     the_cord = random(-6, 6)
    #     return the_cord
    def rand_shot(self):
        ranges = [(-10, -2), (2, 10)]
        # x_range = random.choice(ranges)
        y_range = random.choice(ranges)
        # self.x_move = random.randint(x_range[0], x_range[1])
        self.y_move = random.randint(y_range[0], y_range[1])
        print(f"y_move: {self.y_move} x_move: {self.x_move}")
        
    
    def reset_position(self):
        self.rand_shot()
        self.bounce(x=True)
        self.goto(1,1)
        self.ball_speed = 0.05
        
    
    def ball_speed_update(self):
        if self.ball_speed > 0.01:
            self.ball_speed -= 0.01
            print(self.ball_speed)
        else:
            self.ball_speed = 0.01
        print(f"ball_speed: {self.ball_speed}")
        
            