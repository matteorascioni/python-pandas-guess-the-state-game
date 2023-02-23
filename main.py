#Enter this commands before run this program
#python3 -m venv venv
#pip3 install pandas
import turtle
import pandas

# General screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get the data from the csv's file
data = pandas.read_csv("50_states.csv")
# Selecting the state column inside the Dataframe
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    #prompt to the user 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        #check what's states the user miss in case there are append it to a new list and then create a new csv file with them
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        #New turlte object created to show the name of the state on the screen
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.speed("fastest")
        #Getting the coordinates
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
