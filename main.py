from tkinter import *

from datetime import *

  
# importing strftime function to
# retrieve system's time
from time import strftime

def click_start():
    print("start clicked")

def click_stop():
    print("stop clicked")

def click_reset():
    print("reset clicked")

def click_quit():
    print("quit clicked")
    window.destroy()

window = Tk()
width_value = window.winfo_screenwidth
height_value = window.winfo_screenheight
window.geometry("800x600")

button_start = Button(window, text="START", command=click_start, font=("Comic Sans", 30))
button_start.place(relx = 0.25, rely = 0.94)

button_stop = Button(window, text="STOP ", command=click_stop, font=("Comic Sans", 30))
button_stop.place(relx = 0.4, rely = 0.94)

button_reset = Button(window, text = "RESET", command=click_reset, font=("Comic Sans", 30))
button_reset.place(relx = 0.55, rely = 0.94)

button_quit = Button(window, text = "QUIT", command=click_quit, font=("Comic Sans", 30))
button_quit.place(relx = 0.70, rely = 0.94)

# This function is used to 
# display time on the label
def time():
    string = strftime('%H:%M:%S:%f %p')
    lbl.config(text = string)
    lbl.after(100, time)

print("here")
  
# Styling the label widget so that clock
# will look more attractive
lbl = Label(window, font = ('calibri', 240, 'bold'), background = 'purple', foreground = 'white')
  
# Placing clock at the centre
# of the tkinter window
#lbl.pack(anchor = 'center')
lbl.place(relx=0.05, rely=0.1, relheight = 0.8, relwidth=0.9)
time()


window.attributes('-fullscreen', True)

window.mainloop()
