from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#6B4F4F")
        self.penup()
        self.goto(-270,255)
        self.level = 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-80,0)
        self.write("GAME OVER", font=FONT)

    def level_up(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

        
