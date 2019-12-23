# это пакеты Python для работы с библиотекой (графический интерфейс)
from tkinter import *
from decimal import *


# в данной функции выбирается число и действие, которое с ним производится 
import math
def calculate(stack):
    ''' в данной функции выбирается число и действие, которое с ним производится '''

    result = 0
    # print(stack)
    if len(stack) > 2:
        operand2 = Decimal(stack.pop())
        operation = stack.pop()
        operand1 = Decimal(stack.pop())
        if operation == '+':
            result = operand1 + operand2
        if operation == '-':
            result = operand1 - operand2
        if operation == '/':
            result = operand1 / operand2
        if operation == '*':
            result = operand1 * operand2

    elif len(stack) == 2:
        operation = stack.pop()
        operand = Decimal(stack.pop())
        if operation == 'log10':
            result = math.log10(operand)
        if operation == '^3':
            result = operand * operand * operand
        if operation == '^2':
            result = operand * operand
                    
        # в операциях sin cos tan используются радианы
        if operation == 'sin':
            result = math.sin(operand)
        if operation == 'cos':
            result = math.cos(operand)
        if operation == 'tan':
            result = math.tan(operand)
    else:
        return Decimal(stack.pop())
    return result

unary = ('log10', '^3', '^2', 'sin', 'cos', 'tan')
# функция обработки нажимаемой клавиши
def click(text):
    '''функция обработки нажимаемой клавиши'''
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif activeStr != 'Error':
        if '0' <= text <= '9':
            activeStr += text
            label.configure(text=activeStr)
        elif text == '.':
            if activeStr.find('.') == -1:
                activeStr += text
                label.configure(text=activeStr)
        elif text ==' ':
            pass
        else:
            stack.append(label['text'])
            if text in unary:
                stack.append(text)
            if text == '=' or len(stack) > 2 or text in unary:
                value = calculate(stack)
                label.configure(text=value)
                stack.clear()
                if text !=  '=' and not text in unary:
                    stack.append(str(value))
                    stack.append(text)
                activeStr = ''
            else:
                stack.append(text)
                activeStr = ''
                
if __name__ == '__main__':
    
    # создаем окно с надписью "Калькулятор"
    root = Tk()
    root.title('Calculator')
    
    # создание кнопок для калькулятора
    buttons = (('7', '8', '9', '/', '6'),
               ('4', '5', '6', '*', '6'),
               ('1', '2', '3', '-', '6'),
               ('0', '.', '=', '+', '6'),
               ('log10', '^3', '^2', ' '),
               )
    
    # в stack вводим числа и операции, а activeStr предназначен для хранения набираемого числа
    activeStr = ''
    stack = []
                   
            
    # внешний вид
    label = Label(root, text='0', width=45)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")
    
    button = Button(root, text='CE', command=lambda text='CE': click(text))
    button.grid(row=1, column=3, sticky="nsew")
    for row in range(5):
        for col in range(4):
            button = Button(root, text=buttons[row][col],
                    command=lambda row=row, col=col: click(buttons[row][col]))
            button.grid(row=row + 2, column=col, sticky="nsew")
    
    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(4, weight=1)
    
    root.mainloop()
    









# lambda - функция без имени (использовали ее, чтобы каждая кнопка правильно работала)