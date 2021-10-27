import pandas
from turtle import Turtle, Screen
import time
from scoreboard import Score

IMG_PATH = "blank_states_img.gif"
SPEED = 0.1

screen = Screen()
screen.setup(width=800, height=500)
screen.bgpic(IMG_PATH)
screen.title("U.S. States Game")
screen.tracer(0)
screen.delay(25)

# method to discover click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

score = Score()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

correct_answers = []
while len(correct_answers) < 50:
    screen.update()
    time.sleep(SPEED)

    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct ",
                                    prompt="What's another state's name?").title().strip()

    state_data = data[data.state == answer_state]
    number_states = data.state.count()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_answers]
        # for state in all_states:
        #     if state not in correct_answers:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states_file.csv")
        select_state = Turtle()
        select_state.penup()
        select_state.hideturtle()

        for state in missing_states:
            missing_data_state = data[data.state == state]
            if state in all_states:
                select_state.goto(missing_data_state["x"].values[0], int(missing_data_state.y))
                select_state.write(state)

    if answer_state in all_states and answer_state not in correct_answers:
        score.increase_score()
        correct_answers.append(answer_state)
        select_state = Turtle()
        select_state.penup()
        select_state.hideturtle()
        select_state.goto(state_data["x"].values[0], int(state_data.y))
        select_state.write(answer_state)



