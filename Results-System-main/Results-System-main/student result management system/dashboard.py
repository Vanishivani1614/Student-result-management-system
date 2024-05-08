from tkinter import *
from tkinter import Label, LabelFrame, Button, PhotoImage
from PIL import Image, ImageTk
from Course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.config(bg="white")
        
        title = Label(self.root, text="Student Result Management System", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=5, relwidth=1)
  
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=30, y=70,width=1470, height=80)
        
        btn_course = Button(M_Frame,text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.add_course)
        btn_course.place(x=40, y=5, width=200, height=40)
        
        btn_student = Button(M_Frame,text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.add_student)
        btn_student.place(x=280, y=5, width=200, height=40)
        
        btn_result = Button(M_Frame,text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.add_result)
        btn_result.place(x=520, y=5, width=200, height=40)
        
        btn_view = Button(M_Frame,text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.add_report)
        btn_view.place(x=760, y=5, width=200, height=40)
        
        btn_logout = Button(M_Frame,text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.logout)
        btn_logout.place(x=1000, y=5, width=200, height=40)
        
        btn_exit = Button(M_Frame,text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.exit_)
        btn_exit.place(x=1240, y=5, width=200, height=40)
        
        self.bg_img=Image.open("photo1.jpeg")
        self.bg_img=self.bg_img.resize((920,350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img)
        self.lbl_bg.place(x=580,y=200,width=920,height=350)
        
        
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style", 20),bd=10,relief=RAISED,bg="#e43b06",fg="white")
        self.lbl_course.place(x=580,y=560,width=300,height=100)
        
        self.lbl_student=Label(self.root,text="Total Courses\n[0]",font=("goudy old style", 20),bd=10,relief=RAISED,bg="#0676ad",fg="white")
        self.lbl_student.place(x=890,y=560,width=300,height=100)
        
        self.lbl_result=Label(self.root,text="Total Result\n[0]",font=("goudy old style", 20),bd=10,relief=RAISED,bg="#038074",fg="white")
        self.lbl_result.place(x=1200,y=560,width=300,height=100)
        
        
        footer=Label(self.root,text="SRMS:- Student Result Managment System\n Contact Us for Technical Issue: ",font=("goudy old style", 12 ), bg="#262626", fg="white")
        footer.pack(side=BOTTOM,fill=X)
        
        self.update_details()
        
    def update_details(self):   
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            
            cur.execute("select * from student ")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
          
            cur.execute("select * from result ")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            
            
            
            self.lbl_student.after(200,self.update_details)
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
        
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)
        
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
            
    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            
            
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
