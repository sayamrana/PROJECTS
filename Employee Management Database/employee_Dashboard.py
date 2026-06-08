from tkinter import *
from tkinter import messagebox
from datetime import datetime
from employee_details import EmployeeDetails
from employee_salary import EmployeeSalary
from salary_receipt import SalaryReceipt
from update_employees import EmployeeUpdate
from view_employees import ViewEmployees
import mysql.connector

NAVBAR = "#0F172A"
SIDEBAR = "#1E293B"
BLUE = "#2563EB"
GREEN = "#22C55E"
ORANGE = "#F59E0B"
RED = "#EF4444"
BG = "#F8FAFC"
WHITE = "#FFFFFF"
TEXT = "#0F172A"


def EmployeeDashboard(master):
    root1 = Toplevel(master)
    root1.title("Employee Management System")
    root1.state("zoomed")
    root1.config(bg=BG)

    emp_manager = EmployeeDetails()
    emp_salary = EmployeeSalary()
    emp_update = EmployeeUpdate()
    emp_salary_receipt = SalaryReceipt()
    view_emp = ViewEmployees()
    
    def logout():
        root1.destroy()
        master.deiconify()

    def add_employee():
        emp_manager.adding_new_emp(root1)

    def update_employee():
        emp_update.update_employee(root1)

    def search_employee():
        emp_manager.search_employee(root1)

    def delete_record():
        emp_manager.deleting_employee(root1)

    def generate_receipt():
        emp_salary_receipt.generate_receipt(root1)

    def calculate_salary():
        emp_salary.update_salary_form(root1)

    def view_all_employees():
        view_emp.view_all_employees(root1)

    header = Frame(root1, bg=NAVBAR, height=70)
    header.pack(fill=X)
    header.pack_propagate(False)

    Label(header, text="Employee Management System",
          font=("Arial", 24, "bold"),
          bg=NAVBAR, fg=WHITE).pack(side=LEFT, padx=30)

    Label(header, text="Welcome, Admin ▼",
          font=("Arial", 14, "bold"),
          bg=NAVBAR, fg=WHITE).pack(side=RIGHT, padx=30)

    main = Frame(root1, bg=BG)
    main.pack(fill=BOTH, expand=True)

    sidebar = Frame(main, bg=SIDEBAR, width=220)
    sidebar.pack(side=LEFT, fill=Y)
    sidebar.pack_propagate(False)

    def sidebar_btn(icon, text, command=None, active=False):
        btn = Button(sidebar,
                     text=f"{icon}  {text}",
                     command=command,
                     font=("Arial", 13, "bold"),
                     bg=BLUE if active else SIDEBAR,
                     fg=WHITE,
                     bd=0,
                     anchor="w",
                     padx=25,
                     pady=15,
                     cursor="hand2",
                     activebackground=BLUE,
                     activeforeground=WHITE)
        btn.pack(fill=X, pady=2)

        def enter(e):
            if not active:
                btn.config(bg="#334155")

        def leave(e):
            if not active:
                btn.config(bg=SIDEBAR)

        btn.bind("<Enter>", enter)
        btn.bind("<Leave>", leave)

    sidebar_btn("⌂", "Dashboard", active=True)
    sidebar_btn("●", "Add Employee", add_employee)
    sidebar_btn("✎", "Update Employee", update_employee)
    sidebar_btn("⌕", "Search Employee", search_employee)
    sidebar_btn("✖", "Delete Record", delete_record)
    sidebar_btn("▣", "Generate Receipt", generate_receipt)
    sidebar_btn("$", "Calculate Salary", calculate_salary)
    sidebar_btn("☷", "View All Employees", view_all_employees)

    Label(sidebar, bg=SIDEBAR).pack(expand=True)
    sidebar_btn("↪", "Logout", logout)

    content = Frame(main, bg=BG)
    content.pack(side=LEFT, fill=BOTH, expand=True, padx=30, pady=30)

    Label(content, text="Welcome to Employee Dashboard",
          font=("Arial", 28, "bold"),
          bg=BG, fg=TEXT).pack(anchor="w")

    Label(content,
          text="Manage employee records, salary, receipt and reports from one place.",
          font=("Arial", 14),
          bg=BG, fg="#64748B").pack(anchor="w", pady=8)

    date_text = datetime.now().strftime("%d %B %Y | %A")

    Label(content, text="📅 " + date_text,
          font=("Arial", 12, "bold"),
          bg=WHITE, fg=TEXT,
          padx=15, pady=8,
          relief=SOLID, bd=1).pack(anchor="e")

    cards = Frame(content, bg=BG)
    cards.pack(fill=X, pady=30)

    def kpi_card(title, value, color, icon):
        box = Frame(cards, bg=color, height=130)
        box.pack(side=LEFT, fill=X, expand=True, padx=10)
        box.pack_propagate(False)

        Label(box, text=icon,
              font=("Arial", 32),
              bg=color, fg=WHITE).pack(side=LEFT, padx=25)

        info = Frame(box, bg=color)
        info.pack(side=LEFT, pady=30)

        Label(info, text=title,
              font=("Arial", 14, "bold"),
              bg=color, fg=WHITE).pack(anchor="w")

        Label(info, text=value,
              font=("Arial", 30, "bold"),
              bg=color, fg=WHITE).pack(anchor="w")

    kpi_card("Total Employees", str(get_total_employees()), BLUE, "☷")
    # kpi_card("Departments", "0", GREEN, "▦")
    kpi_card("Salary Records", str(get_salary_records()), ORANGE, "$")

    Label(content, text="Quick Actions",
          font=("Arial", 22, "bold"),
          bg=BG, fg=TEXT).pack(anchor="w", pady=10)

    action_frame = Frame(content, bg=BG)
    action_frame.pack(fill=X)

    def action_btn(text, color, command, row, col):
        btn = Button(action_frame,
                     text=text,
                     command=command,
                     font=("Arial", 15, "bold"),
                     bg=WHITE,
                     fg=color,
                     activebackground=color,
                     activeforeground=WHITE,
                     bd=1,
                     relief=SOLID,
                     cursor="hand2",
                     height=3)
        btn.grid(row=row, column=col, padx=12, pady=12, sticky="nsew")
        action_frame.grid_columnconfigure(col, weight=1)

    action_btn("● Add New Employee", RED, add_employee, 0, 0)
    action_btn("⌕ Search Employee", BLUE, search_employee, 0, 1)
    action_btn("✎ Update Employee", ORANGE, update_employee, 0, 2)
    action_btn("✖ Delete Record", "#7C3AED", delete_record, 1, 0)
    action_btn("▣ Generate Receipt", GREEN, generate_receipt, 1, 1)
    action_btn("$ Calculate Salary", BLUE, calculate_salary, 1, 2)

    Button(content,
           text="☷ View All Employees",
           command=view_all_employees,
           font=("Arial", 16, "bold"),
           bg="#DCFCE7",
           fg="#15803D",
           activebackground=GREEN,
           activeforeground=WHITE,
           height=2,
           bd=1,
           relief=SOLID,
           cursor="hand2").pack(fill=X, pady=25)

    Label(content,
          text="© 2026 Employee Management System",
          font=("Arial", 10),
          bg=BG, fg="#64748B").pack(side=BOTTOM, pady=10)
    
    
def get_total_employees():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port=3307,
            database="employeeedb"
        )

        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM employees")

        total = cursor.fetchone()[0]

        conn.close()

        return total

    except Exception as e:
        print("Error:", e)
        return 0
    
def get_salary_records():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port=3307,
            database="employeeedb"
        )

        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM salary")

        total = cursor.fetchone()[0]

        conn.close()

        return total

    except Exception as e:
        print("Error:", e)
        return 0
    
