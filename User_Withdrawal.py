import tkinter as tk
from datetime import date, datetime
from PIL import Image, ImageTk
from tkinter import messagebox

app_font = "Arial"

class User_Withdrawal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = "" 

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "WITHDRAWAL", font = (app_font, 20, "bold"), fg = "firebrick3")
        self.label_welcome.pack(pady = 80)

        self.label_money = tk.Label(self, text = "Input money you want to withdrawal", font = (app_font, 12))
        self.label_money.pack(pady = 20)

        self.entry_money = tk.Entry(self, font = (app_font, 12, "bold"), bd = 5)
        self.entry_money.pack()

        self.button_continue = tk.Button(self, text = "Continue", font = (app_font, 12, "bold"), fg = "blue", border = "0", command = self.confirm)
        self.button_continue.pack(pady = 30)

    def update(self):
        pass

    def confirm(self):
        money = self.entry_money.get()
        money_confirm = True

        try:
            money = int(money)
        except:
            messagebox.showerror(title = "Withdrawal", message = "Money you input invalid!")
            money_confirm = False
            self.entry_money.delete(0, "end")
        
        if money_confirm:
            if money > 0:
                done = messagebox.askokcancel(title = "Withdrawal", message = "Are you sure to withdrawal with money is $%d?"%(money))
                if done:
                    self.withdrawal(money)
            else:
                messagebox.showerror(title = "Withdrawal", message = "Money you input invalid!")


    def withdrawal(self, money):
        code = """SELECT BALANCE FROM USER_ACCOUNT
                WHERE ACC_NUM = '%s'"""%(self.username)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        balance = data[0][0]
        if money <= balance:
            code = "CALL WITHDRAWAL('%s', %f)"%(self.username, money)
            self.controller.cursor.execute(code)
            t_id = self.create_transaction_id()
            time = date.today().strftime("%b-%d-%Y") + " " + datetime.now().strftime("%H:%M:%S")
            code = "CALL ADD_USER_TRANSACTION('%s', '%s', '%s', '%s', '%s')"%(t_id, time, self.username, "WITHDRAWAL", "-" + str(money) + " USD")
            self.controller.cursor.execute(code)
            self.controller.update("User_Account_Information")
            self.controller.update("User_Transaction")
            messagebox.showinfo(title = "Withdrawal", message = "You have successfully withdrawn with money is $%d!"%(money))
        else:
            messagebox.showerror(title = "Withdrawal", message = "The current balance in your account is not enough to make a transaction!")
        self.entry_money.delete(0, "end")
    
    def back(self):
        self.entry_money.delete(0, "end")
        self.controller.show_frame("User_HomePage")

    def create_transaction_id(self):
        t_id = "UT" + self.controller.rand(5)
        code = """SELECT * FROM USER_TRANSACTION
                WHERE T_ID = '%s'"""%(t_id)
        self.controller.cursor.execute(code)
        result = self.controller.cursor.fetchall()
        while result:
            t_id = "UT" + self.controller.rand(5)
            code = """SELECT * FROM USER_TRANSACTION
                    WHERE T_ID = '%s'"""%(t_id)
            self.controller.cursor.execute(code)
            result = self.controller.cursor.fetchall()
        return t_id