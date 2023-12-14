from tkinter import *
from tkinter import messagebox

class HealthApp:
    def __init__(self, root):  #initilizing the class
        self.root = root
        self.root.configure(bg="lightblue")  #changing the background color to lightblue
        self.root.title("Andrews Health App")

        #creating and placing the images becuase I had to resize them they are a little blurry
        self.photo_one = PhotoImage(file="image4.png")
        label = Label(root, image=self.photo_one)
        label.grid(row=1, column=0, columnspan = 2, padx=10, pady=10)

        self.photo_two = PhotoImage(file="image5.png")
        label = Label(root, image=self.photo_two)
        label.grid(row=13, column=0, columnspan = 2, padx=10, pady=10)
        

        # Labels for user entry and title of app
        myLabel = Label(root, text="Health Tracker", font=("Arial", 25))
        myLabel.grid(row=2, column=0, columnspan = 2, padx=10, pady=20)

        myLabel = Label(root, text="Enter your Name: ")
        myLabel.grid(row=3, column=0, padx=10, pady=10)

        myLabel = Label(root, text="Enter the Date: ")
        myLabel.grid(row=4, column=0, padx=10, pady=10)

        myLabel = Label(root, text="Enter your Weight: ")
        myLabel.grid(row=5, column=0, padx=10, pady=10)

        myLabel = Label(root, text="Enter the Calories that you Burned Today:")
        myLabel.grid(row=6, column=0, padx=10, pady=10)

        myLabel = Label(root, text="Enter your Daily Calorie Goal:")
        myLabel.grid(row=7, column=0, padx=10, pady=10)

        myLabel = Label(root, text="Enter the Workouts that you did Today:")
        myLabel.grid(row=8, column=0, padx=10, pady=10)


        # Entries
        self.name_var = StringVar()  #this is storing user input for name
        self.date_var = StringVar()  #this is storing user input for date
        self.weight_var = StringVar() #this is storing user input for weight
        self.calorieGoal_var = StringVar() #this is storing user input for the amount of calories user wants to burn
        self.caloriesBurned_var = StringVar() #this is storing user input for the amount of calories burned 
        self.workoutType_var = StringVar() #this is storing user input for the type of workouts done

        e = Entry(root, textvariable=self.name_var, width=35, borderwidth=5) #entry widget for name
        e.grid(row=3, column=1, padx=10, pady=10) # where its placed

        e = Entry(root, textvariable=self.date_var, width=35, borderwidth=5) #entry widget for name
        e.grid(row=4, column=1, padx=10, pady=10) # where its placed

        e = Entry(root, textvariable=self.weight_var, width=35, borderwidth=5) # entry widget for weight
        e.grid(row=5, column=1, padx=10, pady=10) # where its placed

        e = Entry(root, textvariable=self.calorieGoal_var, width=35, borderwidth=5) #entry widget for calorie goal
        e.grid(row=6, column=1, padx=10, pady=10) # where its placed

        e = Entry(root, textvariable=self.caloriesBurned_var, width=35, borderwidth=5) #entry widget for calories burned
        e.grid(row=7, column=1, padx=10, pady=10) # where its placed

        e = Entry(root, textvariable=self.workoutType_var, width=35, borderwidth=5) #entry widget for the type of workout
        e.grid(row=8, column=1, padx=10, pady=10) # where its placed

        # Buttons
        button_summary = Button(root, text="Daily Report", padx=10, pady=10, command=self.open_summary_window)
        button_clear = Button(root, text="Clear", padx=10, pady=10, command=self.button_clear)
        button_save = Button(root, text="Save", padx=10, pady=10, command=self.button_save)
        button_exit = Button(root, text="Exit", padx=10, pady=10, command=self.button_exit)
        
        
        # Put the buttons on the screen
        button_summary.grid(row=12, column=1)
        button_clear.grid(row=12, column=2)
        button_save.grid(row=12, column=3)
        button_exit.grid(row=12, column=4)

    # Create a function for a new window for the daily report. Its a user report that shows info before you save it to a file.
    def open_summary_window(self):
        summary_window = Toplevel(self.root)
        summary_window.title("Daily Report")

        try:
            weight = int(self.weight_var.get())  #using accessor methods to get info
            calorieGoal = int(self.calorieGoal_var.get())   #using accessor methods to get info
            caloriesBurned = int(self.caloriesBurned_var.get())    #using accessor methods to get info
            caloriesRemaining = caloriesBurned - calorieGoal    #saving calories burned to variable to display in summary
            summary = f"Name: {self.name_var.get()}\n"     #using a format string to display info
            summary += f"Date: {self.date_var.get()}\n"    #using a format string to display info
            summary += f"Weight: {weight} lbs\n"    #using a format string to display info
            summary += f"Calorie Goal: {calorieGoal} calories\n"  #using a format string to display info
            summary += f"Calories Burned: {caloriesBurned} calories\n"  #using a format string to display info
            summary += f"Workout Type: {self.workoutType_var.get()}\n"  #using a format string to display info
            summary += f"Remaining Calories: {caloriesRemaining} calories"  #using a format string to display info
            label_summary = Label(summary_window, text=summary)
            label_summary.pack()
        except ValueError:
            messagebox.showerror("Error", "Enter information in all fields. Enter integers for weight, calorie goal, and calories burned.")   # secure coding, this is what will show if summary failed

    #created a function for button clear, simply resets all fields to blank
    def button_clear(self):
        self.name_var.set("")
        self.date_var.set("")
        self.weight_var.set("")
        self.calorieGoal_var.set("")
        self.caloriesBurned_var.set("")
        self.workoutType_var.set("")

    #created a function for save button, it gets the info and converts it to a string then appends it to a text file created intially the first time a save is successful
    def button_save(self):
        try:
            # Gather workout and user info
            name = self.name_var.get() #using an accessor method to gather info on name
            date = self.date_var.get() #using an accessor method to gather info on date 
            weight = int(self.weight_var.get()) #using an accessor method to gather info on weight 
            calorieGoal = int(self.calorieGoal_var.get()) #using an accessor method to gather info on the calorie goal
            caloriesBurned = int(self.caloriesBurned_var.get()) #using an accessor method to gather info on the calories burned
            workoutType = self.workoutType_var.get() #using an accessor method to gather info on the type of workouts user did

            # calories remaining
            caloriesRemaining = caloriesBurned - calorieGoal 

            # Create a string with the information to save to file
            savedInfo = f"Name: {name}\nDate: {date}\nWeight: {weight} lbs\nCalorie Goal: {calorieGoal} calories\nCalories Burned: {caloriesBurned} calories\nWorkout Type: {workoutType}\nRemaining Calories: {caloriesRemaining} calories\n\n"

            # Open a file in append mode and add workout info
            with open("health_data.txt", "a") as file:
                file.write(savedInfo)

            messagebox.showinfo("Save", "Your workout has been saved to a file.")  #utilizing the messagebox again to display save was not successful
        except ValueError:
            messagebox.showerror("Error", "Your workout was not saved, make sure the data you entered is correct.")  #using secure coding to show user if workout was not saved to file

    def button_exit(self):
    	self.root.destroy()


# Run the program
root = Tk()
health_app = HealthApp(root)
root.mainloop()
