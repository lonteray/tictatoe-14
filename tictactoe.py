from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x500')
root.title('Хрестики-нулики')
root.configure(bg='#fac166')

is_crosses_turn = True
is_game_over = False

x_wins = 0
o_wins = 0
draws = 0

score_label = Label(
    root,
    text="X: 0 | O: 0 | Нічиї: 0",
    font=("Arial", 14)
)
score_label.grid(row=5, column=0, columnspan=3)


def on_button_click(event):
    global is_crosses_turn

    button = event.widget

    if button['state'] == 'disabled' or is_game_over:
        return

    if is_crosses_turn:
        button.configure(text='x')
        row_index = button.row_index
        column_index = button.column_index
        points[row_index][column_index] = 1
    else:
        button.configure(text='o')
        row_index = button.row_index
        column_index = button.column_index
        points[row_index][column_index] = -1

    is_crosses_turn = not is_crosses_turn
    button['state'] = 'disabled'

    check_points()
    check_for_draw()


def check_for_draw():
    global is_game_over, draws

    if is_game_over:
        return

    is_draw = True

    for row_index in range(3):
        for column_index in range(3):
            if points[row_index][column_index] == 0:
                is_draw = False
                break

    if is_draw:
        draws += 1
        is_game_over = True

        score_label.config(
            text=f"X: {x_wins} | O: {o_wins} | Нічиї: {draws}"
        )

        messagebox.showinfo('Гру скінчено', 'Нічия')


def check_points():
    check_points_for_win(
        points[0][0], points[0][1], points[0][2]) #1р
    if is_game_over:
        return

    check_points_for_win(
        points[1][0], points[1][1], points[1][2]) #2р
    if is_game_over:
        return

    check_points_for_win(
        points[2][0], points[2][1], points[2][2]) #3р
    if is_game_over:
        return

    check_points_for_win(
        points[0][0], points[1][0], points[2][0])
    if is_game_over:
        return

    check_points_for_win(
        points[0][1], points[1][1], points[2][1])
    if is_game_over:
        return

    check_points_for_win(
        points[0][2], points[1][2], points[2][2])
    if is_game_over:
        return

    check_points_for_win(
        points[0][0], points[1][1], points[2][2])
    if is_game_over:
        return

    check_points_for_win(
        points[0][2], points[1][1], points[2][0])


def check_points_for_win(p1, p2, p3):
    global is_game_over, x_wins, o_wins

    sum = p1 + p2 + p3

    if sum == 3:
        x_wins += 1
        is_game_over = True

        score_label.config(
            text=f"X: {x_wins} | O: {o_wins} | Нічиї: {draws}"
        )

        messagebox.showinfo(
            'Перемога!',
            'Хрестики перемогли!'
        )

    if sum == -3:
        o_wins += 1
        is_game_over = True

        score_label.config(
            text=f"X: {x_wins} | O: {o_wins} | Нічиї: {draws}"
        )

        messagebox.showinfo(
            'Перемога!',
            'Нулики перемогли!'
        )


points = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

buttons = []

for row_index in range(3):
    row = []

    for column_index in range(3):
        button = Button(width=10, height=4, bg="blue")
        button.grid(
            row=row_index,
            column=column_index,
            padx=20,
            pady=20
        )

        button.bind('<Button-1>', on_button_click)
        button.row_index = row_index
        button.column_index = column_index

        row.append(button)

    buttons.append(row)


root.mainloop()
