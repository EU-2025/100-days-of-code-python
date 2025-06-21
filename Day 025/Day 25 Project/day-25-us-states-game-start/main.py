import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_states = pandas.read_csv("50_states.csv")
states_list = data_states["state"].to_list()

states_guessed = []
states_to_learn = []
t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
t.penup()

# Write text at turtle's position

game_is_on = True
while(game_is_on):
    if len(states_guessed) == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?").title()
    else:
        answer_state = screen.textinput(title=f"States correct {len(states_guessed)}/{len(states_list)}", prompt="What's another state's name?").title()
        if answer_state in states_guessed:
            continue
    
    if answer_state == "Exit":
        for st in states_list:
            if st not in states_guessed:
                states_to_learn.append(st)
        states_left = {
            "state" : states_to_learn
        }
        df_left = pandas.DataFrame(states_left)
        df_left.to_csv("states_left.csv")
        break
    
    if answer_state in states_list:
        states_guessed.append(answer_state)
        state_data = data_states[data_states.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.pendown()
        t.write(answer_state, align="center", font=("Courier", 10, "bold"))
        t.penup()
    if len(states_guessed) == 50:
        game_is_on = False
        t.goto(0,290)
        t.write(f"Congrats! You completed the {len(states_guessed)} states", align="center", font=("Courier", 20, "bold"))

screen.mainloop()