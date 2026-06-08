from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
import mysql.connector


class EmployeeDetails:

    def __init__(self):
        # Constructor runs automatically when object is created
        self.create_database_and_table()

    def create_database_and_table(self):
        # This function creates database and employees table
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port=3307
            )

            cursor = conn.cursor()

            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS employeeedb")
            cursor.execute("USE employeeedb")

            # Create employees table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees(
                    emp_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    dob DATE NOT NULL,
                    doj DATE NOT NULL,
                    gender VARCHAR(40) NOT NULL,
                    mobile VARCHAR(15) NOT NULL,
                    designation VARCHAR(50) NOT NULL,
                    address TEXT NOT NULL
                )
            """)

            conn.commit()
            conn.close()

            print("Employee table ready")

        except Exception as err:
            print("ERROR:", err)
            messagebox.showerror("Database Error", str(err))

    def get_next_emp_id(self):
        # This function gets next auto-generated employee ID
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port=3307,
                database="employeeedb"
            )

            cursor = conn.cursor()

            # Get next AUTO_INCREMENT value
            cursor.execute("""
                SELECT AUTO_INCREMENT
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_SCHEMA = 'employeeedb'
                AND TABLE_NAME = 'employees'
            """)

            result = cursor.fetchone()
            conn.close()

            if result and result[0]:
                return result[0]
            else:
                return 1

        except Exception as e:
            print("Employee ID Error:", e)
            return ""

    def adding_new_emp(self, master):
        # Add employee form
        today = date.today()

        root2 = Toplevel(master)
        root2.geometry("500x630")
        root2.title("Adding New Employee")
        root2.resizable(False, False)
        root2.transient(master)
        root2.grab_set()
        root2.focus_force()

        # Heading
        Label(
            root2,
            text="Add New Employee",
            fg="white",
            bg="#0F172A",
            font=("Arial", 20, "bold"),
            pady=20
        ).place(x=0, y=0, relwidth=1)

        # Form frame
        f1 = Frame(
            root2,
            bg="white",
            bd=3,
            relief=GROOVE,
            width=480,
            height=480
        )
        f1.place(x=10, y=80)

        # =========================
        # Employee ID - Auto Generate
        # =========================
        Label(
            f1,
            text="Employee ID :",
            fg="#1E293B",
            bg="white",
            font=("Arial", 15, "bold")
        ).place(x=8, y=10)

        # Store auto-generated ID in StringVar
        self.emp_id_var = StringVar()

        # Set next employee ID
        self.emp_id_var.set(str(self.get_next_emp_id()))

        # Readonly field, user cannot edit Employee ID
        self.emp_id_entry = Entry(
            f1,
            font=("Arial", 12, "bold"),
            bg="#dfe7e8",
            bd=2,
            relief=SOLID,
            textvariable=self.emp_id_var,
            state="readonly"
        )
        self.emp_id_entry.place(x=170, y=10)

        # Name
        Label(
            f1,
            text="Name :",
            fg="#1E293B",
            bg="white",
            font=("Arial", 15, "bold")
        ).place(x=8, y=60)

        self.name_entry = Entry(
            f1,
            font=("Arial", 12, "bold"),
            bg="white",
            bd=2,
            relief=SOLID
        )
        self.name_entry.place(x=170, y=60)

        # Date of Birth
        Label(
            f1,
            text="D.O.B :",
            fg="#1E293B",
            bg="white",
            font=("Arial", 15, "bold")
        ).place(x=8, y=110)

        self.dob_entry = DateEntry(
            f1,
            font=("Arial", 12, "bold"),
            bg="white",
            bd=2,
            relief=SOLID,
            width=15,
            date_pattern="yyyy-mm-dd",
            mindate=date(today.year - 60, 1, 1),
            maxdate=date(today.year - 19, today.month, today.day)
        )
        self.dob_entry.place(x=170, y=110)

        # Date of Joining
        Label(
            f1,
            text="D.O.J :",
            fg="#1E293B",
            bg="white",
            font=("Arial", 15, "bold")
        ).place(x=8, y=160)

        self.doj_entry = DateEntry(
            f1,
            font=("Arial", 12, "bold"),
            bg="white",
            bd=2,
            relief=SOLID,
            width=15,
            date_pattern="yyyy-mm-dd"
        )
        self.doj_entry.place(x=170, y=160)

        # Gender
        Label(
            f1,
            text="Gender :",
            fg="#1E293B",
            bg="white",
            font=("Arial", 15, "bold")
        ).place(x=8, y=210)

        self.gender_entry = Entry(
            f1,
            font=("Arial", 12, "bold"),
            bg="white",
            bd=2,
            relief=SOLID
        )
        self.gender_entry.place(x=170, y=210)

        # Mobile Number
        Label(
            f1,
            text="Mobile No. :",
            fg="#1E293B",
            bg="white",
            font=("Arial", 15, "bold")
        ).place(x=8, y=260)

        self.mobile_entry = Entry(
            f1,
            font=("Arial", 12, "bold"),
            bg="white",
            bd=2,
            relief=SOLID
        )
        self.mobile_entry.place(x=170, y=260)

        # Designation
        Label(
            f1,
            text="Designation :",
            fg="#1E293B",
            bg="white",
            font=("Arial", 15, "bold")
        ).place(x=8, y=310)

        self.desig_entry = Entry(
            f1,
            font=("Arial", 12, "bold"),
            bg="white",
            bd=2,
            relief=SOLID
        )
        self.desig_entry.place(x=170, y=310)

        # Address
        Label(
            f1,
            text="Address :",
            fg="#1E293B",
            bg="white",
            font=("Arial", 15, "bold")
        ).place(x=8, y=360)

        self.address_entry = Text(
            f1,
            font=("Arial", 12, "bold"),
            bg="white",
            bd=2,
            relief=SOLID,
            width=30,
            height=4
        )
        self.address_entry.place(x=170, y=360)

        # Save Button
        Button(
            root2,
            text="Save Employee",
            font=("Arial", 15, "bold"),
            command=lambda: self.save_employee(root2),
            padx=20,
            bg="green",
            fg="white",
            bd=0,
            relief=FLAT
        ).place(x=40, y=570)

        # Cancel Button
        Button(
            root2,
            text="Cancel",
            font=("Arial", 15, "bold"),
            command=root2.destroy,
            padx=60,
            bg="red",
            fg="white",
            bd=0,
            relief=FLAT
        ).place(x=260, y=570)

    def save_employee(self, root2):
        # Get data from form fields
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        desig = self.desig_entry.get()
        address = self.address_entry.get("1.0", END).strip()
        mobile = self.mobile_entry.get()
        dob = self.dob_entry.get_date()
        doj = self.doj_entry.get_date()

        # Blank field validation
        if not name or not gender or not desig or not address or not mobile:
            messagebox.showerror("Invalid Input","All fields must be filled.",parent=root2)
            return

        # Mobile number validation
        if not mobile.isdigit():
            messagebox.showerror("Invalid Input","Mobile Number must contain only digits.",parent=root2)
            return

        if len(mobile) != 10:
            messagebox.showerror("Invalid Input","Mobile Number must be exactly 10 digits.",parent=root2
            )
            return

        if mobile[0] not in "6789":
            messagebox.showerror("Invalid Input","Mobile Number is not valid.",parent=root2
            )
            return

        # Date validation
        if dob >= doj:
            messagebox.showerror("Invalid Input","Date of birth cannot be greater than or equal to date of joining.", parent=root2)
            return

        # Insert employee data into database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port=3307,
                database="employeeedb"
            )

            cursor = conn.cursor()

            # Employee ID is not inserted because MySQL creates it automatically
            cursor.execute("""
                INSERT INTO employees
                (name,dob,doj, gender, mobile,designation,address)
                VALUES(%s, %s, %s, %s, %s, %s, %s)""", (name,dob,doj,gender,mobile,desig,address))

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Employee saved successfully.",
                parent=root2
            )

            # Clear form after saving
            self.name_entry.delete(0, END)
            self.gender_entry.delete(0, END)
            self.mobile_entry.delete(0, END)
            self.desig_entry.delete(0, END)
            self.address_entry.delete("1.0", END)

            # Reset joining date
            self.doj_entry.set_date(date.today())

            # Update employee ID for next record
            self.emp_id_var.set(str(self.get_next_emp_id()))

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e),
                parent=root2
            )


    def search_employee(self, master):
        root2 = Toplevel(master)
        root2.geometry("500x550")
        root2.title("Search Employee")
        root2.resizable(False, False)
        root2.transient(master)
        root2.grab_set()
        root2.focus_force()

        Label(root2, text="Search Employee by ID",
            fg="white", bg="#0F172A",
            font=("Arial", 20, "bold"),
            pady=20).place(x=0, y=0, relwidth=1)

        Label(root2, text="Employee ID:",
            fg="#1E293B",
            font=("Arial", 15, "bold")).place(x=50, y=85)

        emp_id_var = StringVar()

        Entry(root2,
            font=("Arial", 10, "bold"),
            bd=2,
            relief=SOLID,
            textvariable=emp_id_var).place(x=200, y=85, width=220)

        result_frame = Frame(root2, bg="white", bd=2, relief=SOLID)
        result_frame.place(x=50, y=145, width=400, height=330)

        def fetch_employee():
            emp_id = emp_id_var.get().strip()

            if not emp_id.isdigit():
                messagebox.showerror("Invalid Error",
                                    "Enter a valid Employee ID",
                                    parent=root2)
                return

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    port=3307,
                    database="employeeedb"
                )

                cursor = conn.cursor()
                cursor.execute("SELECT * FROM employees WHERE emp_id=%s", (emp_id,))
                row = cursor.fetchone()
                conn.close()

                for widget in result_frame.winfo_children():
                    widget.destroy()

                if row:
                    details = [
                        ("Employee ID", row[0]),
                        ("Name", row[1]),
                        ("D.O.B", row[2]),
                        ("D.O.J", row[3]),
                        ("Gender", row[4]),
                        ("Mobile", row[5]),
                        ("Designation", row[6]),
                        ("Address", row[7])
                    ]

                    for i, (field, value) in enumerate(details):
                        Label(result_frame,
                            text=f"{field}:",
                            font=("Arial", 10, "bold"),
                            bg="white",
                            fg="#0F172A",
                            anchor="w").grid(row=i, column=0, sticky="w", padx=10, pady=5)

                        Label(result_frame,
                            text=str(value),
                            font=("Arial", 10, "bold"),
                            bg="white",
                            fg="green",
                            anchor="w",
                            justify=LEFT,
                            wraplength=220).grid(row=i, column=1, sticky="w", padx=10, pady=5)
                else:
                    Label(result_frame,
                        text="❌ Employee Not Found",
                        font=("Arial", 10, "bold"),
                        bg="white",
                        fg="red").pack(pady=100)

            except Exception as e:
                messagebox.showerror("Database Error", str(e), parent=root2)

        Button(root2, text="Search",
            font=("Arial", 15, "bold"),
            command=fetch_employee,
            bg="green",
            fg="white",
            bd=0,
            relief=FLAT).place(x=50, y=490, width=180, height=45)

        Button(root2, text="Cancel",
            font=("Arial", 15, "bold"),
            command=root2.destroy,
            bg="red",
            fg="white",
            bd=0,
            relief=FLAT).place(x=270, y=490, width=180, height=45)
    
    def deleting_employee(self,master):
        root2 = Toplevel(master)
        root2.geometry("500x550")
        root2.title("Search Employee")
        root2.resizable(False, False)
        root2.transient(master)
        root2.grab_set()
        root2.focus_force()

        Label(root2, text="Search Employee by ID",
            fg="white", bg="#0F172A",
            font=("Arial", 20, "bold"),
            pady=20).place(x=0, y=0, relwidth=1)

        Label(root2, text="Employee ID:",
            fg="#1E293B",
            font=("Arial", 15, "bold")).place(x=50, y=85)

        emp_id_var = StringVar()

        Entry(root2,
            font=("Arial", 10, "bold"),
            bd=2,
            relief=SOLID,
            textvariable=emp_id_var).place(x=200, y=85, width=220)

        result_frame = Frame(root2, bg="white", bd=2, relief=SOLID)
        result_frame.place(x=50, y=145, width=400, height=330)

        def fetch_employee():
            emp_id = emp_id_var.get().strip()

            if not emp_id.isdigit():
                messagebox.showerror("Invalid Error",
                                    "Enter a valid Employee ID",
                                    parent=root2)
                return

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    port=3307,
                    database="employeeedb"
                )

                cursor = conn.cursor()
                cursor.execute("SELECT * FROM employees WHERE emp_id=%s", (emp_id,))
                row = cursor.fetchone()
                conn.close()

                for widget in result_frame.winfo_children():
                    widget.destroy()

                if row:
                    details = [
                        ("Employee ID", row[0]),
                        ("Name", row[1]),
                        ("D.O.B", row[2]),
                        ("D.O.J", row[3]),
                        ("Gender", row[4]),
                        ("Mobile", row[5]),
                        ("Designation", row[6]),
                        ("Address", row[7])
                    ]

                    for i, (field, value) in enumerate(details):
                        Label(result_frame,
                            text=f"{field}:",
                            font=("Arial", 10, "bold"),
                            bg="white",
                            fg="#0F172A",
                            anchor="w").grid(row=i, column=0, sticky="w", padx=10, pady=5)

                        Label(result_frame,
                            text=str(value),
                            font=("Arial", 10, "bold"),
                            bg="white",
                            fg="green",
                            anchor="w",
                            justify=LEFT,
                            wraplength=220).grid(row=i, column=1, sticky="w", padx=10, pady=5)
                else:
                    Label(result_frame,
                        text="❌ Employee Not Found",
                        font=("Arial", 10, "bold"),
                        bg="white",
                        fg="red").pack(pady=100)

            except Exception as e:
                messagebox.showerror("Database Error", str(e), parent=root2)

        def delete_record():
            emp_id = emp_id_var.get().strip()

            if not emp_id.isdigit():
                messagebox.showerror("Invalid Error","Enter a valid Employee ID",parent=root2)
                return

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    port=3307,
                    database="employeeedb"
                )

                cursor = conn.cursor()
                cursor.execute("SELECT * FROM employees WHERE emp_id=%s", (emp_id,))
                row = cursor.fetchone()

                if not row:
                    messagebox.showerror("Error","Employee ID not found",parent=root2)
                else:
                    confirm=messagebox.askyesno("Confirm Delete",f"Are you sure you want to permenently delete the Employee ID {emp_id}?",parent=root2)
                
                    if confirm:
                        cursor.execute("DELETE FROM salary WHERE emp_id=%s",(emp_id,))
                        cursor.execute("DELETE FROM employees WHERE emp_id=%s",(emp_id,))
                        conn.commit()
                        
                        messagebox.showinfo("Deleted",f"Employee ID {emp_id}Deleted Successfully!",parent=root2)
                        
                        emp_id_var.set("")
                        result_frame.delete("1.0",END)
                
                conn.close()
            
            except Exception as e:
                messagebox.showerror("Datebase Error",str(e),parent=root2)




        Button(root2, text="Show",font=("Arial", 12, "bold"),command=fetch_employee,bg="blue", fg="white", bd=0,relief=FLAT).place(x=70, y=490, width=100, height=45)
        Button(root2, text="Delete", font=("Arial", 12, "bold"),command=delete_record, bg="red", fg="white",bd=0,relief=FLAT).place(x=200, y=490, width=100, height=45)
        Button(root2, text="Close", font=("Arial", 12, "bold"), command=root2.destroy, bg="#F59E0B", fg="white",bd=0,relief=FLAT).place(x=330, y=490, width=100, height=45)