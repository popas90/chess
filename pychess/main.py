from tkinter import *
from pychess.SquareView import SquareView

root = Tk()

leftFrame = Frame(root)
leftFrame.pack(side = LEFT)
rightFrame = Frame(root)
rightFrame.pack(side = RIGHT)

for i in range (0,8):
    for j in range (0,8):
        square = SquareView(leftFrame, "{0}".format(i*8+(j+1)))
        square.grid(row = i, column = j)
        square.config(height = 5, width = 10)

input = Entry(rightFrame)
input.pack()

root.mainloop()