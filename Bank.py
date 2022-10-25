import tkinter as tk
from tkinter import messagebox
import mysql.connector
import random as rd

from Welcome import *
from User_Login import *
from User_Forgot_Password import *
from User_New_Password import *
from User_HomePage import *
from User_Personal_Information import *
from User_Edit_Personal_Information import * 
from User_Account_Information import *
from User_Change_Password import *
from User_Change_Answer import *
from User_Transaction import *
from User_Withdrawal import *
from User_Recharge import *
from User_Transfer import *
from User_About import *

from Admin_Login import *
from Admin_Forgot_Password import *
from Admin_New_Password import *
from Admin_HomePage import *
from Admin_Personal_Information import *
from Admin_Edit_Personal_Information import * 
from Admin_Account_Information import *
from Admin_Change_Password import *
from Admin_Change_Answer import *
from Admin_Transaction import *
from Admin_Show_All_Users import *
from Admin_Create_User import *
from Admin_Check_User import *
from Admin_About import *

class Bank(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.mysql = True
        self.title("CNTT CLC F3 Bank Application")
        self.geometry("400x600")
        self.resizable(False, False)
        self.iconbitmap("pictures/app/logo.ico")

        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        try:
            self.database = mysql.connector.connect(user = "root", password = "KevinDuong2001@", 
                                                    host = "127.0.0.1", database = "BANK")
            self.cursor = self.database.cursor()
        except:
            messagebox.showerror(title = "Error", message = "Can't connect with database")
            self.mysql = False

        if self.mysql: 
            self.frames = {}
            self.pages = (Welcome, 
            User_Login, User_Forgot_Password, User_New_Password, User_HomePage, 
            User_Personal_Information, User_Edit_Personal_Information, User_Account_Information, 
            User_Change_Password, User_Change_Answer, User_Withdrawal, User_Recharge, 
            User_Transfer, User_About, 
            Admin_Login, Admin_Forgot_Password, Admin_New_Password, Admin_HomePage, 
            Admin_Personal_Information, Admin_Edit_Personal_Information, Admin_Account_Information, 
            Admin_Change_Password, Admin_Change_Answer, Admin_Create_User, Admin_Check_User, Admin_About)
            for F in self.pages:
                page_name = F.__name__
                frame = F(parent = self.container, controller = self)
                self.frames[page_name] = frame
                frame.grid(row = 0, column = 0, sticky = "nsew")

            self.show_frame("Welcome")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def send_data(self, destination, data):
        if destination == "user":
            for F in (User_HomePage, User_Personal_Information, User_Edit_Personal_Information, 
                    User_Account_Information, User_Change_Password, User_Change_Answer, User_Transaction, 
                    User_Withdrawal, User_Recharge, User_Transfer):
                page_name = F.__name__
                if page_name == "User_Transaction":
                    f = F(parent = self.container, controller = self)
                    self.frames[page_name] = f
                    f.grid(row = 0, column = 0, sticky = "nsew")
                frame = self.frames[page_name]
                frame.username = data
                frame.update()
        elif destination == "admin":
            for F in (Admin_HomePage, Admin_Personal_Information, Admin_Edit_Personal_Information, 
                    Admin_Account_Information, Admin_Change_Password, Admin_Change_Answer, Admin_Transaction, 
                    Admin_Create_User, Admin_Show_All_Users):
                page_name = F.__name__
                if page_name == "Admin_Transaction" or page_name == "Admin_Show_All_Users":
                    f = F(parent = self.container, controller = self)
                    self.frames[page_name] = f
                    f.grid(row = 0, column = 0, sticky = "nsew")
                frame = self.frames[page_name]
                frame.adminname = data
                frame.update()
    
    def update(self, page_name):
        frame = self.frames[page_name]
        frame.update()

    def delete(self, page_name):
        frame = self.frames[page_name]
        del frame

    def rand(self, num):
        string = ""
        while len(string) < num:
            string += str(rd.randint(0, 9))
        return string