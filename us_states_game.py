import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("U.S States game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("50_states.csv")
states_df=pd.DataFrame(data)
score=0
guessed_states=[]
states_list=states_df["state"].to_list()
is_game_on=True
while score<50 and is_game_on:
    user=screen.textinput(title="guess the city", prompt=f"{score} out of 50 states guessed").title()
    if user=="Exit":
        is_game_on=False
    for i in range(len(states_list)):
        if user==states_list[i] and user not in guessed_states:
            guessed_states.append(user)
            score+=1
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data=data[data.state==user]
            t.goto(int(state_data.x),int(state_data.y))
            t.write(user)





























screen.exitonclick()
