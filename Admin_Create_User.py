import tkinter as tk
from datetime import date, datetime
from tkinter.constants import END, LEFT
from PIL import Image, ImageTk
from tkinter import messagebox

app_font = "Arial"

class Admin_Create_User(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.adminname = ""  

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "CREATE USER", font = ("Arial", 20, "bold"), fg = "burlywood4")
        self.label_welcome.pack(pady = 20)

        self.label_accountnumber_title = tk.Label(self, text = "Account number:", font = (app_font, 12))
        self.label_accountnumber_title.place(x = 70, y = 70)

        self.text_account_number = "070088142266"
        self.label_account_number = tk.Label(self, text = self.text_account_number, font = (app_font, 15, "bold"), fg = "green")
        self.label_account_number.place(x = 195, y = 67)

        self.label_fullname = tk.Label(self, text = "Full name: ", font = (app_font, 12))
        self.label_fullname.place(x = 15, y = 110)

        self.entry_fullname = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5)
        self.entry_fullname.place(x = 102, y = 108)

        self.label_id = tk.Label(self, text = "ID/Passport:", font = (app_font, 12))
        self.label_id.place(x = 15, y = 150)

        self.entry_id = tk.Entry(self, font = (app_font, 12, "bold"), width = 29, bd = 5)
        self.entry_id.place(x = 111, y = 148)

        self.label_sex = tk.Label(self, text = "Sex:", font = (app_font, 12))
        self.label_sex.place(x = 15, y = 190)

        self.lst_sex = ["Male", "Female", "Other"]
        self.sex_type = tk.IntVar()
        self.sex_type.set(-1)

        self.radio_sex = tk.Radiobutton(self, text = "Male", font = (app_font, 12), value = 1, variable = self.sex_type)
        self.radio_sex.place(x = 100, y = 190)

        self.radio_sex = tk.Radiobutton(self, text = "Female", font = (app_font, 12), value = 2, variable = self.sex_type)
        self.radio_sex.place(x = 200, y = 190)

        self.radio_sex = tk.Radiobutton(self, text = "Other", font = (app_font, 12), value = 3, variable = self.sex_type)
        self.radio_sex.place(x = 315, y = 190)

        self.label_dob = tk.Label(self, text = "Date of birth:", font = (app_font, 12))
        self.label_dob.place(x = 15, y = 230)

        self.lst_year = range(1920, 2022)
        self.clicked_year = tk.StringVar()
        self.clicked_year.set("Year")
        self.option_year = tk.OptionMenu(self, self.clicked_year, *self.lst_year)
        self.option_year.place(x = 130, y = 225)

        self.lst_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", 
                    "October", "November", "December"]
        self.clicked_month = tk.StringVar()
        self.clicked_month.set("Month")
        self.option_month = tk.OptionMenu(self, self.clicked_month, *self.lst_month)
        self.option_month.place(x = 218, y = 225)


        self.lst_day = ["Day"]
        self.clicked_day = tk.StringVar()
        self.clicked_day.set("Day")
        self.option_day = tk.OptionMenu(self, self.clicked_day, *self.lst_day)
        self.option_day.place(x = 320, y = 225)
        self.temp_year = "year"
        self.temp_month = "month"
        self.dob = False

        self.label_phone = tk.Label(self, text = "Phone number:", font = (app_font, 12))
        self.label_phone.place(x = 15, y = 270)

        self.entry_phone = tk.Entry(self, font = (app_font, 12, "bold"), width = 27, bd = 5)
        self.entry_phone.place(x = 130, y = 268)

        self.label_email = tk.Label(self, text = "Email:", font = (app_font, 12))
        self.label_email.place(x = 15, y = 310)

        self.entry_email = tk.Entry(self, font = (app_font, 12, "bold"), width = 34, bd = 5)
        self.entry_email.place(x = 68, y = 308)

        self.label_address = tk.Label(self, text = "Address:", font = (app_font, 12))
        self.label_address.place(x = 15, y = 350)

        self.textbox_address = tk.Text(self, font = (app_font, 12, "bold"), bd = 5, width = 32, height = 3)
        self.textbox_address.place(x = 87, y = 350)

        self.label_balance = tk.Label(self, text = "Balance:", font = (app_font, 12))
        self.label_balance.place(x = 15, y = 430)

        self.entry_balance = tk.Entry(self, font = (app_font, 12, "bold"), width = 27, bd = 5)
        self.entry_balance.place(x = 86, y = 428)

        self.label_usd = tk.Label(self, text = "USD", font = (app_font, 12))
        self.label_usd.place(x = 347, y = 430)

        self.label_question = tk.Label(self, text = "QUESTION SPECIAL\nWHAT IS YOUR INTEGER FAVORITE?", font = (app_font, 12), fg = "red")
        self.label_question.place(x = 61, y = 465)

        self.label_answer = tk.Label(self, text = "Your answer:", font = (app_font, 12))
        self.label_answer.place(x = 15, y = 510)

        self.entry_answer = tk.Entry(self, font = (app_font, 12, "bold"), width = 29, bd = 5)
        self.entry_answer.place(x = 115, y = 508)

        self.button_continue = tk.Button(self, text = "Continue", fg = "blue", border = "0", font = (app_font, 12, "bold"), command = self.confirm)
        self.button_continue.place(x = 161, y = 548)

        self.update_dob()
    
    def confirm(self):
        arg = []
        fullname = self.entry_fullname.get()
        id = self.entry_id.get()
        sex = self.sex_type.get()
        year = self.clicked_year.get()
        month = self.clicked_month.get()
        day = self.clicked_day.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.textbox_address.get("1.0", "end-1c")
        balance = self.entry_balance.get()
        answer = self.entry_answer.get()
        have_error = False
        
        if fullname and id and sex and year != "Year" and month != "Month" and day != "Day" and phone and email and address and balance and answer:
            if fullname.replace(" ", "").isalpha():
                fullname = fullname.upper()
                arg.append(fullname)
            elif not have_error:
                messagebox.showerror(title = "Create User", message = "Full name is invalid!")
                have_error = True

            if id.isalnum() and len(id) <= 12:
                id = id.upper()
                arg.append(id)
            elif not have_error:
                messagebox.showerror(title = "Create User", message = "ID/Passport is invalid!")
                have_error = True

            if sex == 1:
                sex = "Male"
            elif sex == 2:
                sex = "Female"
            else:
                sex = "Other"
            arg.append(sex)

            dob = month.upper()[0:3] + "-" + day + "-" + year
            arg.append(dob)

            if phone.isnumeric() and len(phone) <= 11:
                arg.append(phone)
            elif not have_error:
                messagebox.showerror(title = "Create User", message = "Phone number is invalid!")
                have_error = True
            
            if "@" in email and " " not in email:
                arg.append(email)
            elif not have_error:
                messagebox.showerror(title = "Create User", message = "Email is invalid!")
                have_error = True

            address = address.upper()
            arg.append(address)

            try:
                balance = int(balance)
                arg.append(balance)
                if balance <= 0 and not have_error:
                    messagebox.showerror(title = "Create User", message = "Balance is invalid!")
                    have_error = True
            except:
                if not have_error:
                    messagebox.showerror(title = "Create User", message = "Balance is invalid!")
                    have_error = True
            
            try:
                answer = int(answer)
                arg.append(answer)
            except:
                if not have_error:
                    messagebox.showerror(title = "Create User", message = "Answer is invalid!")
                    have_error = True
            
        else:
            messagebox.showerror(title = "Create User", message = "You must input all information!")
            have_error = True
    
        if not have_error:
            self.create_user(arg)
    
    def create_user(self, arg):
        password = self.controller.rand(6)
        code = """SELECT * FROM USER
                WHERE U_ID = '%s'"""%(arg[1])
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        if data:
            time = date.today().strftime("%b-%d-%Y") + " " + datetime.now().strftime("%H:%M:%S")
            code = "CALL CREATE_USER_ACCOUNT('%s', '%s', '%s', '%s', %f, '%s')"%(self.text_account_number, arg[1], password, time.upper(), arg[7], arg[8])
            self.controller.cursor.execute(code)
            t_id = self.create_transaction_id()
            code = "CALL ADD_ADMIN_TRANSACTION('%s', '%s', '%s', '%s', '%s')"%(t_id, time.upper(), self.adminname, "CREATE USER", "Create user " + self.text_account_number)
            self.controller.cursor.execute(code)
            code = "CALL ADD_USER_TRANSACTION('%s', '%s', '%s', '%s', '%s')"%(t_id, time.upper(), self.text_account_number, "CREATE USER", "Created user by " + self.adminname)
            self.controller.cursor.execute(code)
            self.controller.update("Admin_Transaction")
            self.controller.update("Admin_Show_All_Users")
            done = messagebox.showinfo(title = "Create user", message = "You have created user successfull with account number is %s and password is %s"%(self.text_account_number, password))
            if done:
                self.delete()
                self.update()
        else:
            time = date.today().strftime("%b-%d-%Y") + " " + datetime.now().strftime("%H:%M:%S")
            code = "CALL ADD_USER('%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(arg[1], arg[0], arg[3], arg[2], arg[6], arg[4], arg[5])
            self.controller.cursor.execute(code)
            code = "CALL CREATE_USER_ACCOUNT('%s', '%s', '%s', '%s', %f, '%s')"%(self.text_account_number, arg[1], password, time.upper(), arg[7], arg[8])
            self.controller.cursor.execute(code)
            t_id = self.create_transaction_id()
            code = "CALL ADD_ADMIN_TRANSACTION('%s', '%s', '%s', '%s', '%s')"%(t_id, time.upper(), self.adminname, "CREATE USER", "Create user " + self.text_account_number)
            self.controller.cursor.execute(code)
            code = "CALL ADD_USER_TRANSACTION('%s', '%s', '%s', '%s', '%s')"%(t_id, time.upper(), self.text_account_number, "CREATE USER", "Created user by " + self.adminname)
            self.controller.cursor.execute(code)
            self.controller.update("Admin_Show_All_Users")
            self.controller.update("Admin_Transaction")
            done = messagebox.showinfo(title = "Create user", message = "You have created user successfull with account number is %s and password is %s"%(self.text_account_number, password))
            if done:
                self.delete()
                self.update()
                

    def create_transaction_id(self):
        t_id = "AT" + self.controller.rand(5)
        code = """SELECT * FROM ADMIN_TRANSACTION
                WHERE T_ID = '%s'"""%(t_id)
        self.controller.cursor.execute(code)
        result = self.controller.cursor.fetchall()
        while result:
            t_id = "AT" + self.controller.rand(5)
            code = """SELECT * FROM ADMIN_TRANSACTION
                    WHERE T_ID = '%s'"""%(t_id)
            self.controller.cursor.execute(code)
            result = self.controller.cursor.fetchall()
        return t_id

    def update_dob(self):
        year = self.clicked_year.get()
        month = self.clicked_month.get()

        if year != "Year" and month != "Month":
            if year != self.temp_year or month != self.temp_month:
                if year != self.temp_year and self.dob:
                    self.clicked_month.set("Month")
                self.clicked_day.set("Day")

                year = int(year)
                month = int(self.lst_month.index(month)+1)

                if month in (1, 3, 5, 7, 8, 10, 12):
                    self.lst_day = list(range(1, 32))
                elif month in (4, 6, 9, 11):
                    self.lst_day = list(range(1, 31))
                else:
                    self.lst_day = list(range(1, 29))
                if ((year%400 == 0) or (year%4 == 0 and year%100 != 0)) and month == 2:
                    self.lst_day = list(range(1, 30))
                
                menu = self.option_day["menu"]
                menu.delete(0, "end")
                for string in self.lst_day:
                    menu.add_command(label = string, command=lambda value = string: self.clicked_day.set(value))
                
                self.temp_year = str(year)
                self.temp_month = self.lst_month[month-1]
                self.dob = True
        
        self.after(100, self.update_dob)

    def delete(self):
        self.entry_fullname.delete(0, "end")
        self.entry_id.delete(0, "end")
        self.sex_type.set(-1)
        self.clicked_year.set("Year")
        self.clicked_month.set("Month")
        self.clicked_day.set("Day")
        self.entry_phone.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.textbox_address.delete("1.0", "end-1c")
        self.entry_balance.delete(0, "end")
        self.entry_answer.delete(0, "end")

    def back(self):
        self.delete()
        self.controller.show_frame("Admin_HomePage")

    def update(self):
        self.text_account_number = "07008814" + self.controller.rand(4)
        code = """SELECT * FROM USER_ACCOUNT
                WHERE ACC_NUM = '%s'"""%(self.text_account_number)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        while (data):
            self.text_account_number = "07008814" + self.controller.rand(4)
            code = """SELECT * FROM USER_ACCOUNT
                    WHERE ACC_NUM = '%s'"""%(self.text_account_number)
            self.controller.cursor.execute(code)
        self.label_account_number.config(text = self.text_account_number)