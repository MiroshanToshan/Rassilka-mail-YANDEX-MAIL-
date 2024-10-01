import os
from dotenv import load_dotenv
from send import send_mail
import json 
import argparse
load_dotenv()




parser = argparse.ArgumentParser(
        description='Приложение находится в бета-тестировании, описание программы недоступно, ожидайте следующих обновлений!)'
)

parser.add_argument('-m', help='В данном аргументе нужно указывать почты, на которые вы хотите сделать рассылку', default='None')
my_mail = parser.parse_args().m

parser.add_argument('-t', help='В данном аргументе нужно указать файл с текстом письма', default='None')
text_file_path = parser.parse_args().t


if my_mail == "None":
  print("Вы не указали аргумент ПОЧТА! Повторите попытку! (-m)")
  exit()

if text_file_path == "None":
  print("Вы не указали аргумент ФАЙЛ С ТЕКСТОМ! Повторите попытку! (-t)")
  exit()


with open("mails.json", "r", encoding="UTF-8") as mails_js:
  mails = mails_js.read()

with open(text_file_path, "r", encoding="UTF-8") as text_txt:
  text = text_txt.read()

mails = json.loads(mails)



my_name = input("Ваше Имя: ")
friend_name = input("Имя друга: ")
subject = input("Введите тему ")
password = os.getenv("PASSWORD")


text = text.replace("%website%", "https://boulderbugle.com/-133m2lwo")
text= text.replace("%friend_name%", friend_name)
text = text.replace("%my_name%", my_name)

for mail in mails:
    send_mail(my_mail, mail, subject, password , text)


