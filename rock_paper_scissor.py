import random
import tkinter as tk
from tkinter import messagebox

# Initialize scores
user_score = 0
computer_score = 0

def play(choice):
    global user_score, computer_score
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    result = determine_winner(choice, computer_choice)
    
    if "Win" in result:
        user_score += 1
    elif "Lose" in result:
        computer_score += 1
    
    result_label.config(text=f'Computer chose: {computer_choice}\n{result}')
    score_label.config(text=f'Your Score: {user_score} | Computer Score: {computer_score}')

def determine_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Scissors' and computer == 'Paper') or \
         (player == 'Paper' and computer == 'Rock'):
        return "You Win!"
    else:
        return "You Lose!"

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x350")

label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))
label.pack(pady=20)

# Buttons for choices
rock_button = tk.Button(root, text="Rock", command=lambda: play('Rock'), width=10, height=2)
paper_button = tk.Button(root, text="Paper", command=lambda: play('Paper'), width=10, height=2)
scissors_button = tk.Button(root, text="Scissors", command=lambda: play('Scissors'), width=10, height=2)

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

# Label for result
tk.Label(root, text="Result:", font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Label for scores
score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Run the application
root.mainloop()
