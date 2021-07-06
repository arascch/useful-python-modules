import tkinter
from datetime import datetime

counter = 66600
running = False

def counter_label(label):
    def count():
        if running:
            global counter

            if counter == 66600:
                display = "Starting ..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string 
            
            label['text'] = display

            label.after(1000,count)
            counter+=1
    count()
#incomplete and wait for complete version
 