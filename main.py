import tkinter as tk

def increment_number():
    current_number = int(lbl_number["text"])
    lbl_number["text"] = str(current_number + 1)

# Create the main Tkinter window
window = tk.Tk()

# Set the window title
window.title("Number Incrementer")

# Set the window size and position for phone resolution
window.geometry("320x480+0+0")

# Create a label to display the number
lbl_number = tk.Label(window, text="0", font=("Arial", 24))
lbl_number.pack(pady=20)

# Create a button to increment the number
btn_increment = tk.Button(window, text="Increment", font=("Arial", 18), command=increment_number)
btn_increment.pack()

# Start the Tkinter event loop
window.mainloop()
