from tkinter import *

window = Tk()
window.geometry("350x350")
window.config(bg='black') # delete if need to white

clicks = 0

Label(text='CPS Test', font=('Tahoma', 20), bg='black', fg='gray').pack() # remove fg and bg property if need white
cpsLabel = Label(text='CPS: ' + str(clicks), fg='gray', bg='black', font=('Tahoma', 18)) # remove fg and bg property if need white
cpsLabel.pack()

def click(event):
    global clicks
    cpsLabel.config(text=f'CPS: {clicks}')
    clicks += 1

def reset(event):
    global clicks
    clicks = 0

window.bind('<Button-1>', click)
window.bind('<Button-2>', reset)

window.mainloop()
