import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINAL_LEVEL = 2

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = CarManager()
screen.listen()
screen.onkey(player.go_up,"Up")
car = CarManager()
game_is_on = True


time.sleep(0.1)
screen.update()
while game_is_on:
    cars.create_car()
    cars.move_cars()
            
    for car in cars.all_cars:
        if abs(car.xcor() - player.xcor()) < 25  and abs(car.ycor() - player.ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.ycor()>=280:
        if scoreboard.level == FINAL_LEVEL:
            game_is_on = False
            scoreboard.you_win()
            break
        else:
            player.restart_game()
            
        if scoreboard.level < FINAL_LEVEL:
            scoreboard.update_level()
            cars.update_speed()
    
    
    time.sleep(0.1)
    screen.update()
screen.exitonclick()