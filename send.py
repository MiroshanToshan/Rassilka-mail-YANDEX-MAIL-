
import smtplib


def send_mail(my_mail, friend_mail, subject, password, text):
    headers = f'''From: {my_mail}
    To: {friend_mail}
    Subject: {subject}
    Content-Type: text/plain; charset="UTF-8"'''

    final_letter = f'''{headers}

    {text}'''

    final_letter = final_letter.encode("UTF-8")

    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(my_mail,password)
    server.sendmail(my_mail,friend_mail ,final_letter)
    server.quit()
