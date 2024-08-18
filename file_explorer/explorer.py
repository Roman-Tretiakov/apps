import tkinter as tk
from tkinter import filedialog as fd
import os


def file_select():
    filename = fd.askopenfilename(initialdir='/',
                                  title='Выберите файл', filetypes=(('Текстовый файл', '.txt'), ('EXE файл', '.exe'),
                                                                    ('Все файлы', '*')))
    text['text'] = 'Файл'
    text['text'] += '\n' + filename
    os.startfile(filename)
    #window.destroy()


window = tk.Tk()
window.title('Проводник')
window.geometry('350x150')
window.configure(background='black')
window.resizable(False, False)

# Configure grid to expand widgets
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure([0, 1], weight=1)

text = tk.Label(window, text='Файл:', width=65, height=5, background='silver', foreground='blue')
text.grid(column=0, row=1, sticky="nsew")

button_select = tk.Button(window, text='Выбрать файл', width=20, height=3,
                          background='silver', foreground='blue', command=file_select)
button_select.grid(column=0, row=2, padx=1, pady=5, ipadx=1, ipady=1)

window.mainloop()
