from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        
    def move(self):
        new_x = self.ycor() + 5
        new_y = self.xcor() + 5
        self.goto(new_x, new_y)
