
from tkinter import *

def mile_to_kilometer():
    miles =float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


windows = Tk()
windows.title("Miles to Kilometer Converter")
windows.config(padx=20,pady=20)



miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1,row=1)

km_label = Label(text="km")
km_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=mile_to_kilometer)
calculate_button.grid(column=1,row=2)


windows.mainloop()

