#Import tkinter library
from tkinter import *
from tkinter import ttk
import pickle
import numpy as np

mymodel = pickle.load(open('mymodel.sav','rb')) 
#Create an instance of tkinter frame or window
win= Tk()

#Set the geometry of tkinter frame
win.title("Number of deaths in prediction")
win.geometry("860x420")
def myCalculator():
   vT1 = float(entry1.get())
   vT2 = float(entry2.get())
   vT3 = float(entry3.get())
   predicted_Die = np.round(mymodel.predict([[vT1,vT2,vT3]]))
   lbl.config(text="Deaths prediction: " + str (predicted_Die))


#Create an Entry 1 Widget
lbl1 = Label(text="Number of positive cases:", width=40)
lbl1.pack(pady=10)
entry1= ttk.Entry(win,font=('Century 20'),width=40)
entry1.pack(pady= 10)

#Create an Entry 2 Widget
lbl2 = Label(text="Number of people older than 70:", width=40)
lbl2.pack(pady=10)
entry2= ttk.Entry(win,font=('Century 20'),width=40)
entry2.pack(pady=10)

#Create an Entry 3 Widget
lbl3 = Label(text="Population:", width=40)
lbl3.pack(pady=10)
entry3= ttk.Entry(win,font=('Century 20'),width=40)
entry3.pack(pady=10)

#Create a button to display the text of entry widget
button= ttk.Button(win, text="Predict the number of deaths", command= myCalculator)
button.pack()

# Create label to show result
lbl = Label(win, text="Deaths Prediction: ", font= ('Century 20 bold'))
lbl.pack(pady=10)

# Show windows
win.mainloop()