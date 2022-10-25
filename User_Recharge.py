import tkinter as tk
from datetime import date, datetime
from PIL import Image, ImageTk
from tkinter import messagebox

app_font = "Arial"

class User_Recharge(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = ""

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "RECHARGE", font = (app_font, 20, "bold"), fg = "burlywood4")
        self.label_welcome.pack(pady = 80)

        self.label_money = tk.Label(self, text = "Input money you want to recharge", font = (app_font, 12))
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
            money = float(money)
        except:
            money_confirm = False
            messagebox.showerror(title = "Recharge", message = "Money you input invalid!")
            self.entry_money.delete(0, "end")

        if money_confirm:
            if money > 0:
                done = messagebox.askokcancel(title = "Recharge", message = "Are you sure to recharge with money is $%f?"%(money))
                if done:
                    self.recharge(money)
            else:
                messagebox.showerror(title = "Recharge", message = "Money you input invalid!")


    def recharge(self, money):
        code = "CALL RECHARGE('%s', %f)"%(self.username, money)
        self.controller.cursor.execute(code)
        t_id = self.create_transaction_id()
        time = date.today().strftime("%b-%d-%Y") + " " + datetime.now().strftime("%H:%M:%S")
        code = "CALL ADD_USER_TRANSACTION('%s', '%s', '%s', '%s', '%s')"%(t_id, time, self.username, "RECHARGE", "+" + str(money) + " USD")
        self.controller.cursor.execute(code)
        self.controller.update("User_Account_Information")
        self.controller.update("User_Transaction")
        messagebox.showinfo(title = "Recharge", message = "You have successfully recharge with money is $%f!"%(money))
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