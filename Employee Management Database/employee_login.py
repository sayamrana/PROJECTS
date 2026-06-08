from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

from employee_Dashboard import EmployeeDashboard

def create_database_and_table():
    
    try:
    
        conn=mysql.connector.connect(host='localhost',user='root',password='',port=3307)
        cursor=conn.cursor()
        
        print("Connected Successfully")
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS employeeedb")
        cursor.execute("USE employeeedb")
        print("Database Created")

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users(
                        username VARCHAR(100)PRIMARY KEY,
                        password VARCHAR(100) NOT NULL
                    )
                    """)

        print("Table Created")
        cursor.execute("SELECT * FROM users  WHERE username='admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT  INTO users (username,password) VALUES ('admin','admin123')")
            conn.commit()
        conn.close()

    except Exception as err:
        print("ERROR:", err)
        messagebox.showerror("Database Error", str(err))


def user_login():
    root = Tk()
    root.geometry("400x450")
    root.title("Employee Management System")
    root.configure(bg="#8799ea")
    root.resizable(False, False)


    create_database_and_table()

    # Login Image
    img = Image.open("login_pic3.png")
    img = img.resize((100, 100), Image.LANCZOS)
    login_image = ImageTk.PhotoImage(img)

    Label(root, image=login_image).pack(pady=25)
    Label(root, text="USER LOGIN", font=("Arial",20,"bold"),fg="white",bg="#8799ea").pack()

    def clear_entry(e,entry,default,is_password=False):
        if entry.get() == default:
            entry.delete(0, END)
            entry.config(bg="white",fg="black")
            if is_password:
                entry.config(show="*")
    def restore_entry(e,entry,default,is_password=False):
        if not entry.get():
            entry.insert(0,default)
            entry.config(fg="gray",bg="white",show="")


    user_entry= Entry(root ,width=25,font=("Arial", 12), fg="grey", bg="white", relief=FLAT)
    user_entry.insert(0,"UserName")
    
    user_entry.bind("<FocusIn>",lambda e:clear_entry(e,user_entry,"UserName"))
    user_entry.bind("<FocusOut>",lambda e: restore_entry(e,user_entry,"UserName"))
    
    
    user_entry.pack(pady=25,ipady=3)
    
    user_Pss= Entry(root ,width=25,font=("Arial", 12), fg="grey", bg="white", relief=FLAT)
    user_Pss.insert(0,"Password")
    
    user_Pss.bind("<FocusIn>",lambda e:clear_entry(e,user_Pss,"Password",True))
    user_Pss.bind("<FocusOut>",lambda e: restore_entry(e,user_Pss,"Password",True))
    
    user_Pss.pack(ipady=3)
   
    def login():
        username = user_entry.get()
        password = user_Pss.get()
       
        if username in ("","UserName") or password in("", "Password"):
            messagebox.showerror("Error","Please fill all fields", parent=root)
            return
   
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='',port=3307,database="employeeedb")
            cursor=conn.cursor()
            
            cursor.execute("SELECT *  FROM  users WHERE username=%s AND password=%s",(username,password))
            result=cursor.fetchone()
            conn.close()
            
            if result:
                messagebox.showinfo("Success","Login Successfully",parent=root)
                root.withdraw()
                EmployeeDashboard(root)
                
            else:
                messagebox.showerror("Failed","Invalid Unsername or Password",parent=root)
            
            
        except Exception as e:
                messagebox.showerror("Error",f"Database Error :\n {str(e)}",parent=root)    
   
   
    Checkbutton(root,text="Remember Me",fg="white",bg="#8799ea"
                ,activeforeground="white", activebackground="#8799ea",selectcolor="#8799ea").place(x=40,y=320)
    
    forgot_pss=Label(root, text="Forgot Password",cursor="hand2", font=("Arial",10,"bold","underline"),fg="white",bg="#8799ea")
    forgot_pss.place(x=250,y=320)
    
    def forgot():
        messagebox.showinfo("Forgot Password ","Please contact your Admin.")
    
    forgot_pss.bind("<Button-1>",lambda e :forgot())
    
    
    Button(root, text="LOGIN", font=("Arial",15,"bold"),fg="white",bg="yellow",command=login,relief=FLAT).place(x=60, y=390, width=280, height=40)
    
    
    
    
    
    root.mainloop()

user_login()