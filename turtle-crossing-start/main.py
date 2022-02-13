import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key='Up',fun=player.go_forward)



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.cars_move_horizontal()

    #detect collision with finish line
    if player.ycor() >= FINISH_LINE_Y:
        player.finish_level()
        scoreboard.update_scoreboard()
        car_manager.car_pace_inc()

    #detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()
    


    screen.update()

screen.exitonclick()