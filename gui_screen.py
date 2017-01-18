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

def setLabel(label, imageHolder, building, room, path):
	buildingPart = building.get()
	roomPart = room.get()
	path.set("%s%d.jpg" % (buildingPart, roomPart) )
	print("Building" + str(buildingPart) + " Room" + str(roomPart) + path.get())
	label.set("Building" + str(buildingPart) + " Room" + str(roomPart))
	newImage = ImageTk.PhotoImage(Image.open(path.get()))
	imageHolder = newImage
#	imageHolder.configure(image = newImage)
#	imageHolder.image = newImage
	return (buildingPart, roomPart)

win = Tk()

my_font = tkFont.Font(family = "Helvetica", size = "36", weight = "bold")

win.title("Graphical User Interface - proto")
win.geometry('1280x720')

container = Frame(win)
uiBox = Frame(container)
imageBox = Frame(container)

#Building ------------------- pack win
building = Frame(uiBox)

buildingLetter = StringVar()
buildingLetter.set('A')

letterMenu = OptionMenu(building, buildingLetter, 'A', 'B', 'C')
letterMenu.config(compound='right',width=50, height=3)
letterMenu.grid(sticky="WE", row=0, column=0)

building.pack()
#building.grid(row=0, column=0)

#Room -----------------pack win ______ grid inside
room = Frame(uiBox)
counter = IntVar()
counter.set(0)

#TODO use Spinbox()
e1 = Entry(room, textvariable=counter)
e1.grid(row=0)

plusButton = Button(room, text = "+", font = my_font, command = lambda: increaseState(counter), height = 1, width = 2)
plusButton.grid(row=0, column=1)

minusButton = Button(room, text = "-", font = my_font, command = lambda: decreaseState(counter), height = 1, width = 2)
minusButton.grid(row=0, column=2)

room.pack()
#room.grid(row=0, column=1)

#Label -----------   pack win
panelStr = StringVar()
panel = Label(uiBox, textvariable=panelStr)
panel.pack()
#panel.grid(row=0, column=3)

#Image ---------------- pack win
path = StringVar()
path.set("A0.jpg")
img = ImageTk.PhotoImage( Image.open( path.get() ))
#photo = Label(imageBox, image = img)
#photo.pack()
#photo.grid(row=0, column=4)

#Button ------------------  pack win
roomButton = Button(uiBox, text="get", font = my_font, command = lambda: (setLabel( panelStr, img, buildingLetter, counter, path)) )
roomButton.pack()
#roomButton.grid(row=0,column=2)

def openImageWindow(_path):
	secondWin = Toplevel(win)
	leaveWindow = lambda *e: secondWin.destroy()
	secondWin.focus_set()
	secondWin.wm_attributes('-zoomed', "2")
	secondWin.bind("<Escape>", leaveWindow)

	newImage = ImageTk.PhotoImage( Image.open( _path.get() ))
	photo = Label(secondWin)
	photo.configure(image = newImage)
	photo.image = newImage
	exitButton2 = Button(secondWin, text = "Exit", font = my_font, command = leaveWindow, height = 1, width = 2)

	exitButton2.pack()
	photo.pack()

#Button ------------------  pack win
newWindow= Button(uiBox, text="new Window", font = my_font, command = lambda: openImageWindow(path))
newWindow.pack()

#Exit Button  - pack win
exitButton = Button(uiBox, text = "Exit", font = my_font, command = exitProgram, height = 2, width = 5)
exitButton.pack()
#exitButton.grid(row=1, pady=100)

uiBox.grid(row=1, column=0)
imageBox.grid(row=1, column=1)
container.pack()

win.bind("<Escape>", quit)
mainloop()
