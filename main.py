import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("360x430")
root.resizable(0, 0)

input_text = tk.StringVar()

entry = tk.Entry(root, textvariable=input_text, font=('Arial', 18), justify='right', bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)

def click_button(item):
    current_text = input_text.get()
    input_text.set(current_text + str(item))

def clear_input():
    input_text.set("")

def evaluate_expression():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except Exception as e:
        input_text.set("Error")

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in range(1, 5):
    for col, button in enumerate(buttons[row-1]):
        if button == 'C':
            btn = tk.Button(root, text=button, font=('Arial', 18), fg='red', width=5, height=2,
                            command=clear_input)
        elif button == '=':
            btn = tk.Button(root, text=button, font=('Arial', 18), fg='green', width=5, height=2,
                            command=evaluate_expression)
        else:
            btn = tk.Button(root, text=button, font=('Arial', 18), width=5, height=2,
                            command=lambda button_value=button: click_button(button_value))
        
        btn.grid(row=row, column=col, padx=5, pady=5)


root.mainloop()