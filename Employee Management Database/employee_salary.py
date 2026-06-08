# ==========================================
# Employee Salary Management System
# Handles Salary Record Creation & Update
# ==========================================

from tkinter import *
from tkinter import messagebox
import mysql.connector


class EmployeeSalary:

    # ==========================================
    # Constructor
    # Creates salary table automatically
    # ==========================================
    def __init__(self):
        self.create_database_and_table()

    # ==========================================
    # Create Salary Table
    # ==========================================
    def create_database_and_table(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port=3307,
                database="employeeedb"
            )

            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS salary(
                    emp_id INT PRIMARY KEY,
                    basic FLOAT DEFAULT 0,
                    hra FLOAT DEFAULT 0,
                    allowances FLOAT DEFAULT 0,
                    overtime FLOAT DEFAULT 0,
                    pf FLOAT DEFAULT 0,
                    tax FLOAT DEFAULT 0,
                    deductions FLOAT DEFAULT 0,
                    gross FLOAT DEFAULT 0,
                    net FLOAT DEFAULT 0,

                    FOREIGN KEY(emp_id)
                    REFERENCES employees(emp_id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
                )
            """)

            conn.commit()
            conn.close()

            print("Salary table ready")

        except Exception as err:
            messagebox.showerror("Database Error", str(err))

    # ==========================================
    # Open Salary Update Window
    # ==========================================
    def update_salary_form(self, master):

        root2 = Toplevel(master)
        root2.geometry("935x600")
        root2.title("Update Salary Record")
        root2.resizable(False, False)
        root2.transient(master)
        root2.grab_set()
        root2.focus_force()

        # ==========================================
        # Header Section
        # ==========================================
        Label(
            root2,
            text="Update Salary Record",
            fg="white",
            bg="#0F172A",
            font=("Arial", 20, "bold"),
            pady=20
        ).place(x=0, y=0, relwidth=1)

        # ==========================================
        # Employee Details Frame
        # ==========================================
        frame_left = Frame(
            root2,
            bg="white",
            bd=3,
            relief=GROOVE,
            width=420,
            height=500
        )
        frame_left.place(x=35, y=85)

        # ==========================================
        # Salary Details Frame
        # ==========================================
        frame_right = Frame(
            root2,
            bg="white",
            bd=3,
            relief=GROOVE,
            width=420,
            height=500
        )
        frame_right.place(x=475, y=85)

        Label(
            frame_left,
            text="Employee Details",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#0F172A"
        ).place(x=5, y=5)

        # Employee ID Variable
        emp_id_var = StringVar()

        Label(
            frame_left,
            text="Enter Employee ID:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#0F172A"
        ).place(x=5, y=40)

        # Employee ID Entry
        emp_id_entry = Entry(
            frame_left,
            font=("Arial", 12),
            textvariable=emp_id_var
        )
        emp_id_entry.place(x=180, y=40)

        # Employee Information Display Box
        emp_info = Text(
            frame_left,
            font=("Arial", 12),
            width=43,
            height=23,
            bg="white"
        )
        emp_info.place(x=5, y=70)

        Label(
            frame_right,
            text="Salary Details",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#0F172A"
        ).place(x=5, y=5)

        # ==========================================
        # Salary Variables
        # ==========================================
        salary_var = {
            "Basic": StringVar(),
            "HRA": StringVar(),
            "Allowances": StringVar(),
            "Overtime": StringVar(),
            "PF": StringVar(),
            "Tax": StringVar(),
            "Deductions": StringVar(),
            "Gross": StringVar(),
            "Net": StringVar()
        }

        # ==========================================
        # Create Salary Entry Fields
        # ==========================================
        def create_field(label, var, y, readonly=False):

            Label(
                frame_right,
                text=label,
                font=("Arial", 12, "bold"),
                bg="white"
            ).place(x=10, y=y)

            entry = Entry(
                frame_right,
                textvariable=var,
                font=("Arial", 10),
                width=20,
                state="readonly" if readonly else "normal"
            )

            entry.place(x=150, y=y)

            return entry

        e1 = create_field("Basic:", salary_var["Basic"], 40)
        e2 = create_field("HRA:", salary_var["HRA"], 75)
        e3 = create_field("Allowances:", salary_var["Allowances"], 110)
        e4 = create_field("Overtime:", salary_var["Overtime"], 145)
        e5 = create_field("PF:", salary_var["PF"], 180)
        e6 = create_field("Tax:", salary_var["Tax"], 215)
        e7 = create_field("Deductions:", salary_var["Deductions"], 250)
        e8 = create_field("Gross:", salary_var["Gross"], 285, True)
        e9 = create_field("Net:", salary_var["Net"], 320, True)

        # ==========================================
        # Auto Calculate Salary
        #
        # Gross = Basic + HRA + Allowances + Overtime
        # Net = Gross - (PF + Tax + Deductions)
        # ==========================================
        def auto_calculate(event=None):

            try:
                basic = float(salary_var["Basic"].get() or 0)
                hra = float(salary_var["HRA"].get() or 0)
                allowances = float(salary_var["Allowances"].get() or 0)
                overtime = float(salary_var["Overtime"].get() or 0)
                pf = float(salary_var["PF"].get() or 0)
                tax = float(salary_var["Tax"].get() or 0)
                deductions = float(salary_var["Deductions"].get() or 0)

                gross = basic + hra + allowances + overtime
                net = gross - (pf + tax + deductions)

                salary_var["Gross"].set(f"{gross:.2f}")
                salary_var["Net"].set(f"{net:.2f}")

            except:
                pass

        # Bind Auto Calculation
        for entry in (e1, e2, e3, e4, e5, e6, e7):
            entry.bind("<KeyRelease>", auto_calculate)

        # ==========================================
        # Fetch Employee & Salary Details
        # ==========================================
        def fetch_data(event=None):

            emp_id = emp_id_var.get().strip()

            # Validate Employee ID
            if not emp_id.isdigit():
                emp_info.delete("1.0", END)
                emp_info.insert(END, "Please enter a valid Employee ID.")
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

                # Fetch Employee Record
                cursor.execute(
                    "SELECT * FROM employees WHERE emp_id=%s",
                    (emp_id,)
                )

                emp = cursor.fetchone()

                emp_info.delete("1.0", END)

                # Clear Salary Fields
                for field in salary_var:
                    salary_var[field].set("")

                if emp:

                    emp_info.insert(
                        END,
                        f"ID: {emp[0]}\n"
                        f"Name: {emp[1]}\n"
                        f"D.O.B: {emp[2]}\n"
                        f"D.O.J: {emp[3]}\n"
                        f"Gender: {emp[4]}\n"
                        f"Mobile: {emp[5]}\n"
                        f"Designation: {emp[6]}\n"
                        f"Address: {emp[7]}"
                    )

                else:
                    emp_info.insert(END, "❌ Employee Not Found")
                    conn.close()
                    return

                # Fetch Existing Salary Record
                cursor.execute(
                    "SELECT * FROM salary WHERE emp_id=%s",
                    (emp_id,)
                )

                sal = cursor.fetchone()

                if sal:
                    salary_var["Basic"].set(sal[1])
                    salary_var["HRA"].set(sal[2])
                    salary_var["Allowances"].set(sal[3])
                    salary_var["Overtime"].set(sal[4])
                    salary_var["PF"].set(sal[5])
                    salary_var["Tax"].set(sal[6])
                    salary_var["Deductions"].set(sal[7])
                    salary_var["Gross"].set(sal[8])
                    salary_var["Net"].set(sal[9])

                conn.close()

            except Exception as e:
                messagebox.showerror("Error", str(e), parent=root2)

        # ==========================================
        # Insert / Update Salary Record
        # ==========================================
        def update_salary():

            emp_id = emp_id_var.get().strip()

            if not emp_id.isdigit():
                messagebox.showerror(
                    "Invalid Error",
                    "Enter a valid Employee ID",
                    parent=root2
                )
                return

            auto_calculate()

            # Collect Salary Data
            data = (
                float(salary_var["Basic"].get() or 0),
                float(salary_var["HRA"].get() or 0),
                float(salary_var["Allowances"].get() or 0),
                float(salary_var["Overtime"].get() or 0),
                float(salary_var["PF"].get() or 0),
                float(salary_var["Tax"].get() or 0),
                float(salary_var["Deductions"].get() or 0),
                float(salary_var["Gross"].get() or 0),
                float(salary_var["Net"].get() or 0)
            )

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    port=3307,
                    database="employeeedb"
                )

                cursor = conn.cursor()

                # Check Employee Exists
                cursor.execute(
                    "SELECT emp_id FROM employees WHERE emp_id=%s",
                    (emp_id,)
                )

                employee_exists = cursor.fetchone()

                if not employee_exists:
                    messagebox.showerror(
                        "Error",
                        "Employee ID does not exist.",
                        parent=root2
                    )
                    conn.close()
                    return

                # Check Salary Record Exists
                cursor.execute(
                    "SELECT emp_id FROM salary WHERE emp_id=%s",
                    (emp_id,)
                )

                salary_exists = cursor.fetchone()

                if salary_exists:

                    # Update Existing Salary Record
                    cursor.execute("""
                        UPDATE salary
                        SET basic=%s,
                            hra=%s,
                            allowances=%s,
                            overtime=%s,
                            pf=%s,
                            tax=%s,
                            deductions=%s,
                            gross=%s,
                            net=%s
                        WHERE emp_id=%s
                    """, (*data, emp_id))

                else:

                    # Insert New Salary Record
                    cursor.execute("""
                        INSERT INTO salary
                        (emp_id,basic,hra,allowances,overtime,pf,tax,deductions,gross,net)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (emp_id, *data))

                conn.commit()
                conn.close()

                messagebox.showinfo(
                    "Success",
                    "Salary record updated successfully!",
                    parent=root2
                )

                # Clear Form
                for field in salary_var:
                    salary_var[field].set("")

                emp_id_var.set("")
                emp_info.delete("1.0", END)
                emp_id_entry.focus_set()

            except Exception as e:
                messagebox.showerror("Error", str(e), parent=root2)

        # ==========================================
        # Event Bindings
        # ==========================================
        emp_id_entry.bind("<Return>", fetch_data)

        # Fetch Button
        Button(
            frame_left,
            text="Fetch",
            bg="#2563EB",
            fg="white",
            font=("Arial", 11, "bold"),
            command=fetch_data
        ).place(x=320, y=38, width=80, height=28)

        # Update Salary Button
        Button(
            frame_right,
            text="Update Salary",
            bg="green",
            fg="white",
            font=("Arial", 12, "bold"),
            command=update_salary
        ).place(x=150, y=370, width=150, height=35)