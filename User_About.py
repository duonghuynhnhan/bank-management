import tkinter as tk
from PIL import Image, ImageTk

app_font = "Arial"

class User_About(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600) 

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = lambda: controller.show_frame("User_HomePage"))
        self.button_back.place(x = 0, y = 0)

        self.img = ImageTk.PhotoImage(Image.open("pictures/app/logo.png").resize((150, 150), Image.ANTIALIAS))
        self.img_label = tk.Label(self, image = self.img)
        self.img_label.pack()

        self.label_welcome = tk.Label(self, text = "ABOUT", font = ("Arial", 20, "bold"), fg = "VioletRed2")
        self.label_welcome.place(x = 150, y = 160)

        self.label_about_app = tk.Label(self, text = "Application Information", font = (app_font, 12, "bold italic"), fg = "blue")
        self.label_about_app.place(x = 10, y = 220)

        self.canvas_1 = tk.Canvas(self)
        self.canvas_1.create_line(5, 2, 380, 2)
        self.canvas_1.place(x = 5, y = 245)

        self.label_version = tk.Label(self, text = "CNTT CLC F3 Bank Application\nVersion 2021.1.0", font = (app_font, 12))
        self.label_version.place(x = 84, y = 253)

        self.canvas_2 = tk.Canvas(self)
        self.canvas_2.create_line(5, 2, 380, 2)
        self.canvas_2.place(x = 5, y = 300)

        self.label_about_app = tk.Label(self, text = "Developer Information", font = (app_font, 12, "bold italic"), fg = "blue")
        self.label_about_app.place(x = 10, y = 310)

        self.canvas_3 = tk.Canvas(self)
        self.canvas_3.create_line(5, 2, 380, 2)
        self.canvas_3.place(x = 5, y = 340)

        self.label_name1 = tk.Label(self, text = "1. DUONG HUYNH NHAN (Kevin. H. N. DUONG)", font = (app_font, 12))
        self.label_name1.place(x = 20, y = 350)

        self.label_email1 = tk.Label(self, text = "nhanb1910676@student.ctu.edu.vn", font = (app_font, 12, "italic"))
        self.label_email1.place(x = 60, y = 370)

        self.label_name2 = tk.Label(self, text = "2. HUYNH HUU BAO KHOA (Bork B. K. H. HUYNH)", font = (app_font, 12))
        self.label_name2.place(x = 20, y = 400)

        self.label_email2 = tk.Label(self, text = "khoab1910658@student.ctu.edu.vn", font = (app_font, 12, "italic"))
        self.label_email2.place(x = 60, y = 420)

        self.canvas_4 = tk.Canvas(self)
        self.canvas_4.create_line(5, 2, 380, 2)
        self.canvas_4.place(x = 5, y = 450)