import tkinter as tk
from tkinter.constants import TOP
from PIL import Image, ImageTk
from datetime import date, datetime
from tkinter import messagebox

app_font = "Arial"

class Admin_HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.adminname = "" 

        self.label_welcome_title = tk.Label(self, text = "Hi ", font = (app_font, 15), fg = "red")
        self.label_welcome_title.place(x = 5, y = 18)
        self.text_welcome = "ADMIN (KEVIN. H. N. DUONG)"
        self.label_welcome = tk.Label(self, text = self.text_welcome + ",", font = (app_font, 15, "bold"), fg = "Magenta4")
        self.label_welcome.place(x = 30, y = 18)

        self.label_time = tk.Label(self, text = "", font = (app_font, 12), fg = "PeachPuff4")
        self.label_time.place(x = 5, y = 48)
        self.time()
        
        self.img_personal_information = ImageTk.PhotoImage(Image.open("pictures/admin/personal_information.png").resize((60, 60), Image.ANTIALIAS))
        self.button_personal_information = tk.Button(self, image = self.img_personal_information, border = "0", text = "Personal\nInformation", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("Admin_Personal_Information"))
        self.button_personal_information.place(x = 78, y = 100)

        self.img_admin_information = ImageTk.PhotoImage(Image.open("pictures/admin/admin_information.png").resize((60, 60), Image.ANTIALIAS))
        self.button_admin_information = tk.Button(self, image = self.img_admin_information, border = "0", text = "Account\nInformation", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("Admin_Account_Information"))
        self.button_admin_information.place(x = 237, y = 100)

        self.img_transaction = ImageTk.PhotoImage(Image.open("pictures/admin/transaction.png").resize((60, 60), Image.ANTIALIAS))
        self.button_transaction = tk.Button(self, image = self.img_transaction, border = "0", text = "Transaction", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("Admin_Transaction"))
        self.button_transaction.place(x = 78, y = 240)

        self.img_show_all_users = ImageTk.PhotoImage(Image.open("pictures/admin/show_all_users.png").resize((60, 60), Image.ANTIALIAS))
        self.button_show_all_users = tk.Button(self, image = self.img_show_all_users, border = "0", text = "Show all users", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("Admin_Show_All_Users"))
        self.button_show_all_users.place(x = 225, y = 240)

        self.img_create_user = ImageTk.PhotoImage(Image.open("pictures/admin/create_user.png").resize((60, 60), Image.ANTIALIAS))
        self.button_create_user = tk.Button(self, image = self.img_create_user, border = "0", text = "Create user", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("Admin_Create_User"))
        self.button_create_user.place(x = 78, y = 360)

        self.img_check_user = ImageTk.PhotoImage(Image.open("pictures/admin/check_user.png").resize((60, 60), Image.ANTIALIAS))
        self.button_check_user = tk.Button(self, image = self.img_check_user, border = "0", text = "Check user", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("Admin_Check_User"))
        self.button_check_user.place(x = 240, y = 360)

        self.img_about = ImageTk.PhotoImage(Image.open("pictures/admin/about.png").resize((60, 60), Image.ANTIALIAS))
        self.button_about = tk.Button(self, image = self.img_about, border = "0", text = "About", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("Admin_About"))
        self.button_about.place(x = 90, y = 488)

        self.img_logout = ImageTk.PhotoImage(Image.open("pictures/admin/logout.png").resize((60, 60), Image.ANTIALIAS))
        self.button_logout = tk.Button(self, image = self.img_logout, border = "0", text = "Log out", font = (app_font, 12), compound = TOP, command = self.logout)
        self.button_logout.place(x = 255, y = 488)

    def update(self):
        code = """SELECT A.FULL_NAME
                FROM ADMIN AS A JOIN ADMIN_ACCOUNT AS AA ON AA.ADMIN = A.A_ID
                WHERE AA.ACC_NUM = '%s'"""%(self.adminname)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        self.text_welcome = "ADMIN (" + data[0][0] + "),"
        self.label_welcome.config(text = self.text_welcome)

    def logout(self):
        log_out = messagebox.askokcancel(title = "Log out", message = "Are you sure to log out?")
        if log_out:
            self.controller.delete("Admin_Transaction")
            self.controller.delete("Admin_Show_All_Users")
            self.adminname = ""
            self.controller.show_frame("Welcome")

    def time(self):
        t = date.today().strftime("%B-%d-%Y") + " " + datetime.now().strftime("%H:%M:%S")
        self.label_time.config(text = t)
        self.after(1000, self.time)