#Assignment_6:Calculator using the Tkinter

#step 1: installing
import tkinter as tk

#Global variables

display_var = None
first_num = None
operator = None

# functions

def button_click(number):
    current = display_var.get()
    if number == '.' and '.' in current:
        return
    display_var.set(current + str(number))

def button_clear():
    display_var.set("")
    global first_num, operator
    first_num = None
    operator = None

def button_operation(op):
    global first_num, operator
    try:
        first_num = float(display_var.get())
        operator = op
        display_var.set("")
    except ValueError:
        display_var.set("Error")
        first_num = None
        operator = None

def button_equals():
    global first_num, operator
    try:
        second_num = float(display_var.get())
        display_var.set("")

        if first_num is not None and operator is not None:
            result = 0
            if operator == '+':
                result = first_num + second_num
            elif operator == '-':
                result = first_num - second_num
            elif operator == '*':
                result = first_num * second_num
            elif operator == '/':
                if second_num == 0:
                    display_var.set("Error: Div by zero")
                    return
                result = first_num / second_num

            if result == int(result):
                display_var.set(str(int(result)))
            else:
                display_var.set(str(result))

            first_num = None
            operator = None
        else:
            display_var.set(second_num)
    except ValueError:
        display_var.set("Error")
    except Exception as e:
        display_var.set(f"Error: {e}")
    finally:
        first_num = None
        operator = None

#step 2: gui interaction

root = tk.Tk()
root.title("Calculator:1.0")
root.geometry('300x400')

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

display_var = tk.StringVar()
e = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 16), justify='right', textvariable=display_var)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

#step 3: inputs

#Buttons

buttons_data = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3, 'operator'),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3, 'operator'),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3, 'operator'),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2, 'operator_long'),
    ('C', 5, 0, 'clear'), ('=', 5, 1, 'equals')
]

buttons_font = ('Arial', 14)

for item_data in buttons_data:
    button_text = item_data[0]
    r = item_data[1]
    c = item_data[2]
    button_type = item_data[3] if len(item_data) > 3 else 'number'

    command_func = None
    column_span = 1

    if button_type == 'clear':
        command_func = button_clear
    elif button_type == 'equals':
        command_func = button_equals
        column_span = 3
    elif button_type == 'operator':
        command_func = lambda op=button_text: button_operation(op)
    elif button_type == 'operator_long':
        command_func = lambda op=button_text: button_operation(op)
        column_span = 2
    else:
        command_func = lambda num=button_text: button_click(num)

    btn = tk.Button(root, text=button_text, font=buttons_font, padx=20, pady=20, command=command_func)
    btn.grid(row=r, column=c, columnspan= column_span, padx=5, pady=5, sticky="nsew"  )

#Mainloop
root.mainloop()
