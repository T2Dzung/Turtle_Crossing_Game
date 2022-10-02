from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#483434")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        if self.ycor()<280:
            self.goto(0, self.ycor()+MOVE_DISTANCE)

    def down(self):
        if self.ycor()>-280:
            self.goto(0, self.ycor()-MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)
