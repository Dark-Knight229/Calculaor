from tkinter import * # Загружаем все компоненты библиотеки
import math


window = Tk() # Основное окно приложения
window.geometry("291x175") # Размер окна
window.title("Калькулятор") # Название окна
window.config(background='black') # Параметры окна

expression = "" # Выражение

result = StringVar() # Строго типизированный тип данных string
express_field = Entry(textvariable=result) # Поле для ввода, textvariable - значение берется для окошка
express_field.grid(columnspan=4, ipadx=83) # columnspan - сколько колонок займет строка; ipadx - сколько занимает одна колонка по x

def press_num(num):
    """Выводит на экран кнопку"""
    global expression # Кл. слово global дает доступ функции к переменной, которая за её пределами
    expression += str(num)
    result.set(expression) # Переменной result передаем значение

def equalpress():
    """Считает и выводит результат"""
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = total
    except:
        result.set("Error")
        expression = ""

def resturt():
    global expression
    expression = ""
    result.set(expression)


"""Создание кнопок"""
button1 = Button(text="1", height=1, width=9, command=lambda: press_num(1)) # Кнопка; в command вызываем нашу ф-цию press_num
button1.grid(row=2, column=0) # Закрепляем кнопку
button2 = Button(text="2", height=1, width=9, command=lambda: press_num(2))
button2.grid(row=2, column=1)
button3 = Button(text="3", height=1, width=9, command=lambda: press_num(3))
button3.grid(row=2, column=2)

button4 = Button(text="4", height=1, width=9, command=lambda: press_num(4)) 
button4.grid(row=3, column=0) 
button5 = Button(text="5", height=1, width=9, command=lambda: press_num(5))
button5.grid(row=3, column=1)
button6 = Button(text="6", height=1, width=9, command=lambda: press_num(6))
button6.grid(row=3, column=2)

button7 = Button(text="7", height=1, width=9, command=lambda: press_num(7)) 
button7.grid(row=4, column=0) 
button8 = Button(text="8", height=1, width=9, command=lambda: press_num(8))
button8.grid(row=4, column=1)
button9 = Button(text="9", height=1, width=9, command=lambda: press_num(9))
button9.grid(row=4, column=2)

minus = Button(text="-", height=1, width=9, command=lambda: press_num("-")) 
minus.grid(row=5, column=0) 
zero = Button(text="0", height=1, width=9, command=lambda: press_num(0))
zero.grid(row=5, column=1)
plus = Button(text="+", height=1, width=9, command=lambda: press_num("+"))
plus.grid(row=5, column=2)

equal = Button(text="=", height=1, width=9, command=equalpress)
equal.grid(row=6, column=1)
multipl = Button(text="*", height=1, width=9, command=lambda: press_num("*"))
multipl.grid(row=6, column=0)
div = Button(text = "/", height=1, width=9, command=lambda: press_num("/"))
div.grid(row=6, column=2)

delete = Button(text="C", height=1, width=9, command=resturt)
delete.grid(row=2, column=3)
lbrack = Button(text="(", height=1, width=4 ,command=lambda: press_num("("))
lbrack.place(x=218.6, y=45)
rbrack = Button(text=")", height=1, width=4, command=lambda: press_num(")"))
rbrack.place(x=256, y=45)

sqtr = Button(text="√", height=1, width=9, command=lambda: press_num("math.sqrt("))
sqtr.grid(row=4, column=3)
procent = Button(text="%", height=1, width=9, command=lambda: press_num("/100"))
procent.grid(row=5, column=3)
mod = Button(text="mod", height=1, width=9, command=lambda: press_num("%"))
mod.grid(row=6, column=3)

cos = Button(text="cos", height=1, width=9, command=lambda: press_num("math.cos("))
cos.grid(row=7, column=0)
sin = Button(text="sin", height=1, width=9, command=lambda: press_num("math.sin("))
sin.grid(row=7, column=1)
degree = Button(text="x^y", height=1, width=9, command=lambda: press_num("**"))
degree.grid(row=7, column=2)
pi = Button(text="π", height=1, width=9, command=lambda: press_num("math.pi"))
pi.grid(row=7, column=3)

window.mainloop() # Запуск программы
