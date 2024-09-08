import tkinter as tk

root = tk.Tk()

root.title('Новый проект')

label = tk.Label(root, text='Привет, мир!')
label.pack()

button = tk.Button(root, text='Нажми меня', command=lambda: print('Кнопка нажата!'))
button.pack()

entry = tk.Entry(root)
entry.pack()

def print_text():
    print(entry.get())


root.mainloop()
