from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import tkinter as tk
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        title = Label(root, text="Manage Course Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)
        #=============Variables=======
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        
        
        #======Widget====
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style", 15, "bold"), bg="white") 
        lbl_courseName.place(x=10,y=60)
        
        lbl_Duration=Label(self.root,text="Duration",font=("goudy old style", 15, "bold"), bg="white") 
        lbl_Duration.place(x=10,y=100)
        
        lbl_Charges=Label(self.root,text="Charges",font=("goudy old style", 15, "bold"), bg="white") 
        lbl_Charges.place(x=10,y=140)
        
        lbl_Description=Label(self.root,text="Description",font=("goudy old style", 15, "bold"), bg="white") 
        lbl_Description.place(x=10,y=180)
        
        #=======Entry=====
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style", 15, "bold"), bg="lightyellow") 
        self.txt_courseName.place(x=150,y=60,width=200)
        
        self.txt_Duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style", 15, "bold"), bg="lightyellow") 
        self.txt_Duration.place(x=150,y=100,width=200)
        
        self.txt_Charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style", 15, "bold"), bg="lightyellow") 
        self.txt_Charges.place(x=150,y=140,width=200)
        
        self.txt_Description=Text(self.root,font=("goudy old style", 15, "bold"), bg="lightyellow") 
        self.txt_Description.place(x=150,y=180,width=500,height=130)
        
        
        #=========Button====
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        
        self.btn_update = Button(self.root,text="update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        
        self.btn_Delete = Button(self.root,text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2",command=self.delete)
        self.btn_Delete.place(x=390, y=400, width=110, height=40)
        
        self.btn_Clear = Button(self.root,text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",cursor="hand2",command=self.clear)
        self.btn_Clear.place(x=510, y=400, width=110, height=40)

#===search====
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style", 15, "bold"), bg="white") 
        lbl_search_courseName.place(x=720,y=60)
        
        self.var_search=StringVar()
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style", 15, "bold"), bg="lightyellow") 
        txt_search_courseName.place(x=870,y=60,width=180)
        btn_search = Button(self.root,text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",cursor="hand2",command=self.Search)
        btn_search.place(x=1070, y=60, width=120, height=28)
#==========content====
        self.C_Frame=Frame(self.root,bd=2,relief=RAISED)
        self.C_Frame.place(x=720, y=100, width=470, height=340)
         
        Scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        Scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"), xscrollcommand=Scrollx.set, yscrollcommand=Scrolly.set)
       
        Scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        Scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        Scrollx.config(command=self.CourseTable.xview)
        Scrolly.config(command=self.CourseTable.yview)



        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.Show()
 #============clear=========
    def clear(self): 
            self.Show()   
            self.var_course.set("")
            self.var_duration.set("")
            self.var_charges.set("")
            self.var_search.set("")
            self.txt_Description.delete("1.0",END)
            self.txt_courseName.config(state="normal")   
        
  #=================Delete=====      
    def delete(self):
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            try:
                    if self.var_course.get()=="":
                            messagebox.showerror("Error","coures Name should be required",parent=self.root)
                    else:
                            cur.execute("select * from course where name=?",(self.var_course.get(),))
                            row=cur.fetchone()
                            if row==None:
                                    messagebox.showerror("Error","please select course from the list first",parent=self.root)
                            else:
                                    op=messagebox.askyesno("Confirm","Do you really want todelete?",parent=self.root)
                                    if op==True:
                                            cur.execute("delete from course where name=?",(self.var_course.get(),))
                                            con.commit()
                                            messagebox.showinfo("Delete","Course deleted Succesfully",parent=self.root)
                                            self.clear()
                                            
            except Exception as ex:
                                    messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
            finally:
                    con.close()
            
        
        
    #=============================get_data==========
    def get_data(self,ev):
            self.txt_courseName.config(state="readonly")
            self.txt_courseName
            r=self.CourseTable.focus()
            content=self.CourseTable.item(r)
            row=content["values"]
           # print(row)
            self.var_course.set(row[1])
            self.var_duration.set(row[2])
            self.var_charges.set(row[3])
            #self.var_course.set(row[4])
            self.txt_Description.delete("1.0",END)
            self.txt_Description.insert(END,row[4])

   #=============================add==========        
           
    def add(self):
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            try:
                    if self.var_course.get()=="":
                            messagebox.showerror("Error","coures Name should be required",parent=self.root)
                    else:
                            cur.execute("select * from course where name=?",(self.var_course.get(),))
                            row=cur.fetchone()
                            if row!=None:
                                    messagebox.showerror("Error","Coures Name AlreadyPresent",parent=self.root)
                            else:
                                    cur.execute("insert into course (name, duration, charges, description) values(?,?,?,?)", (
                                            self.var_course.get(),
                                            self.var_duration.get(),
                                            self.var_charges.get(),
                                            self.txt_Description.get("1.0", END)
                                            ))

                                    con.commit()
                                    messagebox.showinfo("Success","Coures Added Successfully",parent=self.root) 
                                    self.Show()           
            except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
                    
           #==============================update=====         
                    
    def update(self):
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            try:
                    if self.var_course.get()=="":
                            messagebox.showerror("Error","coures Name should be required",parent=self.root)
                    else:
                            cur.execute("select * from course where name=?",(self.var_course.get(),))
                            row=cur.fetchone()
                            if row==None:
                                    messagebox.showerror("Error","Select Coures from list",parent=self.root)
                            else:
                                    cur.execute("UPDATE course SET duration=?, charges=?, description=? WHERE name=?", (
                                            self.var_duration.get(),
                                            self.var_charges.get(),
                                            self.txt_Description.get("1.0", END), 
                                            self.var_course.get()
                                            ))


                                    con.commit()
                                    messagebox.showinfo("Success","Coures Update Successfully",parent=self.root) 
                                    self.Show()           
            except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
    
    
    #==============  show
    def Show(self):
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            try:
                    cur.execute("select * from course ")
                    rows=cur.fetchall()
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    for row in rows:
                            self.CourseTable.insert("",END,values=row)             
            except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)      

#==============search===============
    def Search(self):
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            try:
                    cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
                    rows=cur.fetchall()
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    for row in rows:
                            self.CourseTable.insert("",END,values=row)             
            except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)      

if __name__ == "__main__":
    root = Tk()
    app =CourseClass(root)
    root.mainloop()
        
        
        
        