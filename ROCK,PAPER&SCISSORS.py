import tkinter as tk
import random
wins, losses, ties = 0, 0, 0
names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

def update_result(result_text):
    result_label.config(text=result_text)
    score_label.config(text=f'Wins: {wins} | Losses: {losses} | Ties: {ties}')
def play(choice):
    global wins, losses, ties
    cpu_choice = random.choice(['R', 'P', 'S'])
    
    if choice == cpu_choice:
        ties += 1
        update_result(f"It's a tie! You both chose {names[choice]}.")
    elif choice == 'R':
        if cpu_choice == 'P':
            losses += 1
            update_result(f'CPU wins! You chose {names[choice]}, CPU chose {names[cpu_choice]}.')
        else:
            wins += 1
            update_result(f'You won! You chose {names[choice]}, CPU chose {names[cpu_choice]}.')
    elif choice == 'P':
        if cpu_choice == 'S':
            losses += 1
            update_result(f'CPU wins! You chose {names[choice]}, CPU chose {names[cpu_choice]}.')
        else:
            wins += 1
            update_result(f'You won! You chose {names[choice]}, CPU chose {names[cpu_choice]}.')
    elif choice == 'S':
        if cpu_choice == 'R':
            losses += 1
            update_result(f'CPU wins! You chose {names[choice]}, CPU chose {names[cpu_choice]}.')
        else:
            wins += 1
            update_result(f'You won! You chose {names[choice]}, CPU chose {names[cpu_choice]}.')

def quit_game():
    root.destroy()
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("700x500")

instruction_label = tk.Label(root, text="Choose your move: Rock, Paper, or Scissors", font=("Times New Roman", 14))
instruction_label.pack(pady=10)

btn_rock = tk.Button(root, text="Rock", command=lambda: play('R'), width=15, font=("Times New Roman", 12))
btn_rock.pack(pady=5)
btn_paper = tk.Button(root, text="Paper", command=lambda: play('P'), width=15, font=("Times New Roman", 12))
btn_paper.pack(pady=5)
btn_scissors = tk.Button(root, text="Scissors", command=lambda: play('S'), width=15, font=("Times New Roman", 12))
btn_scissors.pack(pady=5)
result_label = tk.Label(root, text="Make your choice!", font=("Times New Roman", 12), fg="green")
result_label.pack(pady=10)
score_label = tk.Label(root, text=f"Wins: {wins} | Losses: {losses} | Ties: {ties}", font=("Times New Roman", 12))
score_label.pack(pady=10)
btn_quit = tk.Button(root, text="Quit", command=quit_game, width=15, font=("Times New Roman", 12), bg="red", fg="white")
btn_quit.pack(pady=5)
root.mainloop()
