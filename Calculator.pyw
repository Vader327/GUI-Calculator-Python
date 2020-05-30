import tkinter as tk
from tkinter import messagebox
import math

window = tk.Tk()
window.geometry("237x160")
window.title("Calculator")
window.resizable(False, False)

expression = ""
mystring = tk.StringVar(window)

def do_num(num):
    global expression
    expression = expression + str(num)
    mystring.set(expression)

def clear():
    global expression
    expression = ""
    mystring.set(expression)

def backspace():
    global expression
    expression = expression[:-1]
    mystring.set(expression)

def root():
    global expression
    try:
        result = math.sqrt(int(expression))
        if result==round(result):
            expression = str(round(result))
            mystring.set(expression)
        else:
            expression = str(result)
            mystring.set(expression)
    except Exception:
        result = math.sqrt(int(eval(expression)))
        if result==round(result):
            expression = str(round(result))
            mystring.set(expression)
        else:
            expression = str(result)
            mystring.set(expression)
    
def getvalue():
    try:
        global expression
        result = (eval(mystring.get()))
        if result == round(result):
            expression = str(round(result))
            mystring.set(expression)
        else:
            expression = str(result)
            mystring.set(expression)
        
    except Exception as e:
        tk.messagebox.showerror(title="Error", message="Invalid Input")

box = tk.Entry(window, width = 38, textvariable = mystring).place(x = 3, y = 2)

eval_button = tk.Button(width = 25, text = "Evaluate", command = getvalue).place(x = 2, y = 132)

button1 = tk.Button(width = 5, text = "1", command = lambda: do_num(1)).place(x = 2, y = 24)
button2 = tk.Button(width = 5, text = "2", command = lambda: do_num(2)).place(x = 49, y = 24)
button3 = tk.Button(width = 5, text = "3", command = lambda: do_num(3)).place(x = 96, y = 24)
button4 = tk.Button(width = 5, text = "4", command = lambda: do_num(4)).place(x = 2, y = 51)
button5 = tk.Button(width = 5, text = "5", command = lambda: do_num(5)).place(x = 49, y = 51)
button6 = tk.Button(width = 5, text = "6", command = lambda: do_num(6)).place(x = 96, y = 51)
button7 = tk.Button(width = 5, text = "7", command = lambda: do_num(7)).place(x = 2, y = 78)
button8 = tk.Button(width = 5, text = "8", command = lambda: do_num(8)).place(x = 49, y = 78)
button9 = tk.Button(width = 5, text = "9", command = lambda: do_num(9)).place(x = 96, y = 78)
button0 = tk.Button(width = 5, text = "0", command = lambda: do_num(0)).place(x = 49, y = 105)

button_clear = tk.Button(width = 5, text = "Clear", command = clear).place(x = 2, y = 105)
button_back = tk.Button(width = 5, text = "←", command = backspace).place(x = 190, y = 24)
button_decimal = tk.Button(width = 5, text = ".", command = lambda: do_num('.')).place(x = 96, y = 105)
button_plus = tk.Button(width = 5, text = "+", command = lambda: do_num('+')).place(x = 143, y = 24)
button_minus = tk.Button(width = 5, text = "-", command = lambda: do_num('-')).place(x = 143, y = 51)
button_multiply = tk.Button(width = 5, text = "*", command = lambda: do_num('*')).place(x = 143, y = 78)
button_divide = tk.Button(width = 5, text = "/", command = lambda: do_num('/')).place(x = 143, y = 105)
button_open_bracket = tk.Button(width = 5, text = "(", command = lambda: do_num("(")).place(x = 190, y = 51)
button_close_bracket = tk.Button(width = 5, text = ")", command = lambda: do_num(")")).place(x = 190, y = 78)
button_exponent = tk.Button(width = 5, text = "xⁿ", command = lambda: do_num("**")).place(x = 190, y = 105)
button_root = tk.Button(width = 5, text = "²√", command = lambda: root()).place(x = 190, y = 132)

window.mainloop()
