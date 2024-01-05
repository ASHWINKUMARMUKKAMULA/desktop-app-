import tkinter as tk

def display_input(page_number):
    input_text = entry.get()
    if page_number == 1:
        label_result.config(text=f"You entered on Page 1: {input_text}")
    elif page_number == 2:
        label_result_page2.config(text=f"You entered on Page 2: {input_text}")

def go_to_page2():
    show_page(2)

def go_back_to_page1():
    show_page(1)

def show_page(page_number):
    if page_number == 1:
        frame_page1.pack()
        frame_page2.pack_forget()
    elif page_number == 2:
        frame_page1.pack_forget()
        frame_page2.pack()

# Create the main window
app = tk.Tk()
app.title("MAJOR PROJECT")


# Create and place widgets for Page 1
frame_page1 = tk.Frame(app)

label_page1 = tk.Label(frame_page1, text="Enter data for Page 1:")
label_page1.pack(pady=10)

entry = tk.Entry(frame_page1)
entry.pack(pady=10)

button_page1 = tk.Button(frame_page1, text="Next Page", command=go_to_page2)
button_page1.pack(pady=10)

label_result = tk.Label(frame_page1, text="")
label_result.pack(pady=10)

# Create and place widgets for Page 2
frame_page2 = tk.Frame(app)

label_page2 = tk.Label(frame_page2, text="Enter data for Page 2:")
label_page2.pack(pady=10)

entry_page2 = tk.Entry(frame_page2)
entry_page2.pack(pady=10)

button_page2 = tk.Button(frame_page2, text="Display Input", command=lambda: display_input(2))
button_page2.pack(pady=10)

label_result_page2 = tk.Label(frame_page2, text="")
label_result_page2.pack(pady=10)

# Back button on Page 2
back_button_page2 = tk.Button(frame_page2, text="Back to Page 1", command=go_back_to_page1)
back_button_page2.pack(pady=10)

# Initially, show Page 1
show_page(1)

# Run the application
app.mainloop()
