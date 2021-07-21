from Tkinter import *

class App(Tk):
    def __init__(self):
        self.root = Tk()
        self.root.title("BMI Calculator")
        Tk.__init__(self)


        # Sets a label and entry field into the window for weight, height in
        # feet, and height in inches
        self.label = Label(self.root, text="Enter your weight in pounds.").pack()
        self.lbs = StringVar()
        Entry(self.root, textvariable=self.lbs).pack()

        self.label = Label(self.root, text="Enter your height in feet.").pack()
        self.feet = StringVar()
        Entry(self.root, textvariable=self.feet).pack()

        self.label = Label(self.root, text="Enter your height in inches.").pack()
        self.inches = StringVar()
        Entry(self.root, textvariable=self.inches).pack()

        # Sets a button and label to click and calculate BMI
        self.buttontext = StringVar()
        Button(self.root, textvariable=self.buttontext, command=self.calculate).pack()
        self.buttontext.set("Calculate")

        # Sets bmi_num to a StringVar so that when it is changed, the label will
        # update
        self.bmi_num = StringVar()
        Label(self.root, textvariable=self.bmi_num).pack()

        # Same thing here
        self.bmi_text = StringVar()
        Label(self.root, textvariable=self.bmi_text).pack()

        self.root.mainloop()

    def calculate(self):
        # Retrieves all necessary information to calculate BMI
        weight = float(self.lbs.get())
        feet = float(self.feet.get())
        inches = float(self.inches.get())
        height = (feet*12)+inches
        bmi = float((weight*703)/(height**2))
        # Updates the status label
        self.bmi_num.set("Your BMI is %.2f" % bmi)
        if bmi < 18.5:
            self.bmi_text.set("You are underweight")
        if 18.5 <= bmi < 25:
            self.bmi_text.set("You are normal")
        if 25 <= bmi < 30:
            self.bmi_text.set("You are overweight")
        if 30<= bmi > 30:
            self.bmi_text.set("You are obese")

App()