from tkinter import*

#Create the window
root = Tk()

#Defining button click
def pressed(number):
    global value
    value = value + str(number)
    text.set(value)

#Defining functions
def equals():
    global value
    sum = str(eval(value))
    text.set(sum)
    value = ""

#GUI title
root.title("Calculator")

value = ""
text = StringVar()

bottomframe = Frame(root)
bottomframe.grid()

#Defining buttons and display
display = Entry(bottomframe, font = ("Century Gothic", 20, "bold"), textvariable = text, justify = "right", bd = 20).grid(columnspan = 4)

button1 = Button(bottomframe, text = "+", padx = 28, bd =7, command = lambda:pressed("+")).grid(row = 5, column = 3)
button2 = Button(bottomframe, text = "-",padx = 28, bd =7, command = lambda:pressed("-")).grid(row = 4, column = 3)
button3 = Button(bottomframe, text = "/",padx = 28, bd = 7, command = lambda:pressed("/")).grid(row = 3, column = 3)
button4 = Button(bottomframe, text = "*",padx = 28, bd = 7, command = lambda:pressed("*")).grid(row = 6, column = 1)
button5 = Button(bottomframe, text = ",",padx = 28, bd = 7, command = lambda:pressed(",")).grid(row = 6, column = 2)
button6 = Button(bottomframe, text = "%",padx = 28, bd = 7, command = lambda:pressed("%")).grid(row = 3, column = 3)
button7 = Button(bottomframe, text = "=",padx = 28, bd = 7, command = equals).grid(row = 6, column = 3)
button8 = Button(bottomframe, text = "C",padx = 28, bd = 7, command = lambda:pressed("C")).grid(row = 3, column = 3)

button9 = Button(bottomframe, text = "1",padx = 28, bd = 7, command = lambda:pressed(1)).grid(row = 5, column = 0)
button11 = Button(bottomframe, text = "2",padx = 28, bd = 7, command = lambda:pressed(2)).grid(row = 5, column = 1)
button12 = Button(bottomframe, text = "3",padx = 28, bd = 7, command = lambda:pressed(3)).grid(row = 5, column = 2)
button13 = Button(bottomframe, text = "4",padx = 28, bd = 7, command = lambda:pressed(4)).grid(row = 4, column = 0)
button14 = Button(bottomframe, text = "5",padx = 28, bd = 7, command = lambda:pressed(5)).grid(row = 4, column = 1)
button15 = Button(bottomframe, text = "6",padx = 28, bd = 7, command = lambda:pressed(6)).grid(row = 4, column = 2)
button16 = Button(bottomframe, text = "7",padx = 28, bd = 7, command = lambda:pressed(7)).grid(row = 3, column = 0)
button17 = Button(bottomframe, text = "8",padx = 28, bd = 7, command = lambda:pressed(8)).grid(row = 3, column = 1)
button18 = Button(bottomframe, text = "9",padx = 28, bd = 7, command = lambda:pressed(9)).grid(row = 3, column = 2)
button19 = Button(bottomframe, text = "0",padx = 28, bd = 7, command = lambda:pressed(0)).grid(row = 6, column = 0)


root.mainloop()
