from turtle import Turtle
import random

#colors used to produce the cars, move distances for both the cars and the speed increment
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.point_cars = []
      
    def create_car(self):
        random_chance = random.randint(1, 6)
        #Produce cars without points (obstacle cars)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)
        
        #Produce cars with points (fruitful cars)
        if random_chance == 2:
            point_car = Turtle("circle")
            point_car.penup()
            point_car.shapesize(stretch_wid=1, stretch_len=2)
            point_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            point_car.goto(300, random_y)
            point_car.setheading(180)
            self.point_cars.append(point_car)
                
    #Move all the cars
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
        for point_car in self.point_cars:
            point_car.forward(self.car_speed)
    
    #Increase the speed of the cars when the level adds up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
