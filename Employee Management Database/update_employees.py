from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector


class EmployeeUpdate:

    # ==========================================
    # Open Update Employee Window
    # ==========================================
    def update_employee(self, master):

        # Create child window
        root2 = Toplevel(master)
        root2.geometry("520x650")
        root2.title("Update Employee")
        root2.resizable(False, False)

        # ================= Header =================
        Label( root2, text="Update Employee",fg="white",bg="#0F172A", font=("Arial", 20, "bold"), pady=20).place(x=0, y=0, relwidth=1)

        # Employee ID Search Section
        Label(root2,text="Employee ID:",font=("Arial", 14, "bold")).place(x=40, y=90)

        # Variable for Employee ID
        emp_id_var = StringVar()

        # Employee ID Entry Box
        Entry(root2,textvariable=emp_id_var,font=("Arial", 13),bd=2,relief=SOLID).place(x=180, y=90, width=180)

        # ================= Form Frame =================
        f1 = Frame(root2,bg="white",bd=2,relief=GROOVE)
        f1.place(x=30, y=140, width=460, height=430)

        # Employee Information Fields
        name_entry = Entry(f1, font=("Arial", 12))
        dob_entry = DateEntry(f1, font=("Arial", 12), date_pattern="yyyy-mm-dd")
        doj_entry = DateEntry(f1, font=("Arial", 12), date_pattern="yyyy-mm-dd")
        gender_entry = Entry(f1, font=("Arial", 12))
        mobile_entry = Entry(f1, font=("Arial", 12))
        desig_entry = Entry(f1, font=("Arial", 12))
        address_entry = Text(f1, font=("Arial", 12), width=25, height=3)

        # Labels and Corresponding Widgets
        labels = [ "Name:","D.O.B:","D.O.J:", "Gender:", "Mobile:", "Designation:","Address:"]

        widgets = [name_entry,dob_entry, doj_entry, gender_entry,mobile_entry,desig_entry,address_entry]

        # Place Labels and Fields
        y = 20
        for label, widget in zip(labels, widgets):
            Label(f1,text=label,bg="white",font=("Arial", 13, "bold")).place(x=20, y=y)

            widget.place(x=180, y=y, width=230)
            y += 50

        # ==========================================
        # Fetch Employee Data from Database
        # ==========================================
        def fetch_employee():

            emp_id = emp_id_var.get().strip()

            # Validate Employee ID
            if not emp_id.isdigit():
                messagebox.showerror( "Error", "Enter valid Employee ID", parent=root2)
                return

            try:
                # Database Connection
                conn = mysql.connector.connect(host="localhost", user="root", password="",port=3307,database="employeeedb")

                cursor = conn.cursor()

                # Fetch Employee Record
                cursor.execute(  "SELECT * FROM employees WHERE emp_id=%s",(emp_id,))

                row = cursor.fetchone()

                conn.close()

                # If Record Found
                if row:

                    # Clear Existing Values
                    name_entry.delete(0, END)
                    gender_entry.delete(0, END)
                    mobile_entry.delete(0, END)
                    desig_entry.delete(0, END)
                    address_entry.delete("1.0", END)

                    # Fill Form with Employee Data
                    name_entry.insert(0, row[1])
                    dob_entry.set_date(row[2])
                    doj_entry.set_date(row[3])
                    gender_entry.insert(0, row[4])
                    mobile_entry.insert(0, row[5])
                    desig_entry.insert(0, row[6])
                    address_entry.insert("1.0", row[7])

                else:
                    messagebox.showerror("Error","Employee not found",parent=root2)

            except Exception as e:
                messagebox.showerror( "Database Error",str(e), parent=root2)

        # ==========================================
        # Update Employee Record
        # ==========================================
        def update_data():

            emp_id = emp_id_var.get().strip()

            # Get Updated Values
            name = name_entry.get()
            dob = dob_entry.get_date()
            doj = doj_entry.get_date()
            gender = gender_entry.get()
            mobile = mobile_entry.get()
            desig = desig_entry.get()
            address = address_entry.get("1.0", END).strip()

            # Check Empty Fields
            if not name or not gender or not mobile or not desig or not address:
                messagebox.showerror("Error","All fields are required",parent=root2)
                return

            try:
                # Database Connection
                conn = mysql.connector.connect( host="localhost",user="root",password="",port=3307, database="employeeedb")

                cursor = conn.cursor()

                # Update Employee Record
                cursor.execute("""
                    UPDATE employees
                    SET name=%s, dob=%s, doj=%s, gender=%s,  mobile=%s, designation=%s, address=%s WHERE emp_id=%s
                """, (name,dob,doj,gender,mobile,desig,address, emp_id))

                conn.commit()
                conn.close()

                messagebox.showinfo("Success","Employee updated successfully", parent=root2 )

                root2.destroy()

            except Exception as e:
                messagebox.showerror("Database Error",str(e),parent=root2 )

        # ================= Buttons =================

        # Fetch Button
        Button( root2, text="Fetch",command=fetch_employee,bg="#2563EB",fg="white",font=("Arial", 11, "bold")).place(x=380, y=88, width=80)

        # Update Button
        Button(root2,text="Update",command=update_data,bg="green",fg="white",font=("Arial", 14, "bold")).place(x=80, y=590, width=160, height=40)

        # Cancel Button
        Button(root2,text="Cancel",command=root2.destroy,bg="red",fg="white",font=("Arial", 14, "bold")).place(x=280, y=590, width=160, height=40)