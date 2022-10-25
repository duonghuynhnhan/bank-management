import tkinter as tk
from tkinter.constants import LEFT
from PIL import Image, ImageTk

app_font = "Arial"

class User_Personal_Information(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = "" 

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/home.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = lambda: controller.show_frame("User_HomePage"))
        self.button_back.place(x = 0, y = 0)

        self.label_welcome = tk.Label(self, text = "PERSONAL INFORMATION", font = ("Arial", 20, "bold"), fg = "green")
        self.label_welcome.pack(pady = 60)

        self.label_identification_information = tk.Label(self, text = "Identification information", font = (app_font, 12, "bold italic"), fg = "blue")
        self.label_identification_information.place(x = 10, y = 120)

        self.canvas_1 = tk.Canvas(self)
        self.canvas_1.create_line(9, 2, 380, 2)
        self.canvas_1.place(x = 5, y = 150)

        self.label_fullname_title = tk.Label(self, text = "Full name:", font = ("Arial", 12))
        self.label_fullname_title.place(x = 20, y = 160)
        self.text_fullname = "DUONG HUYNH NHAN"
        self.label_fullname = tk.Label(self, text = self.text_fullname, font = (app_font, 12))
        self.label_fullname.place(x = 371-(len(self.text_fullname)*10.1), y = 160)

        self.label_id_title = tk.Label(self, text = "ID/Passport:", font = ("Arial", 12))
        self.label_id_title.place(x = 20, y = 190)
        self.text_id = "093201008346"
        self.label_id = tk.Label(self, text = self.text_id, font = (app_font, 12))
        self.label_id.place(x = 371-(len(self.text_id)*9), y = 190)

        self.canvas_2 = tk.Canvas(self)
        self.canvas_2.create_line(9, 2, 380, 2)
        self.canvas_2.place(x = 5, y = 220)

        self.label_additional_information = tk.Label(self, text = "Additional information", font = (app_font, 12, "bold italic"), fg = "blue")
        self.label_additional_information.place(x = 10, y = 230)

        self.canvas_3 = tk.Canvas(self)
        self.canvas_3.create_line(9, 2, 380, 2)
        self.canvas_3.place(x = 5, y = 262)

        self.label_email_title = tk.Label(self, text = "Email:", font = (app_font, 12))
        self.label_email_title.place(x = 20, y = 270)
        self.text_email = "duonghuynhnhan@outlook.com"
        self.label_email = tk.Label(self, text = self.text_email, font = (app_font, 12))
        self.label_email.place(x = 371-(len(self.text_email)*8.2), y = 270)

        self.label_sex_title = tk.Label(self, text = "Sex", font = (app_font, 12))
        self.label_sex_title.place(x = 20, y = 300)
        self.text_sex = "Male"
        self.label_sex = tk.Label(self, text = self.text_sex, font = (app_font, 12))
        self.label_sex.place(x = 371-(len(self.text_sex)*8.5), y = 300)

        self.label_dob_title = tk.Label(self, text = "Date of birth:", font = (app_font, 12))
        self.label_dob_title.place(x = 20, y = 330)
        self.text_dob = "ARP-26-2001"
        self.label_dob = tk.Label(self, text = self.text_dob, font = (app_font, 12))
        self.label_dob.place(x = 371-(len(self.text_dob)*8.5), y = 330)

        self.label_phone_title = tk.Label(self, text = "Phone number:", font = (app_font, 12))
        self.label_phone_title.place(x = 20, y = 360)
        self.text_phone = "0354984001"
        self.label_phone = tk.Label(self, text = self.text_phone, font = (app_font, 12))
        self.label_phone.place(x = 371-(len(self.text_phone)*8.6), y = 360)

        self.label_address_title = tk.Label(self, text = "Address:", font = (app_font, 12))
        self.label_address_title.place(x = 20, y = 390)
        self.text_address = "NGA BAY, HAU GIANG"
        self.label_address = tk.Label(self, text = self.text_address, font = (app_font, 12))
        self.label_address.place(x = 371-(len(self.text_address)*8.9), y = 390)

        self.canvas_4 = tk.Canvas(self)
        self.canvas_4.create_line(9, 2, 380, 2)
        self.canvas_4.place(x = 5, y = 420)

        self.img_edit = ImageTk.PhotoImage(Image.open("pictures/app/edit.png").resize((40, 40), Image.ANTIALIAS))
        self.button_edit = tk.Button(self, image = self.img_edit, fg = "gray50", border = "0", text = "Edit Personal Information", font = (app_font, 12, "bold"), compound = LEFT, command = self.edit)
        self.button_edit.place(x = 80, y = 460)

    def update(self):
        code = """SELECT *
                FROM USER AS U JOIN USER_ACCOUNT AS UA ON UA.USER = U.U_ID
                WHERE UA.ACC_NUM = '%s'"""%(self.username)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()

        self.text_id = data[0][0]
        self.label_id.config(text = self.text_id)
        self.label_id.place(x = 371-(len(self.text_id)*9), y = 190)

        self.text_fullname = data[0][1]
        self.label_fullname.config(text = self.text_fullname)
        self.label_fullname.place(x = 371-(len(self.text_fullname)*10.1), y = 160)

        self.text_dob = str(data[0][2].strftime("%b-%d-%Y")).upper()
        self.label_dob.config(text = self.text_dob)
        self.label_dob.place(x = 371-(len(self.text_dob)*8.5), y = 330)

        self.text_sex = data[0][3]
        self.label_sex.config(text = self.text_sex)
        self.label_sex.place(x = 371-(len(self.text_sex)*8.5), y = 300)

        self.text_address = data[0][4]
        self.label_address.config(text = self.text_address)
        self.label_address.place(x = 371-(len(self.text_address)*8.9), y = 390)

        self.text_phone = data[0][5]
        self.label_phone.config(text = self.text_phone)
        self.label_phone.place(x = 371-(len(self.text_phone)*8.6), y = 360)

        self.text_email = data[0][6]
        self.label_email.config(text = self.text_email)
        self.label_email.place(x = 371-(len(self.text_email)*8.2), y = 270)

    def edit(self):
        self.controller.show_frame("User_Edit_Personal_Information")