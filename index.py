from tkinter import *
from tkinter import ttk
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1250x700+0+0")
        self.root['bg']='black'

        title=Label(self.root,text="Student Management System",bd=10,font=("times new roman",40,"bold"),bg="grey")
        title.pack(side=TOP,fill=X)

        #********************Manage Frame*******************#

        Manage_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="grey")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_Frame,text="Manage Students",bg="grey",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_name=Label(Manage_Frame,text="Name",bg="grey",font=("times new roman",15,"bold"))
        lbl_name.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,font=("times new roman",10,"bold"),bd=5,relief=RAISED)
        txt_name.grid(row=1,column=1,pady=10,padx=20,sticky="w")
         
        lbl_roll=Label(Manage_Frame,text="Roll no.",bg="grey",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,font=("times new roman",10,"bold"),bd=5,relief=RAISED)
        txt_roll.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_course=Label(Manage_Frame,text="Course",bg="grey",font=("times new roman",15,"bold"))
        lbl_course.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        combo_course=ttk.Combobox(Manage_Frame,font=("times new roman",9,"bold"),state='readonly')
        combo_course['values']=('BCA','BBA','BCOM')
        combo_course.grid(row=3,column=1,padx=20,pady=10)    

        lbl_email=Label(Manage_Frame,text="Email",bg="grey",font=("times new roman",15,"bold"))
        lbl_email.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,font=("times new roman",10,"bold"),bd=5,relief=RAISED)
        txt_email.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender",bg="grey",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",9,"bold"),state='readonly')
        combo_gender['values']=('Male','Female','Others')
        combo_gender.grid(row=5,column=1,padx=20,pady=10)    

        lbl_contact=Label(Manage_Frame,text="Contact",bg="grey",font=("times new roman",15,"bold"))
        lbl_contact.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,font=("times new roman",10,"bold"),bd=5,relief=RAISED)
        txt_contact.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="grey",font=("times new roman",15,"bold"))
        lbl_dob.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(Manage_Frame,font=("times new roman",10,"bold"),bd=5,relief=RAISED)
        txt_dob.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address",bg="grey",font=("times new roman",15,"bold"))
        lbl_address.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        txt_address=Text(Manage_Frame,width=25,height=4,font=("times new roman",10))
        txt_address.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        #*********************Button*****************#

        btn_Frame=Frame(Manage_Frame,bd=3,relief=FLAT,bg="black")
        btn_Frame.place(x=15,y=520,width=400)

        Addbtn=Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=9,pady=9)
        updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=9,pady=9)
        deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=9,pady=9)
        clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=9,pady=9)


        #********************Detail Frame*******************#

        Detail_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="grey")
        Detail_Frame.place(x=500,y=100,width=800,height=600)

        lbl_search=Label(Detail_Frame,text="Search",bg="grey",fg="White",font=("times new roman",10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values']=('Roll no.','Name','Contact')
        combo_search.grid(row=0,column=1,padx=10,pady=5)

        txt_search=Entry(Detail_Frame,font=("times new roman",10,"bold"),bd=5,relief=RAISED)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10).grid(row=0,column=4,padx=10,pady=10)

        #******************Table Frame*********************#

        Table_Frame=Frame(Detail_Frame,bd=4,relief=GROOVE,bg="white")
        Table_Frame.place(x=13,y=50,width=760,height=520)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Student_table=ttk.Treeview(Table_Frame,columns=("name","roll","course","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("name",text="Name")
        Student_table.heading("roll",text="Rollno.")
        Student_table.heading("course",text="Course")
        Student_table.heading("email",text="Email")
        Student_table.heading("gender",text="Gender")
        Student_table.heading("contact",text="Contact")
        Student_table.heading("dob",text="D.O.B")
        Student_table.heading("address",text="Address")
        Student_table['show']='headings'
        Student_table.pack(fill=BOTH,expand=1)

root=Tk()
ob=Student(root)
root.mainloop()