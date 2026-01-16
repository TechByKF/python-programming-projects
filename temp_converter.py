import tkinter as tk

# Create window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("380x360")
window.resizable(False, False)
window.configure(bg="#f2f2f2")

# Function to convert temperature
def convert_temp():
    try:
        value = float(temp_entry.get())
        from_unit = from_choice.get()
        to_unit = to_choice.get()

        # Convert input to Celsius first
        if from_unit == "Celsius":
            celsius = value
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = value - 273.15

        # Convert Celsius to target unit
        if to_unit == "Celsius":
            result = celsius
        elif to_unit == "Fahrenheit":
            result = (celsius * 9/5) + 32
        elif to_unit == "Kelvin":
            result = celsius + 273.15

        result_box.config(text=f"Result: {round(result, 2)}")

    except:
        result_box.config(text="Result: Invalid input")

# Title
title = tk.Label(
    window,
    text="Temperature Converter",
    font=("Segoe UI", 16, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=10)

# FROM label
from_label = tk.Label(
    window,
    text="From:",
    font=("Segoe UI", 11),
    bg="#f2f2f2"
)
from_label.pack()

# From dropdown
from_choice = tk.StringVar()
from_choice.set("Celsius")

from_menu = tk.OptionMenu(window, from_choice, "Celsius", "Fahrenheit", "Kelvin")
from_menu.config(font=("Segoe UI", 11), width=15)
from_menu.pack(pady=5)

# TO label
to_label = tk.Label(
    window,
    text="To:",
    font=("Segoe UI", 11),
    bg="#f2f2f2"
)
to_label.pack()

# To dropdown
to_choice = tk.StringVar()
to_choice.set("Fahrenheit")

to_menu = tk.OptionMenu(window, to_choice, "Celsius", "Fahrenheit", "Kelvin")
to_menu.config(font=("Segoe UI", 11), width=15)
to_menu.pack(pady=5)

# Temperature label
temp_label = tk.Label(
    window,
    text="Temperature:",
    font=("Segoe UI", 11),
    bg="#f2f2f2"
)
temp_label.pack(pady=(10, 0))

# Input box
temp_entry = tk.Entry(
    window,
    font=("Segoe UI", 12),
    justify="center"
)
temp_entry.pack(pady=5)

# Convert button
convert_button = tk.Button(
    window,
    text="Convert",
    font=("Segoe UI", 12),
    bg="#4CAF50",
    fg="white",
    width=18,
    relief="flat",
    command=convert_temp
)
convert_button.pack(pady=15)

# Result display
result_box = tk.Label(
    window,
    text="Result:",
    font=("Segoe UI", 12),
    bg="#f2f2f2"
)
result_box.pack()

window.mainloop()
