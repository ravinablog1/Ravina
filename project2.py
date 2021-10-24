from tkinter import *
import pymysql
from tkinter import ttk

class NTHStudentsData:
    def _init_(self,root):
        self.root = root     #Main Window name is self.root
        self.root.title("NARAYANA Tech House")
        self.root.geometry("1350x680")   #(WidthxHight)

#Creating Lable
        title = Label(self.root, text="Welcome to NTH Students Info",
                      bd=5, relief = GROOVE, bg = "green", fg = "white",
                      font = ('ms sans serif', 30, 'bold'), )

        title.pack(fill=X, side=TOP)

        self.roll_no_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.course_var = StringVar()
        self.fee_var = StringVar()
        self.institute_var = StringVar()
        self.mobile_var = StringVar()
        self.email_var = StringVar()

        self.searchBy = StringVar()
        self.searchText = StringVar()

#Creating Frame for Form
        FormFrame = Frame(self.root,bg="green",bd=5,relief=GROOVE)
        FormFrame.place(x=10, y=60, height=600, width=400)

        title = Label(FormFrame, text = "Enter Students Data", bg="green", fg="white", font = ('ms sans serif', 20, 'bold') )
        title.grid(row=0, columnspan=2, padx=60, pady=20)

#Roll Number
        roll_no = Label(FormFrame,text="Roll No:", bg="green", fg="white", font = ('ms sans serif', 15, 'bold'))
        roll_no.grid(row=1, column=0, sticky='W', padx = 20)

        txt_roll_no = Entry(FormFrame, textvariable = self.roll_no_var, font = ('ms sans serif', 14, 'bold'))
        txt_roll_no.grid(row=1, column=1,pady=10,sticky='W')

#First Name
        first_name = Label(FormFrame,text="First Name:", bg="green", fg="white", font = ('ms sans serif', 15, 'bold'))
        first_name.grid(row=2, column=0, sticky='W', padx = 20)

        txt_first_name = Entry(FormFrame, textvariable = self.first_name_var, font = ('ms sans serif', 14, 'bold'))
        txt_first_name.grid(row=2, column=1, pady=10,sticky='W')


#Last Name
        last_name = Label(FormFrame,text="Last Name:", bg="green", fg="white", font = ('ms sans serif', 15, 'bold'))
        last_name.grid(row=3, column=0, sticky='W', padx = 20)

        txt_last_name = Entry(FormFrame, textvariable = self.last_name_var, font = ('ms sans serif', 14, 'bold'))
        txt_last_name.grid(row=3, column=1, pady=10,sticky='W')

#Course Name
        course = Label(FormFrame,text="Course:", bg="green", fg="white", font = ('ms sans serif', 15, 'bold'))
        course.grid(row=4, column=0, sticky='W', padx = 20)

        txt_course = Entry(FormFrame, textvariable=self.course_var,  font = ('ms sans serif', 14, 'bold'))
        txt_course.grid(row=4, column=1, pady=10,sticky='W')

#Institute Name
        institute = Label(FormFrame,text="Institute:", bg="green", fg="white", font = ('ms sans serif', 15, 'bold'))
        institute.grid(row=5, column=0, sticky='W', padx = 20)

        txt_institute = Entry(FormFrame, textvariable = self.institute_var, font = ('ms sans serif', 14, 'bold'))
        txt_institute.grid(row=5, column=1, pady=10,sticky='W')

#Fee
        fee = Label(FormFrame,text="Fee:", bg="green", fg="white", font = ('ms sans serif', 15, 'bold'))
        fee.grid(row=6, column=0, sticky='W', padx = 20)

        txt_fee = Entry(FormFrame, textvariable = self.fee_var, font = ('ms sans serif', 14, 'bold'))
        txt_fee.grid(row=6, column=1, pady=10,sticky='W')

#Email
        email = Label(FormFrame,text="Email:", bg="green", fg="white", font = ('ms sans serif', 15, 'bold'))
        email.grid(row=7, column=0, sticky='W', padx = 20)

        txt_email = Entry(FormFrame, textvariable = self.email_var, font = ('ms sans serif', 14, 'bold'))
        txt_email.grid(row=7, column=1, pady=10,sticky='W')

#Mobile
        mobile = Label(FormFrame,text="Mobile:", bg="green", fg="white", font = ('ms sans serif', 15, 'bold'))
        mobile.grid(row=8, column=0, sticky='W', padx = 20)

        txt_mobile = Entry(FormFrame, textvariable = self.mobile_var, font = ('ms sans serif', 14, 'bold'))
        txt_mobile.grid(row=8, column=1, pady=10,sticky='W')


#Creating buttons

        btn_frame = Frame(FormFrame, bd=4, relief = GROOVE, bg='green')
        btn_frame.place(x = 10, y = 470, width=370, height=70)

        btn_add = Button(btn_frame, text="Add", command = self.adding_data, font = ('ms sans serif', 12, 'bold'), width=6, bg='red', fg='white')
        btn_add.grid(row=0, column=0,padx=10, pady=10)

        btn_update = Button(btn_frame, text="Update", command = self.update_data, font = ('ms sans serif', 12, 'bold'), width=6, bg='blue', fg='white')
        btn_update.grid(row=0, column=1,padx=10, pady=10)

        btn_delete = Button(btn_frame, text="Delete", command = self.delete_data, font = ('ms sans serif', 12, 'bold'), width=6, bg='yellow', fg='red')
        btn_delete.grid(row=0, column=2,padx=10, pady=10)

        btn_clear = Button(btn_frame, text="Clear", command=self.clear, font = ('ms sans serif', 12, 'bold'), width=6, bg='pink', fg='blue')
        btn_clear.grid(row=0, column=3,padx=10, pady=10)

#Creating Frame For Table
        TableFrame = Frame(self.root,bg="green",bd=5,relief=GROOVE)
        TableFrame.place(x = 420 , y = 60, height=600, width=930)

        lbl_search = Label(TableFrame, text="Search By:", width=15, bg="green", fg="white",font = ('ms sans serif', 15, 'bold'))
        lbl_search.grid(row=0, column=0, pady=20)


        combo_search = ttk.Combobox(TableFrame, textvariable = self.searchBy, font = ('ms sans serif', 15, 'bold'), width=10)
        combo_search['values'] = ('course','institute')
        combo_search.grid(row=0, column=1, sticky="W")

        txt_search = Entry(TableFrame, textvariable = self.searchText, font = ('ms sans serif', 15, 'bold'), width=10)
        txt_search.grid(row=0, column=2, padx=40)

        btnSearch = Button(TableFrame, command = self.search_data, text="Search", bg="blue",fg="white", font = ('ms sans serif', 13, 'bold'), width=10)
        btnSearch.grid(row=0, column=3)

        btnShowAll = Button(TableFrame, command = self.fetching_data, text="Show All", bg="red",fg="white", font = ('ms sans serif', 13, 'bold'), width=10)
        btnShowAll.grid(row=0, column=4, padx=40)


#Creating Data Frame
        DataFrame = Frame(TableFrame, bd=5, relief = GROOVE)
        DataFrame.place(x=20, y=80, width=880, height=450)

        self.Student_Table = ttk.Treeview(DataFrame, columns=('roll_no','first_name','last_name','course','institute','fee','email', 'mobile'))
        self.Student_Table.heading('roll_no', text='Roll NO')
        self.Student_Table.heading('first_name', text='First Name')
        self.Student_Table.heading('last_name', text='Last Name')
        self.Student_Table.heading('course', text='Course')
        self.Student_Table.heading('institute', text='Institute')
        self.Student_Table.heading('fee', text='Fee')
        self.Student_Table.heading('mobile', text='Mobile')
        self.Student_Table.heading('email', text='Email')

        self.Student_Table['show'] = 'headings'

        self.Student_Table.column('roll_no', width=70, anchor = CENTER)
        self.Student_Table.column('first_name', width=100, anchor = CENTER)
        self.Student_Table.column('last_name', width=100, anchor = CENTER)
        self.Student_Table.column('course', width=120, anchor = CENTER)
        self.Student_Table.column('institute', width=100, anchor = CENTER)
        self.Student_Table.column('fee', width=100, anchor = CENTER)
        self.Student_Table.column('mobile', width=140, anchor = CENTER)
        self.Student_Table.column('email', width=140, anchor = CENTER)

        self.Student_Table.pack()
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetching_data()

    def adding_data(self):
            connection = pymysql.connect(host='localhost', user='root', password='root', db='nthstudentsinfo')
            cursor = connection.cursor()
            cursor.execute('insert into studentsdata values (%s, %s, %s, %s, %s, %s, %s, %s)',
                           (self.roll_no_var.get(),
                           self.first_name_var.get(),
                           self.last_name_var.get(),
                           self.course_var.get(),
                           self.institute_var.get(),
                           self.fee_var.get(),
                           self.email_var.get(),
                           self.mobile_var.get()
                           ))
            connection.commit()
            self.fetching_data()
            self.clear()
            connection.close()

    def fetching_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='root', db='nthstudentsinfo')
        cursor = connection.cursor()
        cursor.execute('select * from studentsdata')
        rows = cursor.fetchall()   #fetching all data from db
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END, values=row)
            connection.commit()
        connection.close()

    def clear(self):
        self.roll_no_var.set('')
        self.first_name_var.set('')
        self.last_name_var.set('')
        self.course_var.set('')
        self.institute_var.set('')
        self.fee_var.set('')
        self.email_var.set('')
        self.mobile_var.set('')

    def get_cursor(self,varA):
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.roll_no_var.set(row[0])
        self.first_name_var.set(row[1])
        self.last_name_var.set(row[2])
        self.course_var.set(row[3])
        self.institute_var.set(row[4])
        self.fee_var.set(row[5])
        self.email_var.set(row[6])
        self.mobile_var.set(row[7])


    def update_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='root', db='nthstudentsinfo')
        cursor = connection.cursor()
        cursor.execute('update studentsdata set first_name=%s, last_name=%s, course=%s, institute=%s, fee=%s, email=%s, mobile=%s where roll_no=%s',
                       (self.first_name_var.get(),
                       self.last_name_var.get(),
                       self.course_var.get(),
                       self.institute_var.get(),
                       self.fee_var.get(),
                       self.email_var.get(),
                       self.mobile_var.get(),
                       self.roll_no_var.get()
                       ))
        connection.commit()
        self.fetching_data()
        self.clear()
        connection.close()


    def delete_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='root', db='nthstudentsinfo')
        cursor = connection.cursor()
        cursor.execute('delete from studentsdata where roll_no=%s', self.roll_no_var.get())
        connection.commit()
        self.fetching_data()
        self.clear()
        connection.close()


    def search_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='root', db='nthstudentsinfo')
        cursor = connection.cursor()

        cursor.execute("select * from studentsdata where "+str(self.searchBy.get())+" like '%"+str(self.searchText.get())+"%'")


        rows = cursor.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END, values=row)
            connection.commit()
        connection.close()


















root = Tk()
obj = NTHStudentsData(root)
root.mainloop()
