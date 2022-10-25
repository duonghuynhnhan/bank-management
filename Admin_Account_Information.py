import tkinter as tk
from tkinter import font
from tkinter.constants import LEFT
from PIL import Image, ImageTk

app_font = "Arial"

class Admin_Account_Information(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.adminname = ""

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = lambda: controller.show_frame("Admin_HomePage"))
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "ACCOUNT INFORMATION", font = (app_font, 20, "bold"), fg = "orange")
        self.label_welcome.pack(pady = 60)

        self.label_adminname = tk.Label(self, text = "Adminname: " + self.adminname, font = (app_font, 18))
        self.label_adminname.pack(pady = 30)

        self.label_date = tk.Label(self, text = "Expiration date: JAN-01-2030", font = (app_font, 18))
        self.label_date.pack(pady = 20)

        self.img_edit_1 = ImageTk.PhotoImage(Image.open("pictures/app/edit.png").resize((40, 40), Image.ANTIALIAS))
        self.button_change_password = tk.Button(self, image = self.img_edit_1, text = "Change your password", font = (app_font, 12, "bold"), border = "0", compound = LEFT, fg = "gray50", command = self.change_password)
        self.button_change_password.place(x = 30, y = 420)

        self.img_edit_2 = ImageTk.PhotoImage(Image.open("pictures/app/edit.png").resize((40, 40), Image.ANTIALIAS))
        self.button_change_password = tk.Button(self, image = self.img_edit_2, text = "Change your answer special question", font = (app_font, 12, "bold"), border = "0", compound = LEFT, fg = "gray50", command = self.change_answer)        
        self.button_change_password.place(x = 30, y = 470)


    def update(self):
        self.label_adminname.config(text = "Adminname: " + self.adminname)

    def change_password(self):
        self.controller.show_frame("Admin_Change_Password")

    def change_answer(self):
        self.controller.show_frame("Admin_Change_Answer")