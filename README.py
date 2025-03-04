# To-Do-List  
import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x400")
        
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0
        
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18))
        self.title_label.pack(pady=10)
        
        self.score_label = tk.Label(root, text="User: 0  |  Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=5)
        
        self.result_label = tk.Label(root, text="Make your move!", font=("Arial", 14))
        self.result_label.pack(pady=10)
        
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        for choice in self.choices:
            btn = tk.Button(self.buttons_frame, text=choice, width=10, command=lambda c=choice: self.play(c))
            btn.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == "Win":
            self.user_score += 1
            message = f"You chose {user_choice}, Computer chose {computer_choice}. You Win!"
        elif result == "Lose":
            self.computer_score += 1
            message = f"You chose {user_choice}, Computer chose {computer_choice}. You Lose!"
        else:
            message = f"You chose {user_choice}, Computer chose {computer_choice}. It's a Tie!"
        
        self.result_label.config(text=message)
        self.score_label.config(text=f"User: {self.user_score}  |  Computer: {self.computer_score}")

    def determine_winner(self, user, computer):
        if user == computer:
            return "Tie"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Scissors" and computer == "Paper") or \
             (user == "Paper" and computer == "Rock"):
            return "Win"
        else:
            return "Lose"

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="User: 0  |  Computer: 0")
        self.result_label.config(text="Make your move!")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
