import tkinter as tk
import random

def number_gussing_game():
    sceret_number=random.randint(1,100)
    attempts_left=10
    def check_guess():
        nonlocal attempts_left
        try:
            guess=int(entry.get())
            attempts_left -=1
            if guess < sceret_number:
                result_label.config(text=f"Too low!  Attempts left:{attempts_left}")
            elif guess > sceret_number:
                result_label.config(text=f"Too High! Attempts left:{attempts_left}")
            else:
                result_label.config(text=f"🎉 Congratulations! The Numbers was {sceret_number}")
                guess_button.config(state="disabled")
                return
            if attempts_left==0 and guess != sceret_number:
                result_label.config(text=f"Out of Attempts! The number was {sceret_number}")
                guess_button.config(state="disabled")
        except ValueError:
            result_label.config(text="You Enter invalid Number.")

# GUI Setup
    root=tk.Tk()

    root.title("Number Guessing game")
    tk.Label(root,text="Guess a Number Between 1 to 100 ",font=("Arial",14)).pack(pady=10)

    entry=tk.Entry(root,width=10,font=("Arial",15))
    entry.pack(pady=5)

    guess_button=tk.Button(root,text="Guess",font=("Arial",15), command=check_guess)
    guess_button.pack(pady=5)

    result_label=tk.Label(root,text="",font=("Arial",14))
    result_label.pack(pady=10)

    root.mainloop()

#Run the Game 

number_gussing_game()
        