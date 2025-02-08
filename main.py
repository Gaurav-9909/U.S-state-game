import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):     #Getting the x,y coordinates of the states when you click mouse
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()





data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    user_enter = screen.textinput(title=f'{len(guessed_state)}/50 State Correct',
                                  prompt="What's the state name?").title()
    if user_enter == 'Exit':

        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if user_enter in all_states:
        guessed_state.append(user_enter)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_enter]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_enter)

screen.exitonclick()