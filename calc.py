import tkinter as tk
'''Imports tkinter module
tk is an alias for easy access'''

#button click handler
def press(v):
    entry.insert(tk.END,v)
    '''called when a number or operator button is clicked
    Inserts the pressed value at the end of the entry Widget'''

def clear():
    entry.delete(0,tk.END)
    '''Clears the calculator screen
    Delets all characters from starting to end(index numbers)'''
def bspace():
    entry.delete(len(entry.get()) - 1, tk.END)
#Calculation function
def calc():
    try:
        result = eval(entry.get())
        '''entry.get() retrives the express e.g.(2+6)
        eval() evaluates the string as a python expression'''
        
        entry.delete(0,tk.END)#clears the old expression
        entry.insert(0,result)#Displays exception instesd of crashing
    
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"INVALID EXPRESSION")
        '''Handles invalid expression
        Displays exception instead of handling'''

#Main window Creation
root=tk.Tk()#main window
root.title("Calculator")#title
root.configure(bg="gray")#background color 
root.resizable(False,False)#can't resize disables resizinng of window
entry = tk.Entry(
    root,
    font=("sens-serif",20),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)

'''Text input field
Acts as a calculator display
Right-aligned for better calculator look'''

entry.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)

#Buttons Labels
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "3","2","1","-",
    "0",".","=","+",
]
'''To reduce repetitive code'''
#dynamic button creation
r=1
c=0
'''Rows and columns counter for grid layout'''

for b in buttons:
    cmd = calc if b== "="  else lambda x=b: press(x)
    '''if button is"=" ,call calc()
    else, call press() with the button value
    lambda x=b prevents late binding issues'''

    tk.Button(
        root,
        text=b, 
        command=cmd,#these three lines creates a button widget
        font=("Calibri",14),
        width=5,
        height=2,
        bg="#5de1f2" if b in "+-*/" else "black",
        fg="black" if b in "+-*/" else "white",
        bd=0
    ).grid(row=r,column=c,padx=6,pady=6)
    c+=1
    if c==4:
        r+=1
        c=0
        '''moves to next row after 4 buttons'''

#clear Button

tk.Button(
    root,
    text="Clear",
    command=clear,
    font=("calibri",14),
    width=15,
    height=2,
    bg="#5de1f2",
    fg="black",
    bd=0
).grid(row=r,column=0,columnspan=2,pady=5)
'''Clears the calculator display screen
spans across all columns'''

tk.Button(
    root,
    text="Backspace",
    command=bspace,
    font=("calibri",14),
    width=15,
    height=2,
    bg="#5de1f2",
    fg="black",
    bd=0
).grid(row=r,column=2,columnspan=2,pady=5)

#Event loop
root.mainloop()
'''Keeps the window running 
listens for user interactions.'''
