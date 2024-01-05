import tkinter as tk

def display_input():
    input_text = entry.get()
    label_result.config(text=f"You entered: {input_text}")

# Create the main window
app = tk.Tk()
app.title("Desktop App")

# Create and place widgets
label = tk.Label(app, text="Enter data:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

button = tk.Button(app, text="Display Input", command=display_input)
button.pack(pady=10)

label_result = tk.Label(app, text="")
label_result.pack(pady=10)

# Run the application
app.mainloop()



