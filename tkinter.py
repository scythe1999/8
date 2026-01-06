import tkinter as tk
from tkinter import ttk

def on_click():
    label.config(text="Hello, Tkinter!")

# Create main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")
root.configure(bg="white")

# Add widgets
label = ttk.Label(root, text="Click the button", font=("Segoe UI", 12))
label.pack(pady=20)

button = ttk.Button(root, text="Say Hello", command=on_click)
button.pack(pady=10)

# Run the app
root.mainloop()
