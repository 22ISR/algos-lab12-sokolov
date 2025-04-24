from tkinter import *
from tkinter import ttk
from random import *

root = Tk()
root.title("Генератор паролей")
root.geometry("300x250")

# Массив с буквами
all_letters = [
    # Латинские буквы (строчные)
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    
    # Латинские буквы (заглавные)
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

 # Массив с Цифрами
all_number = [
    # Цифры
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
# Массив с спецсимволами
all_symbols = [
    # Специальные символы (основные)
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
]

# Массив с пробелом
all_spase = [
    # Пробел
    ' '
]


# ФУНКЦИОНАЛ

# Функционал "Количество цифр в пароле"

def number_in_password():
    print("Hello")

# Функционал "Добавить цифры"

def number_in_password():
    value = number.get()
    number.set(value + all_number)







# ИНТЕРФЕЙС 

# Количество цифр в пароле 
Spinbox = ttk.Spinbox(from_=1.0, to=100.0)
Spinbox.pack(anchor=N)

# Добавить цифры
number = IntVar() 

number_checkbutton = ttk.Checkbutton(text="Включить цифры", variable=number)
number_checkbutton.pack(padx=6, pady=6, anchor=NW)

# Добавить спецсимволы
symbol = IntVar() 

symbol_checkbutton = ttk.Checkbutton(text="Включить спецсимволы", variable=symbol)
symbol_checkbutton.pack(padx=6, pady=6, anchor=NW)

# Добавить пробелы
space = IntVar() 

space_checkbutton = ttk.Checkbutton(text="Включать пробелы", variable=space)
space_checkbutton.pack(padx=6, pady=6, anchor=NW)

#Кнопка генерации
generation = ttk.Button(text="Сгенерировать")
generation.pack()

#Поле вывода пароля
field = ttk.Entry()
field.pack(padx=8, pady=8)








root.mainloop()
