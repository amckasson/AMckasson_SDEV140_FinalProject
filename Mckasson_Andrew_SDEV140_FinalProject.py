from tkinter import *

root = Tk()
root.title("Health Tracker")

#labels

myLabel = Label(root, text="Health Tracker")
myLabel.grid(row=1, column=0, padx=10, pady=10)

myLabel = Label(root, text="Enter your Daily Calorie Goal")
myLabel.grid(row=2, column=0, padx=10, pady=10)

myLabel = Label(root, text="Enter the Workouts that you did today")
myLabel.grid(row=5, column=0, padx=10, pady=10)

myLabel = Label(root, text="Enter the Calaries that you burned today")
myLabel.grid(row=8, column=0, padx=10, pady=10)

#Entries

e = Entry(root, width=35, borderwidth=5)
e.grid(row=3, column=0, padx=10, pady=10)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=6, column=0, padx=10, pady=10)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=9, column=0, padx=10, pady=10)


# set functions

def button_click(number):
	current = e.get()
	e.delete(0, END)

def button_cGoal():
	return

def button_workouts():
	return

def button_cBurned():
	return


# Define Buttons

button_cGoal = Button(root, text="Calaries Goal", padx=10, pady=10, command=button_cGoal)
button_workouts = Button(root, text="Workouts", padx=10, pady=10, command=button_workouts)
button_cBurned = Button(root, text="Calaries Burned", padx=10, pady=10, command=button_cBurned)

#Put the buttons on the screen

button_cGoal.grid(row=4, column=1)
button_workouts.grid(row=7, column=1)
button_cBurned.grid(row=10, column=1)




root.mainloop()

