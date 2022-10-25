import tkinter as tk
from tkinter.constants import LEFT
from PIL import Image, ImageTk

app_font = "Arial"

class Admin_Check_User(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.adminname = ""  
        self.lst_label = []

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = self.back)
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "CHECK USER", font = ("Arial", 20, "bold"), fg = "medium orchid")
        self.label_welcome.pack(pady = 20)

        self.label_input = tk.Label(self, text = "Input ID/Passport/Account number", font = (app_font, 12))
        self.label_input.pack(pady = 10)

        self.entry_input = tk.Entry(self, font = (app_font, 12, "bold"), width = 30, bd = 5)
        self.entry_input.pack()

        self.button_check = tk.Button(self, text = "Check", font = (app_font, 12, "bold"), border = "0", fg = "blue", command = self.check)
        self.button_check.pack()

        self.canvas = tk.Canvas(self)
        self.canvas.create_line(9, 2, 380, 2)
        self.canvas.place(x = 5, y = 180)

        self.label_notfound = tk.Label(self, text = "", font = (app_font, 12, "bold"), fg = "red")
        self.label_notfound.pack(pady = 20)

        self.label_id = tk.Label(self, text = "", font = (app_font, 12, "bold"), fg = "green")
        self.label_id.pack()

        self.label_fullname = tk.Label(self, text = "", font = (app_font, 12, "bold"), fg = "blue")
        self.label_fullname.pack()

        for index in range(10):
            self.lst_label.append(tk.Label(self, text = "", font = (app_font, 12, "bold"), fg = "orange"))
            self.lst_label[index].pack()

    def check(self):
        self.refresh()
        input = self.entry_input.get()
        code1 = """SELECT * FROM USER
                WHERE U_ID = '%s'"""%(input)
        self.controller.cursor.execute(code1)
        data_1 = self.controller.cursor.fetchall()

        code2 = """SELECT * FROM USER_ACCOUNT
                WHERE ACC_NUM = '%s'"""%(input)
        self.controller.cursor.execute(code2)
        data_2 = self.controller.cursor.fetchall()

        if not data_1 and not data_2:
            self.label_notfound.config(text = "NOT FOUND USER!")
        else:
            if data_1:
                id, fullname = data_1[0][0], data_1[0][1]
                self.label_id.config(text = id)
                self.label_fullname.config(text = fullname)
                code = """SELECT UA.ACC_NUM
                        FROM USER_ACCOUNT AS UA JOIN USER AS U ON UA.USER = U.U_ID
                        WHERE U.U_ID = '%s'"""%(id)
                self.controller.cursor.execute(code)
                lst_accnum = self.controller.cursor.fetchall()
                for index in range(len(lst_accnum)):
                    self.lst_label[index].config(text = lst_accnum[index][0])
            else:
                code = """SELECT U.U_ID, U.FULL_NAME
                        FROM USER_ACCOUNT AS UA JOIN USER AS U ON UA.USER = U.U_ID
                        WHERE UA.ACC_NUM = '%s'"""%(input)
                self.controller.cursor.execute(code)
                data = self.controller.cursor.fetchall()
                self.lst_label[0].config(text = input)
                self.label_id.config(text = data[0][0])
                self.label_fullname.config(text = data[0][1])

    def refresh(self):
        self.label_notfound.config(text = "")
        self.label_id.config(text = "")
        self.label_fullname.config(text = "")
        for index in range(10):
            self.lst_label[index].config(text = "")
        self.label_notfound.config(text = "")

    def back(self):
        self.entry_input.delete(0, "end")
        self.refresh()
        self.controller.show_frame("Admin_HomePage")

    def update(self):
        pass