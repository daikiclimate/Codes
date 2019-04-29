import numpy as np

class Tic_Tac_Toe:
    global board, mark_ox, comment_label
    
    def __init__(self):
        self.turn = 0#プレイヤーターン
        self.winner = 0#勝利プレイヤー
        
    #command for button
    def board_change1(self):
        if board[0]== 0: # =0 のとき空欄、それ以外は置いてあるのでターンを進めない。
            board[0] = self.turn%2 + 1
            self.num2mark()    #012 -> "" "o" "x"
            b1_button["text"] = mark_ox[0]    #update label
            self.win_lose()    #judgement of win
            self.winner_print()
    def board_change2(self):
        if board[1] == 0:
            board[1] = self.turn%2 + 1
            self.num2mark()
            b2_button["text"] = mark_ox[1]
            self.win_lose()
            self.winner_print()
    def board_change3(self):
        if board[2] == 0:
            board[2] = self.turn%2 + 1
            self.num2mark()
            b3_button["text"] = mark_ox[2]
            self.win_lose()
            self.winner_print()
    def board_change4(self):
        if board[3] == 0:
            board[3] = self.turn%2 + 1
            self.num2mark()
            b4_button["text"] = mark_ox[3]
            self.win_lose()
            self.winner_print()
    def board_change5(self):
        if board[4] == 0:
            board[4] = self.turn%2 + 1
            self.num2mark()
            b5_button["text"] = mark_ox[4]
            self.win_lose()
            self.winner_print()
    def board_change6(self):
        if board[5] == 0:
            board[5] = self.turn%2 + 1
            self.num2mark()
            b6_button["text"] = mark_ox[5]
            self.win_lose()
            self.winner_print()
    def board_change7(self):
        if board[6] == 0:
            board[6] = self.turn%2 + 1
            self.num2mark()
            b7_button["text"] = mark_ox[6]
            self.win_lose()
            self.winner_print()
    def board_change8(self):
        if board[7] == 0:
            board[7] = self.turn%2 + 1
            self.num2mark()
            b8_button["text"] = mark_ox[7]
            self.win_lose()
            self.winner_print()
    def board_change9(self):
        if board[8] == 0:
            board[8] = self.turn%2 + 1
            self.num2mark()
            b9_button["text"] = mark_ox[8]
            self.win_lose()
            self.winner_print()
            
    def num2mark(self):
        for t in np.arange(9):
            if board[t] == 0:mark_ox[t] ="    "
            if board[t] == 1:mark_ox[t] =" o "
            if board[t] == 2:mark_ox[t] =" x "
        self.turn += 1
        
    def clear(self):
        #board = np.zeros(9)
        for i in range(9):
            board[i] = 0
        self.num2mark()
        b1_button["text"] = "    "
        b2_button["text"] = "    "
        b3_button["text"] = "    "
        b4_button["text"] = "    "
        b5_button["text"] = "    "
        b6_button["text"] = "    "
        b7_button["text"] = "    "
        b8_button["text"] = "    "
        b9_button["text"] = "    "
        self.turn = 0
        comment_label["text"] =  "o 's turn"
        self.winner = 0
        
#judgement of game
    def win_lose(self):
    #123.456.789,147.258.369.1.5.9.3.5.7
        print(board)
        for i in (0,3,6):
            jud = np.prod(board[i:i+3])
            if jud == 1:
                self.winner = 1
            if jud == 8:
                self.winner = 2 
        for i in (0,1,2):
            jud = np.prod(board[i::3])
            if jud == 1:
                self.winner= 1
            if jud == 8:
                self.winner= 2 
        jud = np.prod(board[0::4])#0, 5,  9
        if jud == 1:
            self.winner= 1
        if jud == 8:
            self.winner= 2
        jud = np.prod([board[2],board[4],board[6]])#2, 4, 6
        if jud == 1:
            self.winner= 1 
        if jud == 8:
            self.winner= 2 
        
    def winner_print(self):
        if self.turn % 2 == 0:
            ban = " o "
        if self.turn % 2 == 1:
            ban = " x "
        if  self.winner== 0:  
            comment_label["text"] = "{}'s turn".format(ban)
        if  self.winner== 1:
            comment_label["text"] = "Player 1 is Winner"
        if  self.winner== 2:
            comment_label["text"] = "Player 2 is Winner"
   # def board_1(board):
        
board = np.zeros(9)#0...blank/ 1...player1/ 2...player2
mark_ox = np.full(9,"    ")

import tkinter as tk

root = tk.Tk()
root.title("")
root.geometry=("640x480")

Tic = Tic_Tac_Toe()
count_label = tk.Label(root, text="Tic_Tac_Toe")
count_label.grid( row=0, column=1 )

comment_label = tk.Label(root, text = "o 's turn")
comment_label .grid (row = 3, column =1)

clear_button= tk.Button(root, text = "clear", command = Tic.clear)
clear_button.grid(row = 2, column = 1)

control_frame = tk.Frame(root)
control_frame.grid(row = 1, column = 1)
b1_button = tk.Button(control_frame, text = mark_ox[0], command = Tic.board_change1)
b1_button.grid(row = 0, column = 0)
b2_button = tk.Button(control_frame, text = mark_ox[1], command =  Tic.board_change2)
b2_button.grid(row = 0, column = 1)
b3_button = tk.Button(control_frame, text = mark_ox[2], command = Tic.board_change3)
b3_button.grid(row = 0, column = 2)
b4_button = tk.Button(control_frame, text = mark_ox[3], command =  Tic.board_change4)
b4_button.grid(row = 1, column = 0)
b5_button = tk.Button(control_frame, text = mark_ox[4], command =  Tic.board_change5)
b5_button.grid(row = 1, column = 1)
b6_button = tk.Button(control_frame, text = mark_ox[5], command =  Tic.board_change6)
b6_button.grid(row = 1, column = 2)
b7_button = tk.Button(control_frame, text = mark_ox[6], command =  Tic.board_change7)
b7_button.grid(row = 2, column = 0)
b8_button = tk.Button(control_frame, text = mark_ox[7], command =  Tic.board_change8)
b8_button.grid(row = 2, column = 1)
b9_button = tk.Button(control_frame, text = mark_ox[8], command =  Tic.board_change9)
b9_button.grid(row = 2, column = 2)

root.mainloop()

