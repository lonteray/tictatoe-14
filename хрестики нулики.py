from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x500')
root.title('Хрестики-Нуликиє')
root.configure(bg='grey')
is_crosses_turn = True
#messagebox.showinfo('Нотація', 'Надоїло')

def on_button_click(event):
    global is_crosses_turn
    button = event.widget
    if button['state'] == 'disabled':
        return
    if is_crosses_turn:
        button.configure(text='X')
        row_index = button.row_index
        column_index = button.column_index
        points[row_index][column_index] = 1
    else:
        button.configure(text='O')
        row_index = button.row_index
        column_index = button.column_index
        points[row_index][column_index] = -1
    is_crosses_turn = not is_crosses_turn
    button['state'] = 'disabled'
    check_points()

def check_points():
    check_points_for_win(
        points[0][0], points[0][1], points[0][2])
    check_points_for_win(
        points[1][0], points[1][1], points[1][2])
    check_points_for_win(
        points[2][0], points[2][1], points[2][2])

    check_points_for_win(
        points[0][0], points[1][0], points[2][0])
    check_points_for_win(
        points[0][1], points[1][1], points[2][1])
    check_points_for_win(
        points[0][2], points[1][2], points[2][2])

    check_points_for_win(
        points[0][0], points[1][1], points[2][2])
    check_points_for_win(
        points[0][2], points[1][1], points[2][0])


def check_points_for_win(p1, p2, p3):
    sum = p1 + p2 + p3
    if sum == 3:
        messagebox.showinfo('перемога!','хрестики перемогли!')

    if sum == -3:
        messagebox.showinfo('перемога!','хрестики перемогли!')

points = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
buttons = []
for row_index in range (3):
    row = []
    points_row = []
    for column_index in range (3):
        button = Button(width=10, height=4)
        button.grid(row=row_index, column=column_index, padx=20, pady=20)
        button.bind('<Button-1>', on_button_click)
        button.row_index = row_index
        button.column_index = column_index
        row.append(button)
    buttons.append(row)

def reset_game():
    global points, is_crosses_turn, is_game_over

    is_crosses_turn = True
    is_game_over = False

    points[
        [0, 0, 0]
        [0, 0, 0]
        [0, 0, 0]
    ]

    for row in buttons:
        for button in row:
            button.configure(text='')
            button.configure(state='normal')

button_new_game = Button(root, text='Нова гра', command=reset_game)
button_new_game.grid(row=3, column=1, pady=10)


root.mainloop()
