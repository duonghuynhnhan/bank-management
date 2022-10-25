import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

app_font = "Arial"

class User_Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)

        self.img = ImageTk.PhotoImage(Image.open("pictures/app/logo.png").resize((220, 220), Image.ANTIALIAS))
        self.img_label = tk.Label(self, image = self.img)
        self.img_label.pack()

        self.img_back = ImageTk.PhotoImage(Image.open("pictures/app/back.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_back, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)
        
        self.label_username = tk.Label(self, text = "username", font = (app_font, 18))
        self.label_username.place(x = 5, y = 255)

        self.entry_username = tk.Entry(self, font = (app_font, 14, "bold"), bd = 5)
        self.entry_username.place(x = 125, y = 257)

        self.label_password = tk.Label(self, text = "password", font = (app_font, 18))
        self.label_password.place(x = 5, y = 300)

        self.entry_password = tk.Entry(self, font = (app_font, 14, "bold"), show = "*", bd = 5)
        self.entry_password.place(x = 125, y = 300)
        
        self.button_showpassword = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password)
        self.button_showpassword.place(x = 356, y = 308)

        self.button_login = tk.Button(self, text = "LOG IN", font = (app_font, 20, "bold"), command = self.login, width = 20, bg = "blue", fg = "white")
        self.button_login.place(x = 24, y = 390)

        self.button_forgotpassword = tk.Button(self, text = "Forgot password?", font = (app_font, 15, "bold"), fg = "blue", border = "0", command = self.forgot_password)
        self.button_forgotpassword.place(x = 110, y = 480)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username and password:
            code = """SELECT PASS FROM USER_ACCOUNT
                    WHERE ACC_NUM = '%s'"""%(username)
            self.controller.cursor.execute(code)
            data = self.controller.cursor.fetchall()
            if data:
                db_password = data[0][0]
                if password == db_password:
                    self.delete_login()
                    self.controller.send_data("user", username)
                    self.controller.show_frame("User_HomePage")
                else:
                    self.error_login = messagebox.showerror(title = "Log in", message = "Username or password invalid!")
                    if self.error_login == "ok":
                        self.delete_login()
            else:
                self.error_login = messagebox.showerror(title = "Log in", message = "Username or password invalid!")
                if self.error_login == "ok":
                    self.delete_login()
        else:
            self.error_login = messagebox.showerror(title = "Log in", message = "Username or password invalid!")
            if self.error_login == "ok":
                self.delete_login()

    def back(self):
        self.delete_login()
        self.hide_password()
        self.controller.show_frame("Welcome")

    def show_password(self):
        self.entry_password.config(show = "")
        self.button_hidepassword = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_password)
        self.button_hidepassword.place(x = 356, y = 308)

    def hide_password(self):
        self.entry_password.config(show = "*")
        self.button_showpassword = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password)
        self.button_showpassword.place(x = 356, y = 308)

    def forgot_password(self):
        self.delete_login()
        self.controller.show_frame("User_Forgot_Password")

    def delete_login(self):
        self.entry_username.delete(0, "end")
        self.entry_password.delete(0, "end")