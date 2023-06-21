import tkinter as tk

def convert(event=None):  # Add 'event=None' as a parameter
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit}°F")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Celsius to Fahrenheit Converter")
window.geometry("400x200")  # Set the window size

# Create and configure widgets
label = tk.Label(window, text="Enter Celsius temperature:", font=("Arial", 16))
label.pack(pady=10)  # Add padding around the label

entry = tk.Entry(window, font=("Arial", 16))
entry.pack(pady=10)

convert_button = tk.Button(window, text="Convert", font=("Arial", 16), command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(window, font=("Arial", 16))
result_label.pack(pady=10)

# Bind the <Return> event to the entry field
entry.bind('<Return>', convert)

# Start the main loop
window.mainloop()
