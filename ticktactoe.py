# -*- coding: utf-8 -*-
"""
Tic Tac Toe
@author: Prajakta Joshi
"""

board =[]

class Player(object):
    def __init__(self,type = "X"):
        self.type =type
    def setplayer(self,type):
        self.type =type
    def getplayer(self):
        return self.type

def resetboard(board):
    board.clear()
    for i in range(9):
        board.append("-")
        
def printboard(board):
    print(board[0] + " " + board[1] + " " + board[2]) 
    print(board[3] + " " + board[4] + " " + board[5]) 
    print(board[6] + " " + board[7] + " " + board[8])

def changeplayer(p):
    p.setplayer("O") if p.getplayer() == "X" else p.setplayer("X")
    
def makemove(p,board):
    while True:
        print("Player " + p.getplayer() + " where do you want to put your marker?")
        strinput = input()
        pinput = int(strinput) -1
        if board[pinput] == "-": 
            break
        else:
            print("that space is already taken, try again")
            continue
    board[pinput] = p.getplayer()
#  turnnumber +=1
    
def checkwin(p,board):
    if board[0] == board[1] == board [2] == p.getplayer():
        return True
    elif board[3] == board[4] == board [5] == p.getplayer():
        return True
    elif board[6] == board[7] == board [8] == p.getplayer():
        return True
    elif board[0] == board[4] == board [8] == p.getplayer():
        return True
    elif board[6] == board[4] == board [2] == p.getplayer():
        return True
    if board[0] == board[3] == board [6] == p.getplayer():
        return True
    if board[1] == board[4] == board [7] == p.getplayer():
        return True
    if board[8] == board[5] == board [2] == p.getplayer():
        return True
    else:
        return False
    
    
def main():
    c = Player()
    resetboard(board)
    turnnumber =1
    while True:
        printboard(board)
        makemove(c,board)
        turnnumber +=1
        if checkwin(c,board) ==True:
            printboard(board)
            break
        elif turnnumber ==10:
            print("it is a tie!")
            break

        else:
            changeplayer(c)
            continue
    print("do you want to play again?")
    again = input()
    if again.startswith("y" or "Y"):
        main()
    else:
        pass
        
main()

    
        
    
    
    
