import os
from dotenv import load_dotenv
from send import send_mail
load_dotenv()


my_name = input("Ваше Имя: ")
friend_name = input("Имя друга: ")
my_mail = input("Ваша почта: ")
friend_mail = input("Почта друга:  ")
subject = input("Введите тему ")

password = os.getenv("PASSWORD")

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
text= text.replace("%friend_name%", friend_name)
text = text.replace("%my_name%", my_name)


send_mail(my_mail=my_mail, friend_mail=friend_mail, subject=subject, password=password, text=text)
send_mail(my_mail, friend_mail, subject, password , text)