from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=20,pady=20)

def clicked_button():
    dst_miles = int(entry.get())
    dst_km = round(dst_miles*1.609,2)
    label_3.config(text=dst_km)

# Labels
label_1 = Label(text="is equal to")
label_2 = Label(text="Miles")
label_3 = Label(text=0 )
label_4 = Label(text="Km" )
label_1.grid(column=0,row=1)
label_3.grid(column=1,row=1)
label_4.grid(column=2,row=1)
label_3.config(padx=20)
label_2.grid(column=2, row=0)

# Button
button = Button(text="Calculate", command=clicked_button)
button.grid(column=1, row=2)

# Entry
entry = Entry(width=10)
entry.grid(column=1,row=0)

window.mainloop()