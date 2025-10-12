import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()
    # Detect turtle collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False
    # Detect whether turtle completes a level
    if player.check_reach():
        car_manager.increase_speed()
        scoreboard.level_update()

screen.exitonclick()
