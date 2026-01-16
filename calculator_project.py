# from tkinter import  *


# window.geometry("500x500")
# window.title("Calculator GUI")


# icon = PhotoImage(file='calc_image123.png')
# window.iconphoto(True, icon)
# window.configure(background="lightblue")

# label = Label(window,)

# window.mainloop()


# root = Tk()
# root.title("Calculator")
# root.geometry("400x500")

# # Create the display
# display = Entry(root, width=35, borderwidth=5)
# display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# # Define button click function
# def button_click(number):
#     current = display.get()
#     display.delete(0, END)
#     display.insert(0, str(current) + str(number))

# # Define clear function
# def button_clear():
#     display.delete(0, END)

# # Define add function
# def button_add():
#     first_number = display.get()
#     global f_num
#     global math_operation
#     math_operation = "addition"
#     f_num = int(first_number)
#     display.delete(0, END)

# # Define equal function
# def button_equal():
#     second_number = display.get()
#     display.delete(0, END)
    
#     if math_operation == "addition":
#         display.insert(0, f_num + int(second_number))

# # Create buttons
# button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
# button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
# button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
# button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
# button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
# button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
# button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
# button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
# button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
# button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
# button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
# button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
# button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)




# import tkinter as tk

# # Create window
# window = tk.Tk()
# window.title("Calculator")
# window.geometry("300x400")
# window.resizable(False, False)

# # Variable to store what the user types
# text = ""

# # Function when a button is clicked
# def click(value):
#     global text
#     text = text + str(value)
#     screen.set(text)

# # Function to clear screen
# def clear():
#     global text
#     text = ""
#     screen.set("")

# # Function to calculate result
# def equal():
#     global text
#     try:
#         answer = eval(text)
#         screen.set(answer)
#         text = str(answer)
#     except:
#         screen.set("Error")
#         text = ""

# # Screen
# screen = tk.StringVar()
# entry = tk.Entry(window, textvariable=screen, font=("Arial", 18), justify="right")
# entry.pack(fill="x", padx=10, pady=10)

# # Buttons frame
# frame = tk.Frame(window)
# frame.pack()

# buttons = [
#     "7", "8", "9", "/",
#     "4", "5", "6", "*",
#     "1", "2", "3", "-",
#     "0", ".", "=", "+"
# ]

# row = 0
# col = 0

# for b in buttons:
#     if b == "=":
#         cmd = equal
#     else:
#         cmd = lambda x=b: click(x)

#     tk.Button(frame, text=b, width=5, height=2, command=cmd)\
#         .grid(row=row, column=col, padx=5, pady=5)

#     col += 1
#     if col == 4:
#         col = 0
#         row += 1

# # Clear button
# tk.Button(window, text="Clear", width=20, command=clear).pack(pady=10)

# window.mainloop()



import tkinter as tk

# Create window
window = tk.Tk()
window.title("Calculator App")

icon = tk.PhotoImage(file='calc_image123.png')
window.iconphoto(True, icon)

window.geometry("300x420")
window.resizable(False, False)
window.configure(bg="#f7c6d0")  # soft pink background

# Store user input
text = ""

# Button click
def click(value):
    global text
    text = text + str(value)
    screen.set(text)

# Clear screen
def clear():
    global text
    text = ""
    screen.set("")

# Calculate result
def equal():
    global text
    try:
        result = eval(text)
        screen.set(result)
        text = str(result)
    except:
        screen.set("Error")
        text = ""

title = tk.Label(
    window,
    text="♡ Simple Calculator ♡",
    font=("Segoe UI", 14),
    bg="#f7c6d0",
    fg="#4a2c2a"
)
title.pack(pady=5)


# Display screen
screen = tk.StringVar()
entry = tk.Entry(
    window,
    textvariable=screen,
    font=("Helvetica", 20),
    justify="right",
    bg="#fff0f5",   # light pink
    fg="#4a2c2a"
)
entry.pack(fill="x", padx=10, pady=15)

# Buttons frame
frame = tk.Frame(window, bg="#f7c6d0")
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for b in buttons:
    if b == "=":
        cmd = equal
        color = "#ff8fab"  # pink for equals
    else:
        cmd = lambda x=b: click(x)
        color = "#fce4ec"  # soft button color

    tk.Button(
        frame,
        text=b,
        width=5,
        height=2,
        font=("Arial", 12),
        bg=color,
        fg="#4a2c2a",
        relief="flat",
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        col = 0
        row += 1

# Clear button
tk.Button(
    window,
    text="Clear",
    width=20,
    font=("Arial", 12),
    bg="#f48fb1",
    fg="white",
    command=clear
).pack(pady=10)

window.mainloop()
