import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, VERTICAL, Y
from tkinter import ttk
from PIL import Image, ImageTk

app_font = "Arial"

class Admin_Show_All_Users(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600) 
        self.adminname = "" 
        self.count = 0

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = lambda: controller.show_frame("Admin_HomePage"))
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "SHOW ALL USERS", font = ("Arial", 20, "bold"), fg = "firebrick3")
        self.label_welcome.pack(pady = 60)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side = LEFT, fill = BOTH, expand = 1)

        self.scrollbar = ttk.Scrollbar(self, orient = VERTICAL, command = self.canvas.yview)
        self.scrollbar.pack(side = RIGHT, fill = Y)

        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        self.temp_frame = tk.Frame(self.canvas)

        self.canvas.create_window((0, 0), window = self.temp_frame, anchor = "nw")

    def update(self):
        code = """SELECT UA.ACC_NUM, U.FULL_NAME 
                FROM USER_ACCOUNT AS UA JOIN USER AS U ON UA.USER = U.U_ID
                ORDER BY UA.CREATE_DATE"""
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        length = len(data)
        if length > self.count:
            for index in range(self.count, length):
                tk.Label(self.temp_frame, text = data[index][0] + " - " + data[index][1], fg = "green", font = (app_font, 12)).pack()
            self.count = length