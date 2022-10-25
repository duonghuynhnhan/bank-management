import tkinter as tk
from tkinter import messagebox
from tkinter.constants import LEFT
from PIL import Image, ImageTk

app_font = "Arial"

class User_Edit_Personal_Information(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width = 400, height = 600)
        self.username = "" 

        self.img_home = ImageTk.PhotoImage(Image.open("pictures/app/back.png").resize((40, 40), Image.ANTIALIAS))
        self.button_back = tk.Button(self, image = self.img_home, border = "0", command = self.back)
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
        self.text_email = tk.StringVar()
        self.text_email.set("duonghuynhnhan@outlook.com")
        self.entry_email = tk.Entry(self, textvariable = self.text_email, font = (app_font, 12), width = 33)
        self.entry_email.place(x = 75, y = 270)

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
        self.textbox_address = tk.Text(self, exportselection = 1, font = (app_font, 12), width = 32, height = 3)
        self.textbox_address.insert("1.0", "NGA BAY, HAU GIANG")
        self.textbox_address.place(x = 90, y = 390)

        self.canvas_4 = tk.Canvas(self)
        self.canvas_4.create_line(9, 2, 380, 2)
        self.canvas_4.place(x = 5, y = 455)

        self.button_done = tk.Button(self, text = "Done", fg = "blue", border = "0", font = (app_font, 12, "bold"), command = self.edit)
        self.button_done.place(x = 180, y = 480)

    def update(self):
        code = """SELECT *
                FROM USER AS U JOIN USER_ACCOUNT AS UA ON UA.USER = U.U_ID
                WHERE UA.ACC_NUM = '%s'"""%(self.username)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()

        self.text_email.set(data[0][6])
        self.entry_email.config(textvariable = self.text_email)

        self.textbox_address.delete("1.0", "end-1c")
        self.text_address = data[0][4]
        self.textbox_address.insert("1.0", self.text_address.upper())

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

        self.text_phone = data[0][5]
        self.label_phone.config(text = self.text_phone)
        self.label_phone.place(x = 371-(len(self.text_phone)*8.6), y = 360)

    def back(self):
        code = """SELECT *
                FROM USER AS U JOIN USER_ACCOUNT AS UA ON UA.USER = U.U_ID
                WHERE UA.ACC_NUM = '%s'"""%(self.username)
        self.controller.cursor.execute(code)
        data = self.controller.cursor.fetchall()

        self.text_email.set(data[0][6])
        self.entry_email.config(textvariable = self.text_email)
        self.textbox_address.delete("1.0", "end-1c")
        self.textbox_address.insert("1.0", self.text_address.upper())
        self.controller.show_frame("User_Personal_Information")

    def edit(self):
        email = self.entry_email.get()
        address = self.textbox_address.get("1.0", "end-1c")
        if email and address:
            if len(email) <= 100 and len(address) <= 100:
                if "@" in email and " " not in email:
                    code = """CALL CHANGE_USER_PERSONAL('%s', '%s', '%s')"""%(self.username, email, address.upper())
                    self.controller.cursor.execute(code)
                    done = messagebox.showinfo(title = "Chang personal information", message = "You have change personal information successfully!")
                    if done:
                        self.controller.update("User_Personal_Information")
                        self.controller.update("User_Edit_Personal_Information")
                        self.controller.show_frame("User_Personal_Information")
                else:
                    messagebox.showerror(title = "Change personal information", message = "Email invalid!")
            else:
                messagebox.showerror(title = "Change personal information", message = "Email or address too long!")
        else:
            messagebox.showerror(title = "Change personal information", message = "You must input all information!")