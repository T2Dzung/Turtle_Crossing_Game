import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("#FFF3E4")
screen.tracer(0)

turtle = Player()
level = Scoreboard()
car = CarManager()

screen.listen()
screen.onkeypress(turtle.up, "Up")
screen.onkeypress(turtle.down, "Down")


game_on = 1
while game_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    if turtle.ycor() > 280:
        turtle.next_level()
        level.level_up()
        car.speedup()

    for i in car.cars:
        if turtle.distance(i) < 30 and abs(turtle.ycor() - i.ycor())<10:
            level.game_over()
            game_on = 0
            
        
screen.exitonclick()
       
