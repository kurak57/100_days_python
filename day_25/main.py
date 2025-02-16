import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./50_states.csv")
states = data.state.to_list()

correct_answer = []
game_on = True

while game_on:
    if len(correct_answer) == 0:
        answer_state = screen.textinput("Guess the State", "What's state's name?").title()
    else:
        answer_state = screen.textinput(f"{len(correct_answer)}/{len(states)} States Correct", "What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_answer]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_need_to_learn.csv")
        break
    
    if answer_state not in correct_answer:
        if answer_state in states:
            correct_answer.append(answer_state)
            state = data[data.state == answer_state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(state.x.item(), state.y.item())
            t.write(answer_state,False,"center",("Arial",8,"normal"))

    if len(correct_answer) == len(states):
        game_on = False
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.write("You've Completed It!!!",False,"center",("Arial",16,"bold"))
