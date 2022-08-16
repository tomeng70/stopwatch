from tkinter import *
from datetime import *
import time

# use numbers to represent state
STOPPED = 0
STARTED = 1
RUNNING = 2
RESET = 3

current_state = RESET
start_time = 0
current_time = 0
elapsed_time = 0

def click_start():
    global current_state
    print("start clicked")
    current_state = STARTED

def click_stop():
    global current_state
    print("stop clicked")
    current_state = STOPPED

def click_reset():
    global current_state
    print("reset clicked")
    current_state = RESET

def click_quit():
    global current_state
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
def update_time():
    global current_state
    global start_time
    global current_time
    global elapsed_time
    print(current_state)
    if (current_state == STOPPED):
        # do something
        pass
    elif (current_state == STARTED):
        start_time = time.time_ns()
        current_state = RUNNING
    elif (current_state == RUNNING):
        current_time = time.time_ns()
        elapsed_time = current_time - start_time
        s = format(round(elapsed_time / 1000000000, 3), '010.3f')
        lbl.config(text = s)
        
    elif (current_state == RESET):
        current_state = STOPPED
        s = format(0, '010.3f')
        print(s)
        lbl.config(text = s)
    lbl.after(1, update_time)
    
  
# Styling the label widget so that clock
# will look more attractive
lbl = Label(window, font = ('calibri', 240, 'bold'), background = 'purple', foreground = 'white')
  
# Placing clock at the centre
# of the tkinter window
#lbl.pack(anchor = 'center')
lbl.place(relx=0.05, rely=0.1, relheight = 0.8, relwidth=0.9)
update_time()


window.attributes('-fullscreen', True)

window.mainloop()
