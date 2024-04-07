from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_reslut_label.config(text = f"{km}")



window = Tk()
window.title("Mile to Km Converter")
miles_label = Label(text = "Miles")
miles_label.grid(column = 2, row = 0)
miles_input = Entry(width = 9)
miles_input.grid(column = 1, row = 0)



is_equal_to_label = Label(text = "is equal to")
is_equal_to_label.grid(column = 0, row = 1)
 
 
km_label = Label(text = "Km")
km_label.grid(column = 2, row = 1)
kilometer_reslut_label = Label(text = "0")
kilometer_reslut_label.grid(column = 1, row = 1)
calculate_button = Button(text = "Calculate", command = calculate)
calculate_button.grid(column = 1, row = 2)






window.mainloop()