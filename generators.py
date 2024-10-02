from faker import Faker

fake = Faker()


def generated_name():
    generated_name = fake.user_name()
    return generated_name


def generated_password():
    generated_password = fake.password(7)
    return generated_password


def generated_email():
    generated_email = fake.email('@', 'yandex.ru')
    return generated_email
