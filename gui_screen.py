from Tkinter import *
import Image
import ImageTk
import tkFont


def exitProgram():
	print("Exit Button Pressed")
	win.quit()

def increaseState(state):
	#string.set("Something diffrent")
	state.set(state.get() + 1)

def decreaseState(state):
	state.set(state.get() - 1)

def setLabel(label, building, room, path):
	buildingPart = building.get()
	roomPart = room.get()
	path.set("img%d.jpg" % roomPart)
	print("Building" + str(buildingPart) + " Room" + str(roomPart) + path.get())
	label.set("Building" + str(buildingPart) + " Room" + str(roomPart))
	return (buildingPart, roomPart)

win = Tk()

my_font = tkFont.Font(family = "Helvetica", size = "36", weight = "bold")

win.title("Graphical User Interface - proto")
win.geometry('1280x720')

#Building -------------------
building = Frame(win)

buildingLetter = StringVar()
buildingLetter.set('A')

letterMenu = OptionMenu(building, buildingLetter, 'A', 'B', 'C')
letterMenu.grid(row=0, column=0)

building.grid(row=0, column=0)

#Room ------------------------
room = Frame(win)
counter = IntVar()
counter.set(0)

#TODO use Spinbox()
e1 = Entry(room, textvariable=counter)
e1.grid(row=0)

plusButton = Button(room, text = "+", font = my_font, command = lambda: increaseState(counter), height = 1, width = 2)
plusButton.grid(row=0, column=1)

minusButton = Button(room, text = "-", font = my_font, command = lambda: decreaseState(counter), height = 1, width = 2)
minusButton.grid(row=0, column=2)

room.grid(row=0, column=1)

#Label -----------
panelStr = StringVar()
panel = Label(win, textvariable=panelStr)
panel.grid(row=0, column=3)

#Image ----------------
path = StringVar()
path.set("img3.jpg")
img = ImageTk.PhotoImage(Image.open(path.get()))

photo = Label(win, image = img)
photo.grid(row=0, column=4)

#Button ------------------
roomButton = Button(win, text="get", font = my_font, command = lambda: setLabel(panelStr, buildingLetter, counter, path))
roomButton.grid(row=0,column=2)


exitButton = Button(win, text = "Exit", font = my_font, command = exitProgram, height = 3, width = 7)
exitButton.grid(row=1, pady=100)

mainloop()
