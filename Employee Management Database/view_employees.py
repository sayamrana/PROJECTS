from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class ViewEmployees:

    def view_all_employees(self, master):
        root2 = Toplevel(master)
        root2.geometry("1000x550")
        root2.title("View All Employees")
        root2.resizable(False, False)
        root2.transient(master)
        root2.grab_set()
        root2.focus_force()

        Label(root2, text="View All Employees",
              fg="white", bg="#0F172A",
              font=("Arial", 20, "bold"),
              pady=20).place(x=0, y=0, relwidth=1)

        columns = (
            "emp_id", "name", "dob", "doj",
            "gender", "mobile", "designation", "address"
        )

        table = ttk.Treeview(root2, columns=columns, show="headings")

        table.heading("emp_id", text="ID")
        table.heading("name", text="Name")
        table.heading("dob", text="D.O.B")
        table.heading("doj", text="D.O.J")
        table.heading("gender", text="Gender")
        table.heading("mobile", text="Mobile")
        table.heading("designation", text="Designation")
        table.heading("address", text="Address")

        table.column("emp_id", width=50)
        table.column("name", width=120)
        table.column("dob", width=100)
        table.column("doj", width=100)
        table.column("gender", width=80)
        table.column("mobile", width=120)
        table.column("designation", width=140)
        table.column("address", width=250)

        table.place(x=20, y=90, width=940, height=370)

        scrollbar_y = Scrollbar(root2, orient=VERTICAL, command=table.yview)
        scrollbar_y.place(x=960, y=90, height=370)

        scrollbar_x = Scrollbar(root2, orient=HORIZONTAL, command=table.xview)
        scrollbar_x.place(x=20, y=460, width=940)

        table.configure(yscrollcommand=scrollbar_y.set,
                        xscrollcommand=scrollbar_x.set)

        def load_data():
            for row in table.get_children():
                table.delete(row)

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    port=3307,
                    database="employeeedb"
                )

                cursor = conn.cursor()
                cursor.execute("SELECT * FROM employees")
                rows = cursor.fetchall()
                conn.close()

                for row in rows:
                    table.insert("", END, values=row)

            except Exception as e:
                messagebox.showerror("Database Error", str(e), parent=root2)

        Button(root2, text="Refresh",
               command=load_data,
               bg="#2563EB", fg="white",
               font=("Arial", 13, "bold")).place(x=320, y=495, width=150, height=40)

        Button(root2, text="Close",
               command=root2.destroy,
               bg="red", fg="white",
               font=("Arial", 13, "bold")).place(x=520, y=495, width=150, height=40)

        load_data()