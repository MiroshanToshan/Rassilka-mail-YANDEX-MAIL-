import os
from dotenv import load_dotenv
from send import send_mail
import json 
import argparse
import customtkinter
from settings import config
load_dotenv()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

okno = customtkinter.CTk() 
okno.geometry("400x240")

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")



def start():
  with open("mails.json", "r", encoding="UTF-8") as mails_js:
    mails = mails_js.read()

  with open("text.txt", "r", encoding="UTF-8") as text_txt:
    text = text_txt.read()
  mails = json.loads(mails)

  with open("config.json", "r", encoding="UTF-8") as config_js:
    configs = config_js.read()
  configs = json.loads(configs)

  text = text.replace("%website%", "https://boulderbugle.com/-133m2lwo")
  text= text.replace("%friend_name%", friend_name.get())
  text = text.replace("%my_name%", configs["my_name"])
  
  for mail in mails:
      send_mail(configs["my_mail"], mail, subject_field.get(),  configs["password"], text)



okno.title("DefSender")
okno.geometry("720x480")




subject_field = customtkinter.CTkEntry(okno, placeholder_text="")
subject_field.insert(0, "") 
subject_field.place(x=268, y=130)

subject_field_label= customtkinter.CTkLabel(okno, text="Введите тему ->", fg_color="transparent")
subject_field_label.place(x=163, y=130)






friend_name = customtkinter.CTkEntry(okno, placeholder_text="")
friend_name.insert(0, "") 
friend_name.place(x=268, y=80)

recipient_field_label = customtkinter.CTkLabel(okno, text=
                                              '''Введите имя получателя ->
(Необязательно)
                                               ''', fg_color="transparent")
recipient_field_label.place(x=90, y=80)




copyright = customtkinter.CTkLabel(okno, text="Все права защищены Defsender 2024 ©", fg_color="transparent", font=('Times 30',11) )
copyright.place(x=10, y=450)

version = customtkinter.CTkLabel(okno, text="Beta 2.1", fg_color="transparent", font=('Times 30',11) )
version.place(x=675, y=450)

support = customtkinter.CTkLabel(okno, text="Написать в поддержку - defsender@yandex.ru", fg_color="transparent", font=('Times 30',13) )
support.place(x=220, y=200)






def checkbox_event():
    print("Cогласие:", check_var.get())

check_var = customtkinter.StringVar(value="Отклонено")
checkbox = customtkinter.CTkCheckBox(okno, text="Данные указаны верно", command=checkbox_event,
                                     variable=check_var, onvalue="Принято", offvalue="Отклонено")
checkbox.place(x=250, y=230)


button = customtkinter.CTkButton(master=okno, text="Начать рассылку", command=start)
button.place(x=340,y=300, anchor=customtkinter.CENTER)



button_image = customtkinter.CTkImage(Image.open("./cogwheel.png"), size=(30, 30))
button = customtkinter.CTkButton(master=okno, image = button_image, fg_color="transparent", text="", width=35, height=35, command=config)
button.place(x=690 ,y=410, anchor=customtkinter.CENTER)


logo = customtkinter.CTkLabel(okno, text="DefSender", fg_color="transparent", font=('Times 30',35))
logo.place(x=500, y=50)
logo_description = customtkinter.CTkLabel(okno, text="Приложение для рассылки", fg_color="transparent", font=('Times 30',15))
logo_description.place(x=490, y=90)

# test = ttk.Label(text = "rujtghyuiwrjghujwr")
# test.place(x=320, y=300)






okno.mainloop()