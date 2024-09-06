def send_email(message, recepient, *, sendler="university.help@gmail.com"):

    if recepient.find('@') == -1 or recepient.endswith(('.com', '.ru', 'net')) == False:
        return print('Невозможно отправить письмо адресату ', recepient)

    elif sendler.find('@') == -1 or  sendler.endswith(('.com', '.ru', 'net')) == False:
        return print('Невозможно отправить письмо с адреса ', sendler)

    elif recepient == sendler:
        return print("Нельзя отправить письмо самому себе!")

    elif sendler.find("university.help@gmail.com") != -1 :
        return print("Письмо успешно отправлено с адреса ", sendler, " на адрес ", recepient)

    else:
        return print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sendler,
                     " на адрес ", recepient)

send_email('Это сообщение для проверки связи ', 'vasyok1337@gmail.com')
send_email('Это сообщение для проверки связи ', 'university.help@gmail.com')
send_email('Вы видите это сообщение как лучщий студент курса ', 'urban.fan@mail.ru',
           sendler = 'urban.info@gmail.com')
send_email('Пожалуйста, исправте задание ', 'urban.student@mail.ru',
           sendler = 'urban.tracfer@mail.ru')
send_email('Напоминаю самому себе о вебинаре ', 'urban.teacher@mail.ru',
           sendler = 'urban.tracher@mail.ru')
send_email('Напоминаю самому себе о вебинаре ', 'urban.teachermail.ru',
           sendler = 'urban.tracher@mail.ru')
send_email('Напоминаю самому себе о вебинаре ', 'urban.teac@hermail.ru',
           sendler = 'urban.trachermail.ru')
send_email('Напоминаю самому себе о вебинаре ', 'urban.teac@hermail.su',
           sendler = 'urban.tracher@mail.ru')
send_email('Напоминаю самому себе о вебинаре ', 'urban.teac@hermail.ru',
           sendler = 'urban.tracher@mail.zux')
send_email('Напоминаю самому себе о вебинаре ', 'urban.teac@hermail.net',
           sendler = 'urban.tracher@mail.ru')
