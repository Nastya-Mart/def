def send_email(message="Привет я Python", recipient="nastya.mart749@gmail.com", *, sender="university.help@gmail.com"):
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    if not (is_valid_email(recipient) and is_valid_email(sender)):
        print(f"Невозможно отправить письмо с адреса '{sender}' на адрес '{recipient}'")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса '{sender}' на адрес '{recipient}'.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса '{sender}' на адрес '{recipient}'.")
print(send_email)
send_email()