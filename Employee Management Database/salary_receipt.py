from tkinter import *
from tkinter import messagebox
import mysql.connector


class SalaryReceipt:

    # --------------------------------------------------
    # Open Salary Receipt Window
    # --------------------------------------------------
    def generate_receipt(self, master):

        # Create child window
        root2 = Toplevel(master)
        root2.geometry("520x600")
        root2.title("Generate Salary Receipt")
        root2.resizable(False, False)

        # ================= Header =================
        Label(
            root2,text="Generate Salary Receipt",fg="white",bg="#0F172A",font=("Arial", 20, "bold"),pady=20).place(x=0, y=0, relwidth=1)

        # Employee ID Label
        Label(root2,text="Employee ID:",font=("Arial", 14, "bold")).place(x=40, y=90)

        # Variable to store Employee ID
        emp_id_var = StringVar()

        # Employee ID Input Field
        Entry(
            root2,textvariable=emp_id_var,font=("Arial", 13),bd=2,relief=SOLID).place(x=180, y=90, width=180)

        # Text Area for Receipt Display
        receipt_text = Text(root2,font=("Consolas", 11),bd=2,relief=SOLID)
        receipt_text.place(x=40, y=150, width=440, height=350)

        # --------------------------------------------------
        # Fetch Employee Salary Details from Database
        # --------------------------------------------------
        def fetch_receipt():

            # Get Employee ID entered by user
            emp_id = emp_id_var.get().strip()

            # Validate Employee ID
            if not emp_id.isdigit():
                messagebox.showerror("Error","Enter valid Employee ID",parent=root2)
                return

            try:
                # Database Connection
                conn = mysql.connector.connect(host="localhost",user="root",password="",port=3307,database="employeeedb")

                cursor = conn.cursor()

                # Fetch Employee + Salary Data
                cursor.execute("""
                    SELECT e.emp_id,e.name,e.designation,e.mobile,s.basic,s.hra,s.allowances,s.overtime,s.pf,s.tax,s.deductions,s.gross,s.net
                    FROM employees e JOIN salary s ON e.emp_id = s.emp_id WHERE e.emp_id = %s""", (emp_id,))

                row = cursor.fetchone()

                conn.close()

                # Clear Previous Receipt
                receipt_text.delete("1.0", END)

                # If Record Exists
                if row:

                    receipt = f"""
========================================
            SALARY RECEIPT
========================================

Employee ID   : {row[0]}
Name          : {row[1]}
Designation   : {row[2]}
Mobile        : {row[3]}

----------------------------------------
Salary Details
----------------------------------------

Basic Salary  : Rs. {row[4]}
HRA           : Rs. {row[5]}
Allowances    : Rs. {row[6]}
Overtime      : Rs. {row[7]}

Gross Salary  : Rs. {row[11]}

----------------------------------------
Deductions
----------------------------------------

PF            : Rs. {row[8]}
Tax           : Rs. {row[9]}
Other Deduct. : Rs. {row[10]}

----------------------------------------
Net Salary    : Rs. {row[12]}
========================================
"""

                    # Display Receipt
                    receipt_text.insert(END, receipt)

                else:
                    receipt_text.insert(
                        END,
                        "Salary record not found for this Employee ID."
                    )

            except Exception as e:
                messagebox.showerror("Database Error",str(e),parent=root2)

        # ================= Buttons =================

        # Generate Receipt Button
        Button(root2,text="Generate",command=fetch_receipt,bg="green",fg="white",font=("Arial", 14, "bold")).place(x=80, y=525, width=160, height=40)

        # Close Window Button
        Button(root2,text="Cancel",command=root2.destroy, bg="red", fg="white",font=("Arial", 14, "bold")).place(x=280, y=525, width=160, height=40)