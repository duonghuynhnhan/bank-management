import tkinter as tk
from tkinter import messagebox
from tkinter.constants import LEFT
from PIL import Image, ImageTk

app_font = "Arial"

class User_Change_Password(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = "" 

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/back.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "CHANGE PASSWORD", font = ("Arial", 20, "bold"), fg = "green")
        self.label_welcome.pack(pady = 60)

        self.label_old_password = tk.Label(self, text = "Input old password", font = (app_font, 12))
        self.label_old_password.pack(pady = 10)
        self.entry_old_password = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_old_password.place(x = 44, y = 200)
        self.button_show_old_password = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_old_password)
        self.button_show_old_password.place(x = 325, y = 205)

        self.label_new_password = tk.Label(self, text = "Input new password (6 digits)", font = (app_font, 12))
        self.label_new_password.pack(pady = 52)
        self.entry_new_password = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_new_password.place(x = 44, y = 285)
        self.button_show_new_password = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_new_password)
        self.button_show_new_password.place(x = 325, y = 290)

        self.label_password_again = tk.Label(self, text = "Input new password again", font = (app_font, 12))
        self.label_password_again.pack(pady = 10)
        self.entry_password_again = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_password_again.place(x = 44, y = 370)
        self.button_showpassword_again = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password_again)
        self.button_showpassword_again.place(x = 325, y = 375)

        self.button_continue = tk.Button(self, text = "Continue", fg = "blue", border = "0", font = (app_font, 12, "bold"), command = self.confirm)
        self.button_continue.place(x = 161, y = 470)

    def update(self):
        pass

    def confirm(self):
        oldpassword = self.entry_old_password.get()
        newpassword = self.entry_new_password.get()
        newpasswordagain = self.entry_password_again.get()

        if oldpassword and newpassword and newpasswordagain:
            code = """SELECT PASS FROM USER_ACCOUNT
                    WHERE ACC_NUM = '%s'"""%(self.username)
            self.controller.cursor.execute(code)
            data = self.controller.cursor.fetchall()
            db_password = data[0][0]
            if oldpassword == db_password:
                if newpassword == newpasswordagain:
                    if len(newpassword) == 6:
                        code = "CALL CHANGE_USER_PASSWORD('%s', '%s')"%(self.username, newpassword)
                        self.controller.cursor.execute(code)
                        done = messagebox.showinfo(title = "Change password", message = "You have changed password successfully!")
                        if done:
                            self.delete()
                            self.controller.show_frame("User_Account_Information")
                    else:
                        messagebox.showerror(title = "Change password", message = "New password must has 6 digits!")
                        self.delete()
                else:
                    messagebox.showerror(title = "Change password", message = "New password doesn't match!")
                    self.delete()
            else:
                messagebox.showerror(title = "Change password", message = "Old password invalid!")
                self.delete()
        else:
            messagebox.showerror(title = "Change password", message = "You must input all information!")
            self.delete()

    def show_old_password(self):
        self.entry_old_password.config(show = "")
        self.button_hide_old_password = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_old_password)
        self.button_hide_old_password.place(x = 325, y = 205)

    def hide_old_password(self):
        self.entry_old_password.config(show = "*")
        self.button_show_old_password = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_old_password)
        self.button_show_old_password.place(x = 325, y = 205)

    def show_new_password(self):
        self.entry_new_password.config(show = "")
        self.button_hide_new_password = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_new_password)
        self.button_hide_new_password.place(x = 325, y = 290)

    def hide_new_password(self):
        self.entry_new_password.config(show = "*")
        self.button_show_new_password = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_new_password)
        self.button_show_new_password.place(x = 325, y = 290)

    def show_password_again(self):
        self.entry_password_again.config(show = "")
        self.button_hidepassword_again = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_password_again)
        self.button_hidepassword_again.place(x = 325, y = 375)

    def hide_password_again(self):
        self.entry_password_again.config(show = "*")
        self.button_showpassword_again = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_password_again)
        self.button_showpassword_again.place(x = 325, y = 375)

    def back(self):
        self.delete()
        self.controller.show_frame("User_Account_Information")

    def delete(self):
        self.entry_old_password.delete(0, "end")
        self.entry_new_password.delete(0, "end")
        self.entry_password_again.delete(0, "end")
        self.hide_old_password()
        self.hide_new_password()
        self.hide_password_again()