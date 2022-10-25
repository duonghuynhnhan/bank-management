import tkinter as tk
from tkinter.constants import LEFT
from PIL import Image, ImageTk

app_font = "Arial"

class User_Account_Information(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = "" 

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = lambda: controller.show_frame("User_HomePage"))
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "ACCOUNT INFORMATION", font = ("Arial", 20, "bold"), fg = "orange")
        self.label_welcome.pack(pady = 60)

        self.img_card = ImageTk.PhotoImage(Image.open("pictures/user/card.png").resize((300, 250), Image.ANTIALIAS))
        self.label_card = tk.Label(self, image = self.img_card)
        self.label_card.place(x = 48, y = 115)

        self.text_accountnumber = "0700\t8814\t2266"
        self.label_accountnumber = tk.Label(self, text = self.text_accountnumber, font = (app_font, 12, "bold"), fg = "green", border = "0")
        self.label_accountnumber.pack(pady = 75)

        self.text_balance = "1,000,000,000 USD"
        self.label_balance = tk.Label(self, text = self.text_balance, font = (app_font, 15, "bold"), fg = "light slate blue", border = "0")
        self.label_balance.pack(pady = 10)

        self.img_edit_1 = ImageTk.PhotoImage(Image.open("pictures/app/edit.png").resize((40, 40), Image.ANTIALIAS))
        self.button_change_password = tk.Button(self, image = self.img_edit_1, text = "Change your password", font = (app_font, 12, "bold"), border = "0", compound = LEFT, fg = "gray50", command = self.change_password)
        self.button_change_password.place(x = 30, y = 420)

        self.img_edit_2 = ImageTk.PhotoImage(Image.open("pictures/app/edit.png").resize((40, 40), Image.ANTIALIAS))
        self.button_change_password = tk.Button(self, image = self.img_edit_2, text = "Change your answer special question", font = (app_font, 12, "bold"), border = "0", compound = LEFT, fg = "gray50", command = self.change_answer)
        self.button_change_password.place(x = 30, y = 470)

    def update(self):
        self.text_accountnumber = ""
        temp = list(self.username)
        temp.insert(4, "\t")
        temp.insert(9, "\t")
        for index in range(len(temp)):
            self.text_accountnumber += temp[index]
        self.label_accountnumber.config(text = self.text_accountnumber)
        code = """SELECT BALANCE FROM USER_ACCOUNT
                WHERE ACC_NUM = '%s'"""%(self.username)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        self.text_balance = str(data[0][0]) + " USD"
        self.label_balance.config(text = self.text_balance)

    def change_password(self):
        self.controller.show_frame("User_Change_Password")

    def change_answer(self):
        self.controller.show_frame("User_Change_Answer")
