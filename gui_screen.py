from Tkinter import *
import tkFont

def exitProgram():
	print("Exit Button Pressed")
	win.quit()

win = Tk()

my_font = tkFont.Font(family = "Helvetica", size = "36", weight = "bold")

win.title("Graphical User Interface - proto")
win.geometry('1280x720')

exitButton = Button(win, text = "Exit", font = my_font, command = exitProgram, height = 3, width = 7)
exitButton.pack()

mainloop()
