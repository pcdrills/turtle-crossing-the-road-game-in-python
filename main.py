import time
from turtle import Screen, onkey
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    #Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            print("A hit")
            scoreboard.game_over()
            game_is_on = False
            
    #Detect a successful Crossing
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.level_up()
        
screen.exitonclick()
            