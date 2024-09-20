import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


moename = input("Ваше Имя: ")
imyadruga = input("Имя друга: ")
my_mail = input("Ваша почта: ")
friend_mail = input("Почта друга:  ")
tema = input("Введите тему ")

password = os.getenv("PASSWORD")

zagolovok = f'''From: {my_mail}
To: {friend_mail}
Subject: {tema}
Content-Type: text/plain; charset="UTF-8"'''

text =  '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

> Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
> Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
> Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся > %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''
text = text.replace("%website%", "https://boulderbugle.com/-133m2lwo")
text= text.replace("%friend_name%", imyadruga)
text = text.replace("%my_name%", moename)

vse = f'''{zagolovok}

{text}'''

vse = vse.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(my_mail,password)
server.sendmail(my_mail,friend_mail ,vse)
server.quit()
