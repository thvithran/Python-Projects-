from tkinter import *
from tkinter import messagebox
import random as r

#----------- MAIN PROGRAM --------------#
root=Tk()                  # window defined
root.title("Tic-Tac-Toe")  # title given
a=r.choice(['O','X'])      # two operators defined
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]
for i in range(3):
    for j in range(3):
        b[i].append(button(root))
        b[i][j].config(command= lambda row=i,col=j:click(row,col))
        b[i][j].grid(row=i,column=j)

reset_btn = Button(text="Reset Game",font=('arial',15,'bold'),command=reset)
reset_btn.grid(row=3,column=0,columnspan=3)
root.mainloop()

#FUNCTIONS
def button(fname):
    b=Button(fname,padx=1,bg="#D4D4D4",width=3,text="  ",font=("'arial",60,'bold'),relief=RAISED,bd=5)
    return b

def change_a():
    #function to change the  operand for the next player
    global a
    for i in range(3):
        for j in range(3):
            b[i][j]["text"]=" "
            b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])

def check(): #Checks for the victory or Draw
    for i in range(3):
        if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or
        b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
            messagebox.showinfo("Congrats!!","'"+a+"' has won ")
            reset()
    if (b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or
            b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == a):
            messagebox.showinfo("Congrats!!", "'" + a + "' has won ")
            reset()
    elif (b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]
    ["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]
    ["state"]==b[2][2]["state"]==DISABLED):
            messagebox.showinfo("Tied!!","The matched end in a draw")
            reset()

def click(row,col):
    b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
 check()
 change_a()