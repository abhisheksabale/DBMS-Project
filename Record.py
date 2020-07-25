from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time;
import datetime
import StudentDatabaseRecord

class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("Student Record Database System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        CourseCode = StringVar()
        CN = StringVar()
        TOC = StringVar()
        SDL = StringVar()
        ISEE = StringVar()
        SEPM = StringVar()
        DBMS = StringVar()
        PracCN = StringVar()
        PracDBMS = StringVar()
        ExamNo = StringVar()
        TotalScore = StringVar()
        Average = StringVar()
        Ranking = StringVar()
        DateIssued = StringVar()

        # =================================================Functions========================================================

        def Exit():
            qExit = tkinter.messagebox.askyesno("Quit System", "Do you wanna quit?")
            if qExit > 0:
                root.destroy()
                return

        def Clear():
            StdID.set("")
            Firstname.set("")
            Surname.set("")
            CourseCode.set("")
            CN.set("")
            TOC.set("")
            SDL.set("")
            ISEE.set("")
            SEPM.set("")
            DBMS.set("")
            PracCN.set("")
            PracDBMS.set("")
            ExamNo.set("")
            TotalScore.set("")
            Average.set("")
            Ranking.set("")
            self.txtUnitGrades.delete("1.0", END)

        def AddUnitScore():
            Unit1 = float(CN.get())
            Unit2 = float(TOC.get())
            Unit3 = float(SDL.get())
            Unit4 = float(ISEE.get())
            Unit5 = float(SEPM.get())
            Unit6 = float(DBMS.get())
            Unit7 = float(PracCN.get())
            Unit8 = float(PracDBMS.get())

            UnitTotal = (Unit1 + Unit2 + Unit3 + Unit4 + Unit5 + Unit6 + Unit7 + Unit8)
            UnitAverage = (Unit1 + Unit2 + Unit3 + Unit4 + Unit5 + Unit6 + Unit7 + Unit8)/8
            TotalScore.set(int(UnitTotal))
            Average.set(int(UnitAverage))

            if (UnitTotal >= 700):
                Ranking.set("Distinction")
            elif (UnitTotal >= 600):
                Ranking.set("First Class")
            elif (UnitTotal >= 500):
                Ranking.set("Second Class")
            elif (UnitTotal >= 400):
                Ranking.set("Third Class")
            elif (UnitTotal >= 300):
                Ranking.set("A.T.K.T.")
            elif (UnitTotal < 300):
                Ranking.set("Fail")

            DateIssued.set(time.strftime("%d/%m/%Y"))
            self.txtUnitGrades.insert(END, '=========-=====Transcript===============' + '\n')
            self.txtUnitGrades.insert(END, 'Student ID:\t\t' + StdID.get() + '\t\t' + DateIssued.get() + '\n')
            self.txtUnitGrades.insert(END, '======================================' + '\n')
            self.txtUnitGrades.insert(END, 'Firstname:\t\t\t\t' + Firstname.get() + '\n')
            self.txtUnitGrades.insert(END, 'Surname:\t\t\t\t' + Surname.get() + '\n')
            self.txtUnitGrades.insert(END, 'Course Code:\t\t\t\t' + CourseCode.get() + '\n')
            self.txtUnitGrades.insert(END, 'CN:\t\t\t\t' + CN.get() + '\n')
            self.txtUnitGrades.insert(END, 'TOC:\t\t\t\t' + TOC.get() + '\n')
            self.txtUnitGrades.insert(END, 'SDL:\t\t\t\t' + SDL.get() + '\n')
            self.txtUnitGrades.insert(END, 'ISEE:\t\t\t\t' + ISEE.get() + '\n')
            self.txtUnitGrades.insert(END, 'SEPM:\t\t\t\t' + SEPM.get() + '\n')
            self.txtUnitGrades.insert(END, 'DBMS:\t\t\t\t' + DBMS.get() + '\n')
            self.txtUnitGrades.insert(END, 'Prac CN\t\t\t\t' + PracCN.get() + '\n')
            self.txtUnitGrades.insert(END, 'Prac DBMS:\t\t\t\t' + PracDBMS.get() + '\n')
            self.txtUnitGrades.insert(END, '======================================' + '\n')
            self.txtUnitGrades.insert(END, 'Total Score:\t\t\t\t' + TotalScore.get() + '\n')
            self.txtUnitGrades.insert(END, 'Average:\t\t\t\t' + Average.get() + '\n')
            self.txtUnitGrades.insert(END, 'Ranking:\t\t\t\t' + Ranking.get() + '\n')
            self.txtUnitGrades.insert(END, '======================================' + '\n')

        #======================================Database Functios========================================================

        def addData():
            AddUnitScore()
            if(len(StdID.get())!=0):
                StudentDatabaseRecord.addStdRec(StdID.get(), Firstname.get(), Surname.get(), CourseCode.get(), CN.get(), TOC.get(), SDL.get(), ISEE.get(), SEPM.get(), DBMS.get(), PracCN.get(), PracDBMS.get(), TotalScore.get(), Average.get(), Ranking.get())
                studentlist.delete(0,END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), CourseCode.get(), CN.get(), TOC.get(), SDL.get(), ISEE.get(), SEPM.get(), DBMS.get(), PracCN.get(), PracDBMS.get(), TotalScore.get(), Average.get(), Ranking.get()))

        def DisplayData():

            studentlist.delete(0, END)
            for row in StudentDatabaseRecord.viewData():
                studentlist.insert(END, row, str(""))

        def DeleteData():
            if (len(StdID.get()) != 0):
                StudentDatabaseRecord.deleteRec(sd[0])
                Clear()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in StudentDatabaseRecord.searchData(StdID.get(), Firstname.get(), Surname.get(), CourseCode.get(), CN.get(), TOC.get(), SDL.get(), ISEE.get(), SEPM.get(), DBMS.get(), PracCN.get(), PracDBMS.get(), TotalScore.get(), Average.get(), Ranking.get()):
                studentlist.insert(END, row, str(""))

        def update():
            if (len(StdID.get()) != 0):
                StudentDatabaseRecord.deleteRec(sd[0])
            if (len(StdID.get()) != 0):
                StudentDatabaseRecord.addStdRec(StdID.get(), Firstname.get(), Surname.get(), CourseCode.get(), CN.get(), TOC.get(), SDL.get(), ISEE.get(), SEPM.get(), DBMS.get(), PracCN.get(), PracDBMS.get(), TotalScore.get(), Average.get(), Ranking.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), CourseCode.get(), CN.get(), TOC.get(), SDL.get(),ISEE.get(), SEPM.get(), DBMS.get(), PracCN.get(), PracDBMS.get(), TotalScore.get(), Average.get(),Ranking.get()))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtFirstname.delete(0, END)
            self.txtFirstname.insert(END, sd[2])
            self.txtSurname.delete(0, END)
            self.txtSurname.insert(END, sd[3])
            self.txtCourseCode.delete(0, END)
            self.txtCourseCode.insert(END, sd[4])
            self.txtCN.delete(0, END)
            self.txtCN.insert(END, sd[5])
            self.txtTOC.delete(0, END)
            self.txtTOC.insert(END, sd[6])
            self.txtSDL.delete(0, END)
            self.txtSDL.insert(END, sd[7])
            self.txtISEE.delete(0, END)
            self.txtISEE.insert(END, sd[8])
            self.txtSEPM.delete(0, END)
            self.txtSEPM.insert(END, sd[9])
            self.txtDBMS.delete(0, END)
            self.txtDBMS.insert(END, sd[10])
            self.txtPracCN.delete(0, END)
            self.txtPracCN.insert(END, sd[11])
            self.txtPracDBMS.delete(0, END)
            self.txtPracDBMS.insert(END, sd[12])
            self.txtTotalScore.delete(0, END)
            self.txtTotalScore.insert(END, sd[13])
            self.txtAverage.delete(0, END)
            self.txtAverage.insert(END, sd[14])
            self.txtRanking.delete(0, END)
            self.txtRanking.insert(END, sd[15])


        #=================================================Frames========================================================

        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame.pack(side = TOP)

        DataFrame2 = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame2.pack(side=BOTTOM)

        ButtonFrame = Frame(DataFrame2, bd=2, width=1350, height=40, padx=18, pady=10, relief=RIDGE, bg="medium aquamarine")
        ButtonFrame.pack(side=BOTTOM)

        ListFrame = Frame(DataFrame2, bd=2, width=1350, height=180, padx=18, pady=10, relief=RIDGE, bg="medium aquamarine")
        ListFrame.pack(side=TOP)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=900, height=200, padx=20, relief=RIDGE, bg="Ghost White",
                                   font = ('Arial', 18, 'bold'), text = "Student Details\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=200, padx=31, pady=3, relief=RIDGE, bg="medium aquamarine",
                                    font = ('Arial', 18, 'bold'), text = "Semester Result\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #===============================================Widgets==================================================================

        self.lblStdID = Label(DataFrameLEFT, font = ('Arial', 14, 'bold'), text = "Student ID", padx = 2, pady = 2, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font = ('Arial', 14, 'bold'), textvariable =StdID, bg="Ghost White", width=28)
        self.txtStdID.grid(row=0, column=1)

        self.lblCN = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="CN", padx=2, pady=2, bg="Ghost White")
        self.lblCN.grid(row=0, column=2, sticky=W)
        self.txtCN = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=CN, bg="Ghost White", width=28)
        self.txtCN.grid(row=0, column=3)

        self.lblCourseCode = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Course Code", padx=2, pady=2, bg="Ghost White")
        self.lblCourseCode.grid(row=1, column=0, sticky=W)
        self.txtCourseCode = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=CourseCode, bg="Ghost White", width=28)
        self.txtCourseCode.grid(row=1, column=1)
        '''self.cboCourseCobe = ttk.Combobox(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=CourseCode, state='readonly', width=26)
        self.cboCourseCobe['value']=('', '215001', '215002', '215003', '215004', '215005', '215006')
        self.cboCourseCobe.current(1)
        self.cboCourseCobe.grid(row=1, column=1, padx=20, pady=3)'''

        self.lblISEE = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="ISEE", padx=2, pady=2, bg="Ghost White")
        self.lblISEE.grid(row=1, column=2, sticky=W)
        self.txtISEE = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=ISEE, bg="Ghost White", width=28)
        self.txtISEE.grid(row=1, column=3)

        self.lblFirstname = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="First Name", padx=2, pady=2, bg="Ghost White")
        self.lblFirstname.grid(row=2, column=0, sticky=W)
        self.txtFirstname = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Firstname, bg="Ghost White", width=28)
        self.txtFirstname.grid(row=2, column=1)

        self.lblTOC = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="TOC", padx=2, pady=2, bg="Ghost White")
        self.lblTOC.grid(row=2, column=2, sticky=W)
        self.txtTOC = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=TOC, bg="Ghost White", width=28)
        self.txtTOC.grid(row=2, column=3)

        self.lblSurname = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Surname", padx=2, pady=2, bg="Ghost White")
        self.lblSurname.grid(row=3, column=0, sticky=W)
        self.txtSurname = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Surname, bg="Ghost White", width=28)
        self.txtSurname.grid(row=3, column=1)

        self.lblSDL = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="SDL", padx=2, pady=2, bg="Ghost White")
        self.lblSDL.grid(row=3, column=2, sticky=W)
        self.txtSDL = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=SDL, bg="Ghost White", width=28)
        self.txtSDL.grid(row=3, column=3)

        self.lblExamNo = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Exam No", padx=2, pady=2, bg="Ghost White")
        self.lblExamNo.grid(row=4, column=0, sticky=W)
        self.txtExamNo = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=ExamNo, bg="Ghost White", width=28)
        self.txtExamNo.grid(row=4, column=1)

        self.lblSEPM = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="SEPM", padx=2, pady=2, bg="Ghost White")
        self.lblSEPM.grid(row=4, column=2, sticky=W)
        self.txtSEPM = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=SEPM, bg="Ghost White", width=28)
        self.txtSEPM.grid(row=4, column=3)

        self.lblTotalScore = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Total Score", padx=2, pady=2, bg="Ghost White")
        self.lblTotalScore.grid(row=5, column=0, sticky=W)
        self.txtTotalScore = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=TotalScore, bg="Ghost White", width=28)
        self.txtTotalScore.grid(row=5, column=1)

        self.lblDBMS = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="DBMS", padx=2, pady=2, bg="Ghost White")
        self.lblDBMS.grid(row=5, column=2, sticky=W)
        self.txtDBMS = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=DBMS, bg="Ghost White", width=28)
        self.txtDBMS.grid(row=5, column=3)

        self.lblAverage = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Average", padx=2, pady=2, bg="Ghost White")
        self.lblAverage.grid(row=6, column=0, sticky=W)
        self.txtAverage = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Average, bg="Ghost White", width=28)
        self.txtAverage.grid(row=6, column=1)

        self.lblPracCN = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Prac CN", padx=2, pady=2, bg="Ghost White")
        self.lblPracCN.grid(row=6, column=2, sticky=W)
        self.txtPracCN = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=PracCN, bg="Ghost White", width=28)
        self.txtPracCN.grid(row=6, column=3)

        self.lblRanking = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Ranking", padx=2, pady=2, bg="Ghost White")
        self.lblRanking.grid(row=7, column=0, sticky=W)
        self.txtRanking = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=Ranking, bg="Ghost White", width=28)
        self.txtRanking.grid(row=7, column=1)

        self.lblPracDBMS = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text="Prac DBMS", padx=2, pady=2, bg="Ghost White")
        self.lblPracDBMS.grid(row=7, column=2, sticky=W)
        self.txtPracDBMS = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=PracDBMS, bg="Ghost White", width=28)
        self.txtPracDBMS.grid(row=7, column=3)

        #=========================================UnitGrades============================================================

        self.txtUnitGrades = Text(DataFrameRIGHT, height = 13, width = 43, bd=1, font =('Arial', 11, 'bold'))
        self.txtUnitGrades.grid(row=0, column=0)

        #==========================================ListFrames===========================================================

        scrollbar = Scrollbar(ListFrame)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(ListFrame, width = 141, height = 7, font=('Arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)

        # ============================================buttons========================================================

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 12, 'bold'), height=1, width=16, bd=2, padx=13, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 12, 'bold'), height=1, width=16, bd=2, padx=8, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 12, 'bold'), height=1, width=16, bd=2, padx=8, command=Clear)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 12, 'bold'), height=1, width=16, bd=2, padx=8, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 12, 'bold'), height=1, width=16, bd=2, padx=8, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 12, 'bold'), height=1, width=16, bd=2, padx=8, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 12, 'bold'), height=1, width=16, bd=2, padx=12, command=Exit)
        self.btnExit.grid(row=0, column=6)


if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()