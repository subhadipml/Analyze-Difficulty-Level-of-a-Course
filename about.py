from tkinter import *
import user
from tkinter import messagebox

master = Tk()
master.title('Analyze Difficulty Level of a Course')
master.config(bg="gold")
master.geometry("1150x600+0+0")

#---Start : Created Frame1 i.e. ( frame1 ) -----Store Infromation About Developer---#

frame1 = Frame(master, bg="gold")
frame1.pack(anchor=NW)
label1 = Label(frame1, text='Analyze Difficulty Level of a Course', font="Georgia 50 italic underline",bg="gold")
label1.grid(row=0, column=0, padx=20, pady=10)
label2 = Label(frame1, text='About Developer', font="Courier 35 bold",bg="gold")
label2.grid(row=1, column=0, padx=5)
image1 = PhotoImage(file="img/subhadip.gif")
Label(frame1, image=image1).grid(row=2,column=0, padx=5, pady=5)
label3 = Label(frame1, text='Name : Subhadip Mondal', font="Times 30 italic",bg="gold")
label3.grid(row=3, column=0, padx=5, pady=5)
label4 = Label(frame1, text='College : Lovely Professional University', font="Times 20",bg="gold")
label4.grid(row=4, column=0, padx=5)
label5 = Label(frame1, text='Course : B.Tech(CSE)', font="Times 20",bg="gold")
label5.grid(row=5, column=0, padx=5)
label6 = Label(frame1, text= 'GitHub Repository : https://github.com/subhadipml/Analyze-Difficulty-Level-of-a-Course', font="halston 15 underline", fg='blue',bg="gold")
label6.grid(row=6, column=0, padx=5)
label7 = Label(frame1, text='LinkedIn ID : https://www.linkedin.com/in/subhadipml/', font="halston 15 underline", fg='blue',bg="gold")
label7.grid(row=7, column=0, padx=5)

#---End : All information about the developer---#

#----User Input Function--------#
def user_input():
    master.destroy()
    ticket_obj = user.UserInput()
button1 = Button(frame1, text='Click To Enter User Input', font="halston 15 italic",cursor="hand2",bg="salmon", command=user_input)
button1.grid(row=8, column=0, pady=5)
#-----------------------------------#

master.mainloop()
