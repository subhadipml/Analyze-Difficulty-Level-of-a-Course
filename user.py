from tkinter import *

#-------Created A GUI based interface to input user details-----#
class UserInput:
    def __init__(self):
        master = Tk()
        master.title('Predict Difficulty Level')
        master.config(bg="gold")
        master.geometry("1000x600+0+0")

        self.frame1 = Frame(master, bg="cyan")
        self.frame1.place(x=80, y=50)

        self.label1 = Label(self.frame1, text='Predict the Difficulty Level of Course ', font="Courier 25 italic bold underline",bg="cyan")
        self.label1.grid(row=0, columnspan=10)

        #---Couse Name-------------#
        self.label2 = Label(self.frame1, text='Course Name : ', font="bold 15",bg="cyan")
        self.label2.grid(row=1, column=0,  pady=10)
        self.Course_Name = StringVar(self.frame1)
        self.entry1 = Entry(self.frame1, textvariable=self.Course_Name, font="bold 20")
        self.entry1.grid(row=1, column=1, ipadx=30, ipady=2)
        #--------------------------#

        #-----CA_1--------------#
        self.label3 = Label(self.frame1, text='CA_1 Marks (0-100) : ',font="Times 15",bg="cyan")
        self.label3.grid(row=2, column=0, pady=5)
        self.CA_1 = IntVar(self.frame1)
        self.entry2 = Entry(self.frame1, textvariable=self.CA_1, font="10")
        self.entry2.grid(row=2, column=1, ipadx=30, ipady=3, pady=5)
        #------------------------#

        #-----CA_2--------------#
        self.label4 = Label(self.frame1, text='CA_2 Marks (0-100) : ',font="Times 15",bg="cyan")
        self.label4.grid(row=3, column=0, pady=5)
        self.CA_2 = IntVar(self.frame1)
        self.entry3 = Entry(self.frame1, textvariable=self.CA_2, font="10")
        self.entry3.grid(row=3, column=1, ipadx=30, ipady=3, pady=5)
        #------------------------#

        #-----CA_3--------------#
        self.label5 = Label(self.frame1, text='CA_3 Marks (0-100) : ',font="Times 15",bg="cyan")
        self.label5.grid(row=4, column=0, pady=5)
        self.CA_3 = IntVar(self.frame1)
        self.entry4 = Entry(self.frame1, textvariable=self.CA_3, font="10")
        self.entry4.grid(row=4, column=1, ipadx=30, ipady=3, pady=5)
        #------------------------#

        #-----CA_4--------------#
        self.label6 = Label(self.frame1, text='CA_4 Marks (0-100) : ',font="Times 15",bg="cyan")
        self.label6.grid(row=5, column=0, pady=5)
        self.CA_4 = IntVar(self.frame1)
        self.entry5 = Entry(self.frame1, textvariable=self.CA_4, font="10")
        self.entry5.grid(row=5, column=1, ipadx=30, ipady=3, pady=5)
        #------------------------#

        #---Course Attendance-------------#
        self.label7 = Label(self.frame1, text='Course Attendance (0-100) : ', font="Times 15",bg="cyan")
        self.label7.grid(row=6, column=0,  pady=5)
        self.Course_Att = IntVar(self.frame1)
        self.entry6 = Entry(self.frame1, textvariable=self.Course_Att, font="10")
        self.entry6.grid(row=6, column=1, ipadx=30, ipady=3, pady=5)
        #--------------------------#

        #-----CA_100--------------#
        self.label8 = Label(self.frame1, text='CA_100 Marks (0-100) : ',font="Times 15",bg="cyan")
        self.label8.grid(row=7, column=0, pady=5)
        self.CA_100 = IntVar(self.frame1)
        self.entry7 = Entry(self.frame1, textvariable=self.CA_100, font="10")
        self.entry7.grid(row=7, column=1, ipadx=30, ipady=3, pady=5)
        #------------------------#

        #-----MTT_50--------------#
        self.label9 = Label(self.frame1, text='MTT_50 Marks (0-50) : ',font="Times 15",bg="cyan")
        self.label9.grid(row=8, column=0, pady=5)
        self.MTT_50 = IntVar(self.frame1)
        self.entry8 = Entry(self.frame1, textvariable=self.MTT_50, font="10")
        self.entry8.grid(row=8, column=1, ipadx=30, ipady=3, pady=5)
        #------------------------#

        #-----ETT_100--------------#
        self.label10 = Label(self.frame1, text='ETT Marks (0-100) : ',font="Times 15",bg="cyan")
        self.label10.grid(row=9, column=0, pady=5)
        self.ETT_100 = IntVar(self.frame1)
        self.entry9 = Entry(self.frame1, textvariable=self.ETT_100, font="10")
        self.entry9.grid(row=9, column=1, ipadx=30, ipady=3, pady=5)
        #------------------------#

        #--------ETP_100-----------#
        self.label11 = Label(self.frame1, text='ETP Marks (0-100) : ',font="Times 15",bg="cyan")
        self.label11.grid(row=10, column=0, pady=5)
        self.ETP_100 = IntVar(self.frame1)
        self.entry10 = Entry(self.frame1, textvariable=self.ETP_100, font="10")
        self.entry10.grid(row=10, column=1, ipadx=30, ipady=3, pady=5)
        #------------------------#
    
        #---------Predict Button------------#
        self.button1 = Button(self.frame1, text='Click To Predict Difficulty Level', font="halston 15 italic",cursor="hand2",bg="salmon", command=self.predict_difficulty)
        self.button1.grid(row=11, column=0, columnspan=5, ipady=3, pady=5)
        #-----------------------------------#

        #---------Developer Page------------#
        self.button1 = Button(self.frame1, text='Click To Know About Developer', font="halston 15 italic",cursor="hand2",bg="salmon", command=self.developer)
        self.button1.grid(row=11, column=2, columnspan=5, ipady=3, pady=5)
        #-----------------------------------#

        master.mainloop()

    #-----Function which predict the Difficulty level of course-------#
    def predict_difficulty(self):
        from tkinter import messagebox
        try:
            import pickle
            km = pickle.load(open( "km.sav", "rb" ))
            # fetch the Entered user input data
            user_input = [self.CA_100.get(), self.MTT_50.get(), self.ETT_100.get(), self.ETP_100.get(), self.Course_Att.get(), self.CA_1.get(), self.CA_2.get(), self.CA_3.get(), self.CA_4.get()]
            # Predict from the user input data
            y_p = km.predict([user_input])
            level = FALSE
            if y_p == 0:
                lavel = 'Difficult'
            elif y_p == 1:
                lavel = 'Easy'
            else:
                lavel = 'Medium'
            messagebox.showinfo("Model Predicted Difficulty Level", "Course Name : "+self.Course_Name.get()+"\n"+" Difficulty Level : "+lavel)
        except:
            messagebox.showerror("Error", "Please Enter Valid Input!!!")
        UserInput()
    #-------------------------------------#
    def developer(self):
        import os
        os.system("python about.py")
