import tkinter as tk

def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text="Temperature in Fahrenheit: {:.2f}".format(fahrenheit),font=('Arial',25))

def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text="Temperature in Celsius: {:.2f}".format(celsius))

root = tk.Tk()
root.title("Temperature Converter")

celsius_frame = tk.Frame(root)
celsius_frame.pack(pady=25)

celsius_label = tk.Label(celsius_frame, text="Celsius:",font=('Arial',25))
celsius_label.pack(side=tk.LEFT)

celsius_entry = tk.Entry(celsius_frame)
celsius_entry.pack(side=tk.LEFT)

celsius_to_fahrenheit_button = tk.Button(root, text="Celsius to Fahrenheit",font=('Arial',25), command=celsius_to_fahrenheit)
celsius_to_fahrenheit_button.pack(pady=20)


fahrenheit_frame = tk.Frame(root)
fahrenheit_frame.pack(pady=25)

fahrenheit_label = tk.Label(fahrenheit_frame, text="Fahrenheit:",font=('Arial',25))
fahrenheit_label.pack(side=tk.LEFT)

fahrenheit_entry = tk.Entry(fahrenheit_frame)
fahrenheit_entry.pack(side=tk.LEFT)

fahrenheit_to_celsius_button = tk.Button(root, text="Fahrenheit to Celsius",font=('Arial',25), command=fahrenheit_to_celsius)
fahrenheit_to_celsius_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
