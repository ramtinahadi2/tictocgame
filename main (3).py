import tkinter as tk
import random
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        self.difficulty = "easy"  #default difficulty easy

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text="", width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.new_game_button = tk.Button(self.master, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=3, columnspan=3, sticky="ew")

        self.continue_game_button = tk.Button(self.master, text="Continue Game", command=self.continue_game)
        self.continue_game_button.grid(row=4, columnspan=3, sticky="ew")

        self.player_mode = tk.StringVar(value="single")
        self.single_player_button = tk.Radiobutton(self.master, text="Single Player", variable=self.player_mode, value="single", command=self.set_player_mode)
        self.single_player_button.grid(row=5, columnspan=3, sticky="ew")

        self.multiplayer_button = tk.Radiobutton(self.master, text="Multiplayer", variable=self.player_mode, value="multi", command=self.set_player_mode)
        self.multiplayer_button.grid(row=6, columnspan=3, sticky="ew")

        self.difficulty_mode = tk.StringVar(value="easy")
        self.easy_difficulty_button = tk.Radiobutton(self.master, text="Easy", variable=self.difficulty_mode, value="easy")
        self.easy_difficulty_button.grid(row=7, columnspan=3, sticky="ew")

        self.normal_difficulty_button = tk.Radiobutton(self.master, text="Normal", variable=self.difficulty_mode, value="normal")
        self.normal_difficulty_button.grid(row=8, columnspan=3, sticky="ew")

        self.hard_difficulty_button = tk.Radiobutton(self.master, text="Hard", variable=self.difficulty_mode, value="hard")
        self.hard_difficulty_button.grid(row=9, columnspan=3, sticky="ew")

    def set_player_mode(self):
        if self.player_mode.get() == "multi":
            self.difficulty_mode.set("easy")

    def make_move(self, index):
        if self.game_over:
            return

        if self.player_mode.get() == "single" and self.current_player == "O":
            self.cpu_move()
            return

        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.game_over = True
            elif "" not in self.board:
                messagebox.showinfo("Draw", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def cpu_move(self):
        if self.difficulty == "easy":
            available_moves = [i for i in range(9) if self.board[i] == ""]
            if available_moves:
                move = random.choice(available_moves)
                self.board[move] = "O"
                self.buttons[move].config(text="O")
        elif self.difficulty == "normal":
            # TODO: Add logic for normal difficulty
            pass
        elif self.difficulty == "hard":
            # TODO: Add logic for hard difficulty
            pass

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]]
                    and self.board[condition[0]] != ""):
                return True
        return False

    def new_game(self):
        self.reset_board()
        self.game_over = False

    def reset_board(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"

    def continue_game(self):
        if self.game_over:
            self.reset_board()
            self.game_over = False

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
