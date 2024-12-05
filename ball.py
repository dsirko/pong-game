from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        
    def move(self):
        new_x = self.ycor() + 1
        new_y = self.xcor() + 1
        self.goto(new_x, new_y)