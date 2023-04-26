from tkinter import *
win = Tk()
win.title('calculator')
win.geometry('515x365')
win.resizable(0, 0)

expression = ""
input_text = StringVar()

def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#function to clear Input field
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# function Equal button
def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""



#Input field frame.
input_frame = Frame(win, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), width=45, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0)

#Increase the height of the input field
input_field.pack(ipady=10)

#Button frame.
buttons_frame = Frame(win, width=310, height=270)
buttons_frame.pack()

clear = Button(buttons_frame, text='C', width=36, height=3, command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(buttons_frame, text='/', width=10, height=3, command=lambda: button_click('/')).grid(row=0, column=3, padx=1, pady=1)

#Button Second Row
seven = Button(buttons_frame, text='7', width=10, height=3, command=lambda: button_click(7) ).grid(row=1, column=0, padx=1, pady=1)
eight = Button(buttons_frame, text='8', width=10, height=3, command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(buttons_frame, text='9', width=10, height=3, command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(buttons_frame, text='*', width=10, height=3, command=lambda: button_click('*')).grid(row=1, column=3, padx=1, pady=1)

#Button Third Row
four = Button(buttons_frame, text='4', width=10, height=3, command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(buttons_frame, text='5', width=10, height=3, command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(buttons_frame, text='6', width=10, height=3, command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(buttons_frame, text='-', width=10, height=3, command=lambda: button_click('-')).grid(row=2, column=3, padx=1, pady=1)

#Button Forth Row
one = Button(buttons_frame, text='1', width=10, height=3, command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(buttons_frame, text='2', width=10, height=3, command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(buttons_frame, text='3', width=10, height=3, command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(buttons_frame, text='+', width=10, height=3, command=lambda: button_click('+')).grid(row=3, column=3, padx=1, pady=1)

#Button Fifth Row
zero = Button(buttons_frame, text='0', width=24, height=3, command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(buttons_frame, text='.', width=10, height=3, command=lambda: button_click('.')).grid(row=4, column=2, padx=1, pady=1)
equal = Button(buttons_frame, text='=', width=10, height=3, command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)
win.mainloop()

