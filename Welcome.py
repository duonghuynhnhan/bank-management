import tkinter as tk

app_font = "Arial"

class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        
        self.label_intro = tk.Label(self, text = "WELCOME TO CNTT CLC F3 BANK", font = (app_font, 12, "bold"), fg = "pale Violet red")
        self.label_intro.place(x = 0, y = 5)
        
        self.label_login = tk.Label(self, text = "LOG IN AS?", font = (app_font, 30, "bold"), fg = "chocolate1")
        self.label_login.pack(pady = 55)

        self.button_user = tk.Button(self, text = "USER", font = (app_font, 35, "bold"), fg = "dark olive green", height = 1, width = 6, bd = 5, command = lambda: controller.show_frame("User_Login"))
        self.button_user.pack(pady = 30)

        self.button_admin = tk.Button(self, text = "ADMIN", font = (app_font, 35, "bold"), fg = "Magenta4", height = 1, width = 6, bd = 5, command = lambda: controller.show_frame("Admin_Login"))
        self.button_admin.pack(pady = 10)

        self.dx = 0
        self.intro()

    def intro(self):
        if self.dx > 400:
            self.dx = 0
        self.label_intro.place(x = self.dx, y = 5)
        self.dx += 20
        self.after(200, self.intro)