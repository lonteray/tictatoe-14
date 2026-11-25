from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x500')
root.title('Хрестики-нулики')
root.configure(bg='#fac166')
is_crosses_turn = True # перший хід хрестиків
is_game_over = False
#messagebox.showinfo('Діалогове вікно', 'Привіт!')

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
    global is_game_over
    if is_game_over:
        return
    is_draw = True
    for row_index in range(3):
        for column_index in range(3):
            if points[row_index][column_index] == 0:
                is_draw = False
                break
    if is_draw:
        is_game_over = True
        messagebox.showinfo('Гру скінчено', 'Нічия')

def check_points():
    check_points_for_win((0, 0), (0, 1), (0, 2)) # 1 рядок
    check_points_for_win((1, 0), (1, 1), (1, 2)) # 2 рядок
    check_points_for_win((2, 0), (2, 1), (2, 2)) # 3 рядок

    check_points_for_win((0, 0), (1, 0), (2, 0))
    check_points_for_win((0, 1), (1, 1), (2, 1))
    check_points_for_win((0, 2), (1, 2), (2, 2))

    check_points_for_win((0, 0), (1, 1), (2, 2))
    check_points_for_win((0, 2), (1, 1), (2, 0))

def check_points_for_win(pos1, pos2, pos3):
    global is_game_over

    if is_game_over:
        return

    p1 = points[pos1[0]][pos1[1]]
    p2 = points[pos2[0]][pos2[1]]
    p3 = points[pos3[0]][pos3[1]]

    sum = p1 + p2 + p3

    if sum == 3 or sum == -3:
        is_game_over = True

        buttons[pos1[0]][pos1[1]].configure(
            bg='green', state='normal')
        buttons[pos2[0]][pos2[1]].configure(
            bg='green', state='normal')
        buttons[pos3[0]][pos3[1]].configure(
            bg='green', state='normal')

        if sum == 3:
            messagebox.showinfo('Перемога!', 'Хрестики перемогли!')
        else:
            messagebox.showinfo('Перемога!', 'Нулики перемогли!')

points = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

buttons = []
for row_index in range(3):
    row = []
    for column_index in range(3):
        button = Button(width=10, height=4)
        button.grid(row=row_index, column=column_index, padx=20, pady=20)
        button.bind('<Button-1>', on_button_click)
        button.row_index = row_index
        button.column_index = column_index
        row.append(button)
    buttons.append(row)
    

root.mainloop()
