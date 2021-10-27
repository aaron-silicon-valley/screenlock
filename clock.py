
import tkinter as tk
from tkinter import *

master = Tk()
# master.geometry('550x500+600+200')
master.resizable(False, False)
master.attributes('-fullscreen', True)
Label(master, text="First Name")
e1 = Entry(master)

e1.pack()

# button1 = Button(master, highlightbackground='red',
#                  text='Go',
#                  command=master.quit,
#                  width=10,
#                  height=10).grid()

def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    print(result)
    done = result.strip()
    if done == "hello":
        master.quit()
    else:
        pass




textExample=tk.Text(master, height=10)
textExample.pack()
btnRead=tk.Button(master, height=1, width=10, text="Read",
                    command=getTextInput)

btnRead.pack()




master.mainloop()
#
# # .grid(row=3,
# #                                     column=0,
# #                                     sticky=tk.W,
# #                                     pady=4,
# #                                     width=50)

# from tkinter import *
#
# tkWindow = Tk()
# tkWindow.geometry('400x150')
# tkWindow.title('Button Background Example')
#
# button = Button(tkWindow, text='Submit', bg='blue', fg='white')
# button.pack()
#
# tkWindow.mainloop()