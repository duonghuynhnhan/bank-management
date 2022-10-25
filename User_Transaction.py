import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT, RIGHT, VERTICAL, Y
from PIL import Image, ImageTk

app_font = "Arial"

class User_Transaction(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = "" 
        self.count = 0

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = lambda: controller.show_frame("User_HomePage"))
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "TRANSACTION", font = ("Arial", 20, "bold"), fg = "medium turquoise")
        self.label_welcome.pack(pady = 40)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side = LEFT, fill = BOTH, expand = 1)

        self.scrollbar = ttk.Scrollbar(self, orient = VERTICAL, command = self.canvas.yview)
        self.scrollbar.pack(side = RIGHT, fill = Y)

        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        self.temp_frame = tk.Frame(self.canvas)

        self.canvas.create_window((0, 0), window = self.temp_frame, anchor = "nw")

    def update(self):
        code = """SELECT * FROM USER_TRANSACTION 
                WHERE WHO = '%s'
                ORDER BY T_TIME"""%(self.username)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()
        length = len(data)
        if length > self.count:
            for index in range(self.count, length):
                id = data[index][0]
                date = str(data[index][1].strftime("%b-%d-%Y %H:%M:%S")).upper()
                type = data[index][3]
                message = data[index][4]
                tk.Label(self.temp_frame, text = id + " | " + date, font = (app_font, 12), fg = "green").pack()
                tk.Label(self.temp_frame, text = "Type: " + type, font = (app_font, 12), fg = "Violet red").pack()
                tk.Label(self.temp_frame, text = "Message: " + message, font = (app_font, 12), fg = "navy").pack()
            self.count = length