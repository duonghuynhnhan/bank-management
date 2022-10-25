import tkinter as tk
from datetime import date, datetime
from tkinter import messagebox
from PIL import Image, ImageTk

app_font = "Arial"

class User_Transfer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600) 
        self.username = ""
        self.name = ""

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "TRANSFER", font = ("Arial", 20, "bold"), fg = "medium orchid")
        self.label_welcome.pack(pady = 60)

        self.label_account = tk.Label(self, text = "Input account number you want to transfer", font = (app_font, 12))
        self.label_account.place(x = 30, y = 150)

        self.entry_account_number = tk.Entry(self, font = (app_font, 12, "bold"), bd = 5)
        self.entry_account_number.place(x = 105, y = 185)

        self.label_name = tk.Label(self, text = "", font = (app_font, 12, "bold"), fg = "green")
        self.label_name.pack(pady = 65)

        self.check_account_number()

        self.label_money = tk.Label(self, text = "Input money you want to transfer", font = (app_font, 12))
        self.label_money.place(x = 30, y = 250)

        self.entry_money = tk.Entry(self, font = (app_font, 12, "bold"), bd = 5)
        self.entry_money.place(x = 105, y = 285)

        self.label_message = tk.Label(self, text = "Message", font = (app_font, 12))
        self.label_message.place(x = 30, y = 350)

        self.text_message = tk.Text(self, font = (app_font, 12, "bold"), height = 3, width = 30, bd = 5, endline = 40)
        self.text_message.place(x = 60, y = 385)

        self.button_continue = tk.Button(self, text = "Continue", font = (app_font, 12, "bold"), fg = "blue", border = "0", command = self.confirm)
        self.button_continue.place(x = 160, y = 500)

    def update(self):
        pass

    def check_account_number(self):
        self.account_number_check = False
        account_number = self.entry_account_number.get()

        if len(account_number) == 0:
            self.label_name.config(text = "")
            self.account_number_check = False
        else:
            code = """SELECT U.FULL_NAME
                    FROM USER_ACCOUNT AS UA JOIN USER AS U ON UA.USER = U.U_ID
                    WHERE UA.ACC_NUM = '%s'"""%(account_number)
            self.controller.cursor.execute(code)
            data = self.controller.cursor.fetchall()
            if data:
                self.name = data[0][0]
                self.label_name.config(text = data[0][0], fg = "green")
                self.account_number_check = True
            else:
                self.label_name.config(text = "NOT FOUND ACCOUNT NUMBER!", fg = "red")
                self.account_number_check = False
        self.after(100, self.check_account_number)

    def confirm(self):
        account_number = self.entry_account_number.get()
        money = self.entry_money.get()
        message = self.text_message.get("1.0", "end-1c")
        done = True
        code = """SELECT BALANCE FROM USER_ACCOUNT
                WHERE ACC_NUM = '%s'"""%(self.username)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        balance = data[0][0]

        if account_number and money and message:
            if len(message) > 40:
                messagebox.showerror(title = "Transfer", message = "Length of message must smaller 40!")
            else:
                try:
                    money = float(money)
                except:
                    messagebox.showerror(title = "Transfer", message = "Money you input invalid!")
                    done = False
                
                if done:
                    if self.account_number_check and account_number != self.username:
                        if 0 < money < balance:
                            self.transfer(account_number, money, message)
                        else:
                            messagebox.showerror(title = "Transfer", message = "Money you input invalid!")
                    else:
                        messagebox.showerror(title = "Transfer", message = "Account number you input invalid!")
        else:
            messagebox.showerror(title = "Transfer", message = "You must input all information!")

    def transfer(self, destination, money, message):
        done = messagebox.askokcancel(title = "Transfer", message = "Are you sure transfer to %s (%s) with money is $%s!"%(destination, self.name, money))
        if done:
            code = "CALL TRANSFER('%s', '%s', %f)"%(self.username, destination, money)
            self.controller.cursor.execute(code)

            t_id = self.create_transaction_id()
            time = date.today().strftime("%b-%d-%Y") + " " + datetime.now().strftime("%H:%M:%S")
            code = "CALL ADD_USER_TRANSACTION('%s', '%s', '%s', '%s', '%s')"%(t_id, time, self.username, "TRANSFER TO " + destination, "-" + str(money) + " USD\n" + message)
            self.controller.cursor.execute(code)

            t_id = self.create_transaction_id()
            code = "CALL ADD_USER_TRANSACTION('%s', '%s', '%s', '%s', '%s')"%(t_id, time, destination, "RECEIVE FROM " + self.username, "+" + str(money) + " USD\n" + message)
            self.controller.cursor.execute(code)
        
            self.controller.update("User_Account_Information")
            self.controller.update("User_Transaction")
            self.entry_account_number.delete(0, "end")
            self.entry_money.delete(0, "end")
            self.text_message.delete("1.0", "end-1c")
            messagebox.showinfo(title = "Transfer", message = "You have transfered successfully to %s (%s) with money is $%s!"%(destination, self.name, money))

    def back(self):
        self.entry_account_number.delete(0, "end")
        self.entry_money.delete(0, "end")
        self.text_message.delete("1.0", "end-1c")
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