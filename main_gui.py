import os
from dotenv import load_dotenv
from send import send_mail
import json 
import argparse
load_dotenv()








from tkinter import *
from tkinter import ttk
okno = Tk()


def start():
  with open(emails_file_field.get(), "r", encoding="UTF-8") as mails_js:
    mails = mails_js.read()

  with open(text_file_field.get(), "r", encoding="UTF-8") as text_txt:
    text = text_txt.read()

  mails = json.loads(mails)

  text = text.replace("%website%", "https://boulderbugle.com/-133m2lwo")
  text= text.replace("%friend_name%", friend_name.get())
  text = text.replace("%my_name%", my_name.get())
  
  for mail in mails:
      send_mail(email_field.get(), mail, subject_field.get(),  password_field.get(), text)



okno.title("Рассылка почт")
okno.geometry("720x480")



email_field = ttk.Entry()
email_field.insert(0, "")
email_field.place(x=250, y=60)

test = ttk.Label(text = "Введите вашу почту")
test.place(x=50, y=300)



password_field = ttk.Entry()
password_field.insert(0, "") 
password_field.place(x=250, y=10)

test = ttk.Label(text = "Введите ваш пароль")
test.place(x=50, y=300)



emails_file_field = ttk.Entry()
emails_file_field.insert(0, "") 
emails_file_field.place(x=250, y=200)

test = ttk.Label(text = "Введите путь до файла с почтами")
test.place(x=50, y=300)



subject_field = ttk.Entry()
subject_field.insert(0, "") 
subject_field.place(x=250, y=30)

test = ttk.Label(text = "Введите тему письма")
test.place(x=50, y=300)




text_file_field = ttk.Entry()
text_file_field.insert(0, "") 
text_file_field.place(x=250, y=150)

test = ttk.Label(text = "Введите путь до файла с текстом")
test.place(x=50, y=300)




friend_name = ttk.Entry()
friend_name.insert(0, "") 
friend_name.place(x=250, y=130)

test = ttk.Label(text = "Введите путь до файла с почтами")
test.place(x=50, y=300)




my_name = ttk.Entry()
my_name.insert(0, "") 
my_name.place(x=250, y=100)

test = ttk.Label(text = "Введите аргумент свое имя")
test.place(x=50, y=300)






button1 = ttk.Button(text="Начать рассылку" , command=start)
button1.place(x=250, y=300)


# test = ttk.Label(text = "rujtghyuiwrjghujwr")
# test.place(x=320, y=300)







okno.mainloop()