import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

app_font = "Arial"

class Admin_Forgot_Password(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)

        self.img = ImageTk.PhotoImage(Image.open("pictures/app/logo.png").resize((150, 150), Image.ANTIALIAS))
        self.img_label = tk.Label(self, image = self.img)
        self.img_label.pack()

        self.img_back = ImageTk.PhotoImage(Image.open("pictures/app/back.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_back, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "FORGOT PASSWORD", font = (app_font, 20, "bold"), fg = "tomato")
        self.label_welcome.pack()

        self.label_adminname = tk.Label(self, text = "Input adminname", font = (app_font, 12))
        self.label_adminname.pack(pady = 40)
        self.entry_adminname = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5)
        self.entry_adminname.place(x = 64, y = 265)

        self.label_answer = tk.Label(self, text = "Input answer of special question", font = (app_font, 12))
        self.label_answer.pack(pady = 30)
        self.entry_answer = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_answer.place(x = 44, y = 360)
        self.button_show_answer = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_answer)
        self.button_show_answer.place(x = 325, y = 365)

        self.button_continue = tk.Button(self, text = "Continue", font = (app_font, 12, "bold"), border = "0", fg = "blue", command = self.confirm)
        self.button_continue.pack(pady = 40)

    def show_answer(self):
        self.entry_answer.config(show = "")
        self.button_hide_answer = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_answer)
        self.button_hide_answer.place(x = 325, y = 365)

    def hide_answer(self):
        self.entry_answer.config(show = "*")
        self.button_show_answer = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_answer)
        self.button_show_answer.place(x = 325, y = 365)

    def confirm(self):
        adminname = self.entry_adminname.get()
        answer = self.entry_answer.get()
        
        if adminname and answer:
            code = """SELECT ANSWER FROM ADMIN_ACCOUNT
                    WHERE ACC_NUM = '%s'"""%(adminname)
            self.controller.cursor.execute(code)
            data = self.controller.cursor.fetchall()
            if data:
                if answer == data[0][0]:
                    self.delete()
                    self.controller.frames["Admin_New_Password"].adminname = adminname
                    self.controller.show_frame("Admin_New_Password")
                else:
                    self.delete()
                    messagebox.showerror(title = "Forgot password", message = "Adminname or answer invalid!")
            else:
                self.delete()
                messagebox.showerror(title = "Forgot password", message = "Adminname or answer invalid!")
        else:
            self.delete()
            messagebox.showerror(title = "Forgot password", message = "You must input all information")

    def back(self):
        self.delete()
        self.controller.show_frame("Admin_Login")

    def delete(self):
        self.entry_adminname.delete(0, "end")
        self.entry_answer.delete(0, "end")