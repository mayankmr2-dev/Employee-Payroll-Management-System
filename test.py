from tkinter import*


class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.config(bg="#e6e6f2")
        self.root.geometry("1280x800+0+0")
        self.root.iconbitmap("payroll.ico")

##################### Main root Frames #############################################

        Frame1 = Frame(self.root, bd=2, relief=RIDGE)
        Frame1.place(x=5, y=80, width=700, height=700)

        Frame2 = Frame(self.root, bd=2, relief=RIDGE)
        Frame2.place(x=720, y=80, width=700, height=330)

        Frame3 = Frame(self.root, bd=2, relief=RIDGE)
        Frame3.place(x=720, y=420, width=700, height=360)

        LabelName = Label(self.root, text="EMPLOYEE PAYROLL SYSTEM", font=(
            'times', 30, 'bold'), bg="#004040", fg='#a9c9d6', anchor=CENTER, bd=2, relief=RIDGE)
        LabelName.place(x=0, y=0, relwidth=1)

################### Frame 1 - Employee Details #######################################

        NameFrame1 = Label(Frame1, text="Employee Details", font=(
            'times', 25, 'bold'), bg="#004040", fg="#a9c9d6", anchor=CENTER, bd=3, relief=RIDGE)
        NameFrame1.place(x=0, y=0, relwidth=1)

        Emp_code = Label(Frame1, text="Employee Code ", font=('times', 15))
        Emp_code.place(x=10, y=60)

        Emp_code = Entry(Frame1, relief=RIDGE, bd=3,
                         width=20, font=('times', 15), bg="#ffffb9")
        Emp_code.place(x=150, y=60)

        Emp_search = Button(Frame1, text="Search",
                            relief=GROOVE, bg="#25004a", fg="#ffffce", font=('times', 15), borderwidth=4)
        Emp_search.place(x=400, y=50)

        Designation = Label(Frame1, text="Designation ", font=('times', 15))
        Designation.place(x=10, y=110)

        Designation = Entry(Frame1, relief=RIDGE, bd=3,
                            width=15, font=('times', 15), bg="#ffffb9")
        Designation.place(x=150, y=110)

        Name = Label(Frame1, text="Name ", font=('times', 15))
        Name.place(x=10, y=160)

        Name = Entry(Frame1, relief=RIDGE, bd=3,
                     width=15, font=('times', 15), bg="#ffffb9")
        Name.place(x=150, y=160)

        Age = Label(Frame1, text="Age ", font=('times', 15))
        Age.place(x=10, y=210)

        Age = Entry(Frame1, relief=RIDGE, bd=3,
                    width=15, font=('times', 15), bg="#ffffb9")
        Age.place(x=150, y=210)

        Gender = Label(Frame1, text="Gender ", font=('times', 15))
        Gender.place(x=10, y=260)

        Gender = Entry(Frame1, relief=RIDGE, bd=3,
                       width=15, font=('times', 15), bg="#ffffb9")
        Gender.place(x=150, y=260)

        Email = Label(Frame1, text="Email ", font=('times', 15))
        Email.place(x=10, y=310)

        Email = Entry(Frame1, relief=RIDGE, bd=3,
                      width=15, font=('times', 15), bg="#ffffb9")
        Email.place(x=150, y=310)

        HiredLocation = Label(
            Frame1, text="Hired Location ", font=('times', 15))
        HiredLocation.place(x=10, y=360)

        HiredLocation = Entry(Frame1, relief=RIDGE, bd=3,
                              width=15, font=('times', 15), bg="#ffffb9")
        HiredLocation.place(x=150, y=360)

        Address = Label(Frame1, text="Address ", font=('times', 15))
        Address.place(x=10, y=410)

        Address = Text(Frame1, relief=RIDGE, bd=3,
                       width=40, height=6, font=('times', 15), bg="#ffffb9")
        Address.place(x=150, y=410)

        dob = Label(Frame1, text="D.O.B ", font=('times', 15))
        dob.place(x=400, y=110)

        dob = Entry(Frame1, relief=RIDGE, bd=3,
                    width=15, font=('times', 15), bg="#ffffb9")
        dob.place(x=500, y=110)

        doj = Label(Frame1, text="D.O.J ", font=('times', 15))
        doj.place(x=400, y=160)

        doj = Entry(Frame1, relief=RIDGE, bd=3,
                    width=15, font=('times', 15), bg="#ffffb9")
        doj.place(x=500, y=160)

        experience = Label(Frame1, text="Experience ", font=('times', 15))
        experience.place(x=400, y=210)

        experience = Entry(Frame1, relief=RIDGE, bd=3,
                           width=15, font=('times', 15), bg="#ffffb9")
        experience.place(x=500, y=210)

        proofid = Label(Frame1, text="Proof ID ", font=('times', 15))
        proofid.place(x=400, y=260)

        proofid = Entry(Frame1, relief=RIDGE, bd=3,
                        width=15, font=('times', 15), bg="#ffffb9")
        proofid.place(x=500, y=260)

        Contact = Label(Frame1, text="Contact ", font=('times', 15))
        Contact.place(x=400, y=310)

        Contact = Entry(Frame1, relief=RIDGE, bd=3,
                        width=15, font=('times', 15), bg="#ffffb9")
        Contact.place(x=500, y=310)

        Status = Label(Frame1, text="Status ", font=('times', 15))
        Status.place(x=400, y=360)

        Status = Entry(Frame1, relief=RIDGE, bd=3,
                       width=15, font=('times', 15), bg="#ffffb9")
        Status.place(x=500, y=360)

########################## Frame 2 - Employee Salary Details ##################

        Month = Label(Frame2, text="Month ", font=('times', 15))
        Month.place(x=10, y=10)

        Month = Entry(Frame2, relief=RIDGE, bd=3,
                      width=5, font=('times', 15), bg="#ffffb9")
        Month.place(x=80, y=10)

        Year = Label(Frame2, text="Year ", font=('times', 15))
        Year.place(x=160, y=10)

        Year = Entry(Frame2, relief=RIDGE, bd=3,
                     width=5, font=('times', 15), bg="#ffffb9")
        Year.place(x=220, y=10)

        # Basic_Salary = Label(Frame2, text="Basic Salary", font=('times', 15))
        # Basic_Salary.place(x=220, y=10)

        # Basic_Salary = Entry(Frame2, relief=RIDGE, bd=3,
        #                      width=5, font=('times', 15), bg="#ffffb9")
        # Basic_Salary.place(x=220, y=10)


root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
