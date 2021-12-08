import tkinter
import random
import  winsound
from tkinter import messagebox
winsound.PlaySound("2.wav",winsound.SND_ASYNC)

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()
def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: "
                              + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        messagebox.showinfo("Time Over", "Your Score is "
                                            +str(score))

root = tkinter.Tk()
root.title("Color Game Akshay's Device")
root.geometry("1095x702")
root.maxsize(1095,700)
root.minsize(1095,700)

photo=tkinter.PhotoImage(file="1.png")
image=tkinter.Label(image=photo)
instructions = tkinter.Label(root, text="Type colour of the words,",font=('Helvetica', 20))
instructions.pack(pady=20)
# instructions1 = tkinter.Label(root, text="and not the word text!",font=('Helvetica', 20))
# instructions1.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start",font=('Helvetica', 20))
scoreLabel.pack(pady=0)
timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 25))
timeLabel.pack()

label = tkinter.Label(root, font=('Univers', 150),bd=2,text="Start..")
label.pack()
#def ntr():
e = tkinter.Entry(root,width=12,bd=4,text="Press Enter",bg="WHITE",font=('Helvetica',20),relief='solid')
image.place(x=1,y=0)
root.bind('<Return>', startGame)
e.pack(pady=100)
e.focus_set()


#btn=tkinter.Button(root,text="Try again...!",command=ntr)
#btn.pack()



root.mainloop()
