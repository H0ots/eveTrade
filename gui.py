from Tkinter import *

# creates our application object
root = Tk()
item = StringVar()
market = StringVar()

# dimensions of the initial box frame
root.geometry('350x350')
root.title('EveTrader')

# creates labels
itemLabel = Label(root, text="Item Name")
solarLabel = Label(root, text="System Name")

# creates a search button
searchBut = Button(root, text="Search for data", fg="white", bg="black")

# creates entry boxes for user input and stores them in "textvariable" variable
itemEntry = Entry(root, textvariable=item)
solarEntry = Entry(root, textvariable=market)

# grid layout for our application
itemLabel.grid(row=0, sticky=E)
solarLabel.grid(row=1, stick=E)
itemEntry.grid(row=0, column=1)
solarEntry.grid(row=1, column=1)
searchBut.grid(columnspan=2)

# construct menu
menubar = Menu(root)

''' File menu '''
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save As...")
file_menu.add_command(label="Close")
menubar.add_cascade(labe="File", menu=file_menu)

''' Help menu '''
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Forum Support")
help_menu.add_command(label="About")
help_menu.add_command(label="Eve-Central")          # https://eve-central.com/
menubar.add_cascade(labe="Help", menu=help_menu)

root.config(menu=menubar)

# ensures that our application window does not close
root.mainloop()
