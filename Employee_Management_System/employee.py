from tkinter import *

from tkinter import ttk
from tkinter import ttk as Treeview
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox 
conn=mysql.connector.connect(host='localhost',username='root',password='Sanatsqlsqlsanat18$',database='mydata')
from bs4 import BeautifulSoup
from datetime import *
import webbrowser
import time








class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x950+0+0")
        self.root.title('Employee Management System')

        #Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        
        









        # 1280x800
        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman', 37, 'bold'), fg='darkblue', bg='white')
        lbl_title.place(x=0, y=0,width=1280, height=50)
        # ========Time=========
        cdt = datetime.now()
        d=cdt.date()
        hr=cdt.hour
        minute=cdt.minute
        day=cdt.weekday()

        f=("Calibri",15,"bold","italic")

        def cidClock():
        	c_time=time.strftime("%H:%M:%S:%p")
        	clock.config(text=c_time)
        	clock.after(100,cidClock)

        clock=Label(root,font=("times",20,"bold"),bg="yellow", fg="red")
        clock.grid(row=1,column=0)
        clock.place(x=1100,y=10,width=150)
        cidClock()

       
        



        # =====Wish===
        if hr<12:
	        msg="Good Morning"
        elif hr<16:
	        msg="Good Afternoon"
        else:
	        msg="Good Evening"
        lab_wish=Label(root,text=msg,font=f,fg="red")
        lab_wish.place(x=1100,y=60,width=150)

        # logo
        img_logo=Image.open('college_images/emplogo.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)


        # #Confirmation
        # def confirm():
        #     answer=askyesno(title='confirmation',messagebox='Do you want to Exit??')
        #     if answer:
        #         root.destroy()
                
        # root.protocol("WM_DELETE_WINDOW",confirm)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=150,y=0,width=50,height=50)

        # Image frame
        img_frame=Frame(self.root,bd=2, relief=RIDGE,bg='white')
        img_frame.place(x=0,y=53, width=1100, height=140)

        # first
        img1=Image.open('college_images/emp5.png');
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)


        # second
        img_2=Image.open('college_images/emp2.png');
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2) 

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=450,y=0,width=520,height=160)
        
        # ========DATE=========
        cdt = datetime.now()
        d=cdt.date()
        lab_cdt=Label(self.root,text=d,font=f,fg="white",bg="black")
        lab_cdt.place(x=2,y=10)
        

        
        # third
        img_3=Image.open('college_images/emp3.png');
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=850,y=0,width=540,height=160)

        # Main Frame
        Main_frame=Frame(self.root,bd=2, relief=RIDGE,bg='lavender')
        Main_frame.place(x=10,y=200, width=1250, height=450)

        # Upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2, relief=RIDGE,bg='lightyellow',text='Employee Information',font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10,y=10, width=1230, height=225)

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('arial', 11, 'bold'), bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial', 11, 'bold'), width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','IT','Marketing','Operations','Finance','Sales','Clerk','Receptionist')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

         # Name
        lbl_Name=Label(upper_frame,font=('arial', 12, 'bold'),text='Name:',bg='white')
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # lbl_Designation
        lbl_designation=Label(upper_frame,font=('arial',12,'bold'),text='Designation:',bg='white')
        lbl_designation.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font=('arial',11,'bold'))
        txt_designation.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # Email
        lbl_email=Label(upper_frame,font=('arial',12,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        # Address
        lbl_address=Label(upper_frame,font=('arila',12,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        # Married
        lbl_married_status=Label(upper_frame,font=('arial',12,'bold'),text='Married Status:')
        lbl_married_status.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_married['value']=('Married', 'Unmarried')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        # Dob
        lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text='DOB:',bg='white')
        lbl_dob.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=3,padx=2,pady=7)

        # Doj
        lbl_doj=Label(upper_frame,font=('arial',12,'bold'),text='DOJ:',bg='white')
        lbl_doj.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=1,padx=2,pady=7)

        # ID Proof

        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state='readonly',font=('arial',12,'bold'),width=8)
        com_txt_proof['value']=("Select ID Proof","PAN CARD","AADHAR CARD","DRIVING LICENSE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        #gender
        lbl_gender=Label(upper_frame,font=('arial', 12, 'bold'),text='Gender:',bg='white')
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)
 
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state='readonly',font=('arial',12,'bold'),width=8)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #phone
        lbl_phone=Label(upper_frame,font=('arial', 12, 'bold'),text='Phone No:',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)  

        # # country
        lbl_country=Label(upper_frame,font=('arial', 12, 'bold'),text='Country:',bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)
 

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        # # CTC
        lbl_salary=Label(upper_frame,font=('arial', 12, 'bold'),text='Salary(CTC):',bg='white')
        lbl_salary.grid(row=2,column=4,sticky=W,padx=2,pady=7) 

        txt_salary=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_salary.grid(row=2,column=5,padx=2,pady=7)

        # Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1000,y=1, width=170, height=200)

        btn_add=Button(button_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),width=13,bg="blue",fg="white")
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=13,bg="blue",fg="white")
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=13,bg="blue",fg="white")
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=("arial",15,"bold"),width=13,bg="blue",fg="white")
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

      
        def my_open():
        	url = "http://registerappsakec.pythonanywhere.com/"
        	webbrowser.open_new(url)

        my_button =Button(root,text="Apply Leave", bg="blue", fg="white",
        cursor="hand2",font=6, width=30, height=1, command=my_open)
        my_button.grid(row=1, column=1,padx=800, pady=454)

        

            



       


       

        
       

       
        #down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='',font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10,y=235, width=1230, height=225)
        
        #Search Frame
        search_frame=LabelFrame(down_frame,bd=2, relief=RIDGE,bg='white',text='Search Employee',font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0,y=0, width=1470, height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #Search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Option","Phone","id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)


        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="Search",command=self.search_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)

    

        #============Employee Table===========
        #Table Frame
        table_frame=Frame(down_frame,bd=3, relief=RIDGE)
        table_frame.place(x=0,y=60, width=1220, height=130)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("degi",text="Designation")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("married",text="Married Status")
        self.employee_table.heading("dob",text="DOB")
        self.employee_table.heading("doj",text="DOJ")
        self.employee_table.heading("idproofcomb",text="ID Type")
        self.employee_table.heading("idproof",text="ID Proof")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("phone",text="Phone")
        self.employee_table.heading("country",text="Country")
        self.employee_table.heading("salary",text="Salary"
        
        
        
        
        
        
        )

        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100) 
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100) 
        self.employee_table.column("salary",width=100)
    
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #***************Functions Declarations***************
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Issue','All Fields are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Sanatsqlsqlsanat18$',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_designation.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_married.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_doj.get(),
                                                                                                                    self.var_idproofcomb.get(),
                                                                                                                    self.var_idproof.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_country.get(),
                                                                                                                    self.var_salary.get(),
        

                                                                                                            ))



                                                                                                        

                conn.commit()
                self.fetch_data()
                messagebox.showinfo('Success','Employee has be Added',parent=self.root)
                conn.close()
               
            except Exception as es:
                messagebox.showerror('Issue',f'Due To:{str(es)}',parent=self.root)

    
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Sanatsqlsqlsanat18$',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
    conn.close()

    #Get Cursor

    def get_cursor(self,event=""):
            cursor_row=self.employee_table.focus()
            content=self.employee_table.item(cursor_row)
            data=content['values']

            self.var_dep.set(data[0])  
            self.var_name.set(data[1])
            self.var_designation.set(data[2])
            self.var_email.set(data[3])
            self.var_address.set(data[4])
            self.var_married.set(data[5])
            self.var_dob.set(data[6])
            self.var_doj.set(data[7])
            self.var_idproofcomb.set(data[8])
            self.var_idproof.set(data[9])
            self.var_gender.set(data[10])
            self.var_phone.set(data[11])
            self.var_country.set(data[12])
            self.var_salary.set(data[13])
        
#update
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Issue','All Fields are Required')
        else:
            try:
                update=messagebox.askyesno('update','Are you sure update this employee data')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Sanatsqlsqlsanat18$',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(

                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_name.get(),
                                                                                                                                                        self.var_designation.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_married.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_doj.get(),
                                                                                                                                                        self.var_idproofcomb.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_country.get(),
                                                                                                                                                        self.var_salary.get(),
                                                                                                                                                        self.var_idproof.get()

                                                                                                                                                                 ))
                    
                else:
                    if not update:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee succesafully updated',parent=self.root)
                  
            except Exception as es:
                messagebox.showerror('Issue',f'Due To:{str(es)}',parent=self.root) 






    # Delete

    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror("Issue","All Fields are Required")
        
        else:
            try:
                Delete=messagebox.askyesno('Delete',"Are you Sure you wan't to Delete this employee",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Sanatsqlsqlsanat18$',database='mydata')
                    my_cursor=conn.cursor()
                    sql='delete from employee1 where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return 
                conn.commit()
                messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
                self.fetch_data()
                conn.close()
                    



            except Exception as es:
                messagebox.showerror('Issue',f'Due To:{str(es)}',parent=self.root)

    # Reset

    def reset_data(self):
        self.var_dep.set("Select Department")  
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("Male")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")


    # Search

    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option")

        else:
            try:
                 conn=mysql.connector.connect(host='localhost',username='root',password='Sanatsqlsqlsanat18$',database='mydata')
                 my_cursor=conn.cursor()
                 my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                 rows=my_cursor.fetchall()
                 if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                    conn.commit()
                    conn.close()
        
            except Exception as es:
                messagebox.showerror('Issue',f'Due To:{str(es)}',parent=self.root)











if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()