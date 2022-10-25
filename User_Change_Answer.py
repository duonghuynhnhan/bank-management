import tkinter as tk
from tkinter import messagebox
from tkinter.constants import LEFT
from PIL import Image, ImageTk

app_font = "Arial"

class User_Change_Answer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = "" 

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/back.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "CHANGE ANSWER", font = ("Arial", 20, "bold"), fg = "green")
        self.label_welcome.pack(pady = 60)

        self.label_old_answer = tk.Label(self, text = "Input old answer", font = (app_font, 12))
        self.label_old_answer.pack(pady = 10)
        self.entry_old_answer = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_old_answer.place(x = 44, y = 200)
        self.button_show_old_answer = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_old_answer)
        self.button_show_old_answer.place(x = 325, y = 205)

        self.label_new_answer = tk.Label(self, text = "Input new answer", font = (app_font, 12))
        self.label_new_answer.pack(pady = 52)
        self.entry_new_answer = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_new_answer.place(x = 44, y = 285)
        self.button_show_new_answer = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_new_answer)
        self.button_show_new_answer.place(x = 325, y = 290)

        self.label_answer_again = tk.Label(self, text = "Input new answer again", font = (app_font, 12))
        self.label_answer_again.pack(pady = 10)
        self.entry_answer_again = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5, show = "*")
        self.entry_answer_again.place(x = 44, y = 370)
        self.button_showanswer_again = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_answer_again)
        self.button_showanswer_again.place(x = 325, y = 375)

        self.button_continue = tk.Button(self, text = "Continue", fg = "blue", border = "0", font = (app_font, 12, "bold"), command = self.confirm)
        self.button_continue.place(x = 161, y = 470)

    def update(self):
        pass

    def confirm(self):
        oldanswer = self.entry_old_answer.get()
        newanswer = self.entry_new_answer.get()
        newansweragain = self.entry_answer_again.get()

        if oldanswer and newanswer and newansweragain:
            code = """SELECT ANSWER FROM USER_ACCOUNT
                    WHERE ACC_NUM = '%s'"""%(self.username)
            self.controller.cursor.execute(code)
            data = self.controller.cursor.fetchall()
            db_answer = data[0][0]
            if oldanswer == db_answer:
                if newanswer == newansweragain:
                    code = "CALL CHANGE_USER_ANSWER('%s', '%s')"%(self.username, newanswer)
                    self.controller.cursor.execute(code)
                    done = messagebox.showinfo(title = "Change answer", message = "You have changed answer of special question successfully!")
                    if done:
                        self.delete()
                        self.controller.show_frame("User_Account_Information")
                else:
                    messagebox.showerror(title = "Change answer", message = "New answer doesn't match!")
                    self.delete()
            else:
                messagebox.showerror(title = "Change answer", message = "Old answer invalid!")
                self.delete()
        else:
            messagebox.showerror(title = "Change answer", message = "You must input all information!")
            self.delete()

    def show_old_answer(self):
        self.entry_old_answer.config(show = "")
        self.button_hide_old_answer = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_old_answer)
        self.button_hide_old_answer.place(x = 325, y = 205)

    def hide_old_answer(self):
        self.entry_old_answer.config(show = "*")
        self.button_show_old_answer = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_old_answer)
        self.button_show_old_answer.place(x = 325, y = 205)

    def show_new_answer(self):
        self.entry_new_answer.config(show = "")
        self.button_hide_new_answer = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_new_answer)
        self.button_hide_new_answer.place(x = 325, y = 290)

    def hide_new_answer(self):
        self.entry_new_answer.config(show = "*")
        self.button_show_new_answer = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_new_answer)
        self.button_show_new_answer.place(x = 325, y = 290)

    def show_answer_again(self):
        self.entry_answer_again.config(show = "")
        self.button_hideanswer_again = tk.Button(self, text = "HIDE", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.hide_answer_again)
        self.button_hideanswer_again.place(x = 325, y = 375)

    def hide_answer_again(self):
        self.entry_answer_again.config(show = "*")
        self.button_showanswer_again = tk.Button(self, text = "SHOW", font = (app_font, 8, "bold"), width = 5, border = "0", command = self.show_answer_again)
        self.button_showanswer_again.place(x = 325, y = 375)

    def back(self):
        self.delete()
        self.controller.show_frame("User_Account_Information")

    def delete(self):
        self.entry_old_answer.delete(0, "end")
        self.entry_new_answer.delete(0, "end")
        self.entry_answer_again.delete(0, "end")
        self.hide_old_answer()
        self.hide_new_answer()
        self.hide_answer_again()