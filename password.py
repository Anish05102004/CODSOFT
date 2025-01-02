import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """Generate a random password based on user input."""
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be greater than 0")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        password_var.set(f"Password is: {password}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def toggle_theme():
    """Toggle between dark and light themes."""
    if root.cget('bg') == '#1E1E1E':
        root.configure(bg='#FFFFFF')
        frame.configure(bg='#F0F0F0')
        title_label.configure(bg='#F0F0F0', fg='#000000')
        length_label.configure(bg='#F0F0F0', fg='#000000')
        generate_button.configure(bg='#4CAF50', fg='#FFFFFF')
        password_entry.configure(readonlybackground='#F0F0F0', fg='#000000', highlightbackground='#4CAF50', highlightcolor='#4CAF50')
        theme_button.configure(text='Switch to Dark Theme')
    else:
        root.configure(bg='#1E1E1E')
        frame.configure(bg='#2B2B2B')
        title_label.configure(bg='#2B2B2B', fg='#FF5722')
        length_label.configure(bg='#2B2B2B', fg='#8BC34A')
        generate_button.configure(bg='#2196F3', fg='#FFFFFF')
        password_entry.configure(readonlybackground='#2B2B2B', fg='#FFC107', highlightbackground='#FF5722', highlightcolor='#FF5722')
        theme_button.configure(text='Switch to Light Theme')

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#1E1E1E")

# Set up the layout
frame = tk.Frame(root, bg="#2B2B2B", bd=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title_label = tk.Label(frame, text="Password Generator", font=("Helvetica", 18, 'bold'), bg="#2B2B2B", fg="#FF5722")
title_label.pack(pady=10)

length_label = tk.Label(frame, text="Password Length:", font=("Helvetica", 12), bg="#2B2B2B", fg="#8BC34A")
length_label.pack(pady=5)

length_entry = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief=tk.SUNKEN)
length_entry.pack(pady=5)

generate_button = tk.Button(frame, text="Generate Password", font=("Helvetica", 12, 'bold'), bg="#2196F3", fg="#FFFFFF", command=generate_password)
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(frame, textvariable=password_var, font=("Helvetica", 12), state="readonly", readonlybackground="#2B2B2B", fg="#FFC107", justify="center", bd=0)
password_entry.pack(pady=10)

# Adding hover effect to the button
def on_enter(e):
    generate_button.config(background='#673AB7', foreground='#FFFFFF')

def on_leave(e):
    generate_button.config(background='#2196F3', foreground='#FFFFFF')

generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

# Adding a stylish box effect
password_entry.config(relief=tk.FLAT, highlightbackground="#FF5722", highlightcolor="#FF5722", highlightthickness=2)

# Add a theme toggle button
theme_button = tk.Button(root, text="Switch to Light Theme", font=("Helvetica", 10, 'bold'), bg="#FF5722", fg="#FFFFFF", command=toggle_theme)
theme_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Run the application
root.mainloop()
