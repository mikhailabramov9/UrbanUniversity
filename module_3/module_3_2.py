def send_email(message, recipient, sender = "university.help@gmail.com"):
    my_list = [".com", ".ru", ",net"]
    correct_recipient = False
    correct_sender = False
    for i in my_list:
        if i in recipient and "@" in recipient:
            correct_recipient = True
        if i in sender and "@" in sender:
            correct_sender = True
    if correct_recipient == True and correct_sender == True:
        if sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)
        elif sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, "на адрес ", recipient)
    else:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')