from tkinter import *

def miles_to_KM():
    miles = float(miles_entry.get())
    km = round(miles * 1.689)
    result.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer convertor")
window.config(padx= 20, pady= 20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

miles_entry = Entry(width= 7)
miles_entry.grid(column=1, row=0)

Km_label = Label(text="KM")
Km_label.grid(column=2, row=1)

result = Label(text= "0")
result.grid(column=1 , row=1)

equal_label = Label(text="Is Equal to ")
equal_label.grid(column=0, row=1)

button = Button(text="Calculate", command=miles_to_KM)
button.grid(column=1, row=2)


window.mainloop()
