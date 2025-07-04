from turtle import Turtle
import random as rd
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.turtle_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = rd.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(rd.choice(COLORS))
            random_y = rd.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.turtle_speed)
            
    def update_speed(self):
        self.turtle_speed += MOVE_INCREMENT

