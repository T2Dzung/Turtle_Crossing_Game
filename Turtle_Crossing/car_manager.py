import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.init_car()
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE

    def init_car(self):
        num = random.randint(10, 15)
        for _ in range(num):
            car = Turtle("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(random.randint(-200, 300), random.randint(-220, 250))
            self.cars.append(car)

    def next_car(self):
        num = random.randint(1, 3)
        for _ in range(num):
            car = Turtle("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-220, 250))
            self.cars.append(car)

    def move(self):
        for i in range(len(self.cars)):
            self.cars[i].goto(self.cars[i].xcor()-self.speed, self.cars[i].ycor())
        if self.cars[len(self.cars)-1].xcor() <= 260:
            self.next_car()

    def speedup(self):
        self.speed += MOVE_INCREMENT
        