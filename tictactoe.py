from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x500')
root.title('Хрестики-нулики')
root.configure(bg='grey')
is_crosses_turn = True # перший хід хрестиків
#messagebox.showinfo('Діалогове вікно', 'Привіт!')

def on_button_click(event):
    global is_crosses_turn
    button = event.widget
    if button['state'] == 'disabled':
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

def check_points_for_win(p1, p2, p3):
    sum = p1 + p2 + p3
    if sum == 3:
        messagebox.showinfo('Перемога!',
                            'Хрестики перемогли!')
    if sum == -3:
        messagebox.showinfo('Перемога!',
                            'Нулики перемогли!')

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
