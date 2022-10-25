import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

app_font = "Arial"

class Admin_Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)

        self.img = ImageTk.PhotoImage(Image.open("pictures/app/logo.png").resize((220, 220), Image.ANTIALIAS))
        self.img_label = tk.Label(self, image = self.img)
        self.img_label.pack()

        self.img_return = ImageTk.PhotoImage(Image.open("pictures/app/back.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_return, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)
        
        self.label_adminname = tk.Label(self, text = "adminname", font = (app_font, 18))
        self.label_adminname.place(x = 0, y = 255)

        self.entry_adminname = tk.Entry(self, font = (app_font, 14, "bold"), bd = 5)
        self.entry_adminname.place(x = 132, y = 257)

        self.label_password = tk.Label(self, text = "password", font = (app_font, 18))
        self.label_password.place(x = 0, y = 300)

        self.entry_password = tk.Entry(self, font = (app_font, 14, "bold"), show = "*", bd = 5)
        self.entry_password.place(x = 132, y = 300)
        
        self.button_showpassword = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password)
        self.button_showpassword.place(x = 360, y = 308)

        self.button_login = tk.Button(self, text = "LOG IN", font = (app_font, 20, "bold"), command = self.login, width = 20, bg = "blue", fg = "white")
        self.button_login.place(x = 24, y = 390)

        self.button_forgotpassword = tk.Button(self, text = "Forgot password?", font = (app_font, 15, "bold"), fg = "blue", border = "0", command = self.forgot_password)
        self.button_forgotpassword.place(x = 110, y = 480)

    def login(self):
        adminname = self.entry_adminname.get()
        password = self.entry_password.get()

        if adminname and password:
            code = """SELECT PASS FROM ADMIN_ACCOUNT
                    WHERE ACC_NUM = '%s'"""%(adminname)
            self.controller.cursor.execute(code)
            data = self.controller.cursor.fetchall()
            if data:
                db_password = data[0][0]
                if password == db_password:
                    self.delete_login()
                    self.controller.send_data("admin", adminname)
                    self.controller.show_frame("Admin_HomePage")
                else:
                    self.error_login = messagebox.showerror(title = "Log in", message = "Adminname or password invalid!")
                    if self.error_login == "ok":
                        self.delete_login()
            else:
                self.error_login = messagebox.showerror(title = "Log in", message = "Adminname or password invalid!")
                if self.error_login == "ok":
                    self.delete_login()
        else:
            self.error_login = messagebox.showerror(title = "Log in", message = "Adminname or password invalid!")
            if self.error_login == "ok":
                self.delete_login()

    def back(self):
        self.delete_login()
        self.hide_password()
        self.controller.show_frame("Welcome")

    def show_password(self):
        self.entry_password.config(show = "")
        self.button_hidepassword = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_password)
        self.button_hidepassword.place(x = 360, y = 308)

    def hide_password(self):
        self.entry_password.config(show = "*")
        self.button_showpassword = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password)
        self.button_showpassword.place(x = 360, y = 308)

    def forgot_password(self):
        self.delete_login()
        self.controller.show_frame("Admin_Forgot_Password")

    def delete_login(self):
        self.entry_adminname.delete(0, "end")
        self.entry_password.delete(0, "end")