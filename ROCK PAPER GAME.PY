import tkinter as tk
import random

# Define the game logic
choices = ["Rock", "Paper", "Scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_round(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    user_score_var.set(f"User: {user_score}")
    computer_score_var.set(f"Computer: {computer_score}")
    result_var.set(f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

def play_again():
    result_var.set("")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_var.set(f"User: {user_score}")
    computer_score_var.set(f"Computer: {computer_score}")
    result_var.set("")

# Ensure the scores are defined globally
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Unique Rock-Paper-Scissors")
root.geometry("400x450")
root.configure(bg="#1E1E1E")

# Set up the layout
frame = tk.Frame(root, bg="#3E3E3E", bd=5, relief=tk.RAISED, padx=10, pady=10)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title_label = tk.Label(frame, text="Rock-Paper-Scissors", font=("Helvetica", 18, 'bold'), bg="#3E3E3E", fg="#FFD700")
title_label.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var, font=("Helvetica", 14), bg="#3E3E3E", fg="#FFD700", relief=tk.SUNKEN, padx=5, pady=5)
result_label.pack(pady=10)

user_score_var = tk.StringVar()
computer_score_var = tk.StringVar()

score_frame = tk.Frame(frame, bg="#3E3E3E")
score_frame.pack(pady=10)
user_score_label = tk.Label(score_frame, textvariable=user_score_var, font=("Helvetica", 14), bg="#3E3E3E", fg="#FFD700")
user_score_label.grid(row=0, column=0, padx=10)
computer_score_label = tk.Label(score_frame, textvariable=computer_score_var, font=("Helvetica", 14), bg="#3E3E3E", fg="#FFD700")
computer_score_label.grid(row=0, column=1, padx=10)

button_frame = tk.Frame(frame, bg="#3E3E3E")
button_frame.pack(pady=10)
rock_button = tk.Button(button_frame, text="✊ Rock", font=("Helvetica", 14), bg="#FFD700", fg="#1E1E1E", command=lambda: play_round("Rock"), bd=3, relief=tk.RAISED)
rock_button.grid(row=0, column=0, padx=5)
paper_button = tk.Button(button_frame, text="✋ Paper", font=("Helvetica", 14), bg="#FFD700", fg="#1E1E1E", command=lambda: play_round("Paper"), bd=3, relief=tk.RAISED)
paper_button.grid(row=0, column=1, padx=5)
scissors_button = tk.Button(button_frame, text="✌ Scissors", font=("Helvetica", 14), bg="#FFD700", fg="#1E1E1E", command=lambda: play_round("Scissors"), bd=3, relief=tk.RAISED)
scissors_button.grid(row=0, column=2, padx=5)

play_again_button = tk.Button(frame, text="Play Again", font=("Helvetica", 14), bg="#FFD700", fg="#1E1E1E", command=play_again, bd=3, relief=tk.RAISED)
play_again_button.pack(pady=10)

reset_button = tk.Button(frame, text="Reset", font=("Helvetica", 14), bg="#FFD700", fg="#1E1E1E", command=reset_game, bd=3, relief=tk.RAISED)
reset_button.pack(pady=10)

# Adding hover effects
def on_enter(e, widget):
    widget.config(bg='#ff8c00', fg='#fff')

def on_leave(e, widget):
    widget.config(bg='#FFD700', fg='#1E1E1E')

for button in [rock_button, paper_button, scissors_button, play_again_button, reset_button]:
    button.bind("<Enter>", lambda e, btn=button: on_enter(e, btn))
    button.bind("<Leave>", lambda e, btn=button: on_leave(e, btn))

# Initialize the scores
user_score_var.set(f"User: {user_score}")
computer_score_var.set(f"Computer: {computer_score}")

# Run the application
root.mainloop()
