import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

app_font = "Arial"

class User_New_Password(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = ""

        self.img = ImageTk.PhotoImage(Image.open("pictures/app/logo.png").resize((150, 150), Image.ANTIALIAS))
        self.img_label = tk.Label(self, image = self.img)
        self.img_label.pack()

        self.label_welcome = tk.Label(self, text = "NEW PASSWORD", font = (app_font, 20, "bold"), fg = "forest green")
        self.label_welcome.pack()

        self.label_password = tk.Label(self, text = "Input new password (6 digits)", font = (app_font, 12))
        self.label_password.pack(pady = 40)
        self.entry_password = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_password.place(x = 44, y = 265)
        self.button_showpassword = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password)
        self.button_showpassword.place(x = 325, y = 270)

        self.label_password_again = tk.Label(self, text = "Input again new password", font = (app_font, 12))
        self.label_password_again.pack(pady = 30)
        self.entry_password_again = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_password_again.place(x = 44, y = 360)
        self.button_showpassword_again = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password_again)
        self.button_showpassword_again.place(x = 325, y = 365)

        self.button_continue = tk.Button(self, text = "Continue", font = (app_font, 12, "bold"), border = "0", fg = "blue", command = self.confirm)
        self.button_continue.pack(pady = 40)

    def show_password(self):
        self.entry_password.config(show = "")
        self.button_hidepassword = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_password)
        self.button_hidepassword.place(x = 325, y = 270)

    def hide_password(self):
        self.entry_password.config(show = "*")
        self.button_showpassword = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password)
        self.button_showpassword.place(x = 325, y = 270)

    def show_password_again(self):
        self.entry_password_again.config(show = "")
        self.button_hidepassword_again = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_password_again)
        self.button_hidepassword_again.place(x = 325, y = 365)

    def hide_password_again(self):
        self.entry_password_again.config(show = "*")
        self.button_showpassword_again = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password_again)
        self.button_showpassword_again.place(x = 325, y = 365)

    def confirm(self):
        password = self.entry_password.get()
        password_again = self.entry_password_again.get()

        if password and password_again:
            if password.isnumeric():
                if len(password) == 6:
                    if password == password_again:
                        code = "CALL CHANGE_USER_PASSWORD('%s', '%s')"%(self.username, password)
                        self.controller.cursor.execute(code)
                        self.username = ""
                        done = messagebox.showinfo(title = "New password", message = "You have changed password successfully!\nNow, please login again!")
                        if done:
                            self.entry_password.delete(0, "end")
                            self.entry_password_again.delete(0, "end")
                            self.controller.show_frame("User_Login")
                    else:
                        messagebox.showerror(title = "New password", message = "The passwords do not match!")
                else:
                    messagebox.showerror(title = "New password", message = "Password must have a length is 6!")
            else:
                messagebox.showerror(title = "New password", message = "Password must be a sequence of 6 digits!")
        else:
            messagebox.showerror(title = "New password", message = "You must input new password!")