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
        # self.direction = "DownRight"
        
    def move(self, x, y):
        new_x = self.xcor() + x
        new_y = self.ycor() + y
        self.goto(new_x, new_y)
        print(x,y)
            