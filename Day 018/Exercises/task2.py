from turtle import Turtle, Screen

tortuga = Turtle()
screen = Screen()

tortuga.shape("turtle")
tortuga.color("blue")

# lados = 4
# total = 0
# angulo = 90
# distancia = 100
# while total < lados:
#     tortuga.forward(distancia)
#     tortuga.right(angulo)
#     total+=1
# tortuga.forward(distancia)

for _ in range(4):
    tortuga.forward(100)
    tortuga.right(90)

screen.exitonclick()
