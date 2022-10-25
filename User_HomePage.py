import tkinter as tk
from tkinter.constants import TOP
from PIL import Image, ImageTk
from datetime import date, datetime
from tkinter import messagebox

app_font = "Arial"

class User_HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = "" 

        self.label_welcome_title = tk.Label(self, text = "Hi ", font = (app_font, 15), fg = "red")
        self.label_welcome_title.place(x = 5, y = 18)
        self.text_welcome = "DUONG HUYNH NHAN"
        self.label_welcome = tk.Label(self, text = self.text_welcome + ",", font = (app_font, 15, "bold"), fg = "green")
        self.label_welcome.place(x = 30, y = 18)

        self.label_time = tk.Label(self, text = "", font = (app_font, 12), fg = "PeachPuff4")
        self.label_time.place(x = 5, y = 48)
        self.time()

        self.img_personal_information = ImageTk.PhotoImage(Image.open("pictures/user/personal_information.png").resize((60, 60), Image.ANTIALIAS))
        self.button_personal_information = tk.Button(self, image = self.img_personal_information, border = "0", text = "Personal\nInformation", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("User_Personal_Information"))
        self.button_personal_information.place(x = 78, y = 100)   

        self.img_account_information = ImageTk.PhotoImage(Image.open("pictures/user/account_information.png").resize((60, 60), Image.ANTIALIAS))
        self.button_account_information = tk.Button(self, image = self.img_account_information, border = "0", text = "Account\nInformation", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("User_Account_Information"))
        self.button_account_information.place(x = 237, y = 100)

        self.img_transaction = ImageTk.PhotoImage(Image.open("pictures/user/transaction.png").resize((60, 60), Image.ANTIALIAS))
        self.button_transaction = tk.Button(self, image = self.img_transaction, border = "0", text = "Transaction", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("User_Transaction"))
        self.button_transaction.place(x = 78, y = 240)

        self.img_withdrawal = ImageTk.PhotoImage(Image.open("pictures/user/withdrawal.png").resize((60, 60), Image.ANTIALIAS))
        self.button_withdrawal = tk.Button(self, image = self.img_withdrawal, border = "0", text = "Withdrawal", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("User_Withdrawal"))
        self.button_withdrawal.place(x = 237, y = 240)

        self.img_recharge = ImageTk.PhotoImage(Image.open("pictures/user/recharge.png").resize((60, 60), Image.ANTIALIAS))
        self.button_recharge = tk.Button(self, image = self.img_recharge, border = "0", text = "Recharge", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("User_Recharge"))
        self.button_recharge.place(x = 80, y = 360)

        self.img_transfer = ImageTk.PhotoImage(Image.open("pictures/user/transfer.png").resize((60, 60), Image.ANTIALIAS))
        self.button_transfer = tk.Button(self, image = self.img_transfer, border = "0", text = "Transfer", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("User_Transfer"))
        self.button_transfer.place(x = 250, y = 360)

        self.img_about = ImageTk.PhotoImage(Image.open("pictures/user/about.png").resize((60, 60), Image.ANTIALIAS))
        self.button_about = tk.Button(self, image = self.img_about, border = "0", text = "About", font = (app_font, 12), compound = TOP, command = lambda: controller.show_frame("User_About"))
        self.button_about.place(x = 90, y = 488)

        self.img_logout = ImageTk.PhotoImage(Image.open("pictures/user/logout.png").resize((60, 60), Image.ANTIALIAS))
        self.button_logout = tk.Button(self, image = self.img_logout, border = "0", text = "Log out", font = (app_font, 12), compound = TOP, command = self.logout)
        self.button_logout.place(x = 255, y = 488)

    def logout(self):
        log_out = messagebox.askokcancel(title = "Log out", message = "Are you sure to log out?")
        if log_out:
            self.controller.delete("User_Transaction")
            self.controller.show_frame("Welcome")

    def time(self):
        t = date.today().strftime("%B-%d-%Y") + " " + datetime.now().strftime("%H:%M:%S")
        self.label_time.config(text = t)
        self.after(1000, self.time)

    def update(self):
        code = """SELECT U.FULL_NAME
                FROM USER AS U JOIN USER_ACCOUNT AS UA ON UA.USER = U.U_ID
                WHERE UA.ACC_NUM = '%s'"""%(self.username)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        self.text_welcome = data[0][0] + ","
        self.label_welcome.config(text = self.text_welcome)