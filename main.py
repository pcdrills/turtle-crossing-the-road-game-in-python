import time
from turtle import Screen, onkey
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from beautiful_borders import BeautifulBorders

screen = Screen()
screen.title("Turtle Crossing Game by PC Drills --- github= @pcdrills")
screen.setup(width=600, height=600)
screen.tracer(0)
user = screen.textinput("Game Guide", 
                        "You can only use -Up Arrow- key. -> Enable your turtle to successfully cross the road"
                        " \nAvoid hitting any rectangular objects. \n"
                        " Hit round objects to get points\n When ready, input your gamer name below and click ok")
if len(user) <= 0:
    user = "N/A"

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard(gamer=user)
beautiful_boarders = BeautifulBorders()

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
            
    #Detect collision with special cars for points
    for point_car in car_manager.point_cars:
        if point_car.distance(player) < 20:
            scoreboard.increase_points()
            print("A Point")
            break
            
    #Detect a successful Crossing
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.level_up()
        
screen.exitonclick()
            