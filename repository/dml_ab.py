from models.ab_models import Addressbook


USERS = Addressbook.objects


def insert_addressbook(name, phone, birthday, emails, address):
    ab_ = Addressbook(
        name=name,
        phone=phone,
        birthday=birthday,
        email=emails,
        address=address
    )
    ab_.save()


def remove_all():
    for user in USERS:
        user.delete()


def remove_user(name):
    for user in USERS:
        if user.name == name:
            user.delete()


def add_email(name, email):
    for user in USERS:
        if user.name == name and user.email is not None:
            user.update(email=email)
        else:
            print('Email already exists')


def show_all():
    return USERS


def change_contact(name, old, new):
    for user in USERS:
        if user.name == name and user.phone == old:
            user.update(phone=new)


def show_phone(name):
    for user in USERS:
        if user.name == name:
            return user.phone


def del_phone(name):
    for user in USERS:
        if user.name == name:
            if user.phone is not None:
                user.phone = None


def add_birthday(name, birthday):
    for user in USERS:
        if user.name == name and user.birthday is None:
            user.update(birthday=birthday)


def find_user(name):
    for user in USERS:
        if user.name == name:
            return user.birthday


def del_email(name):
    for user in USERS:
        if user.name == name:
            user.update(email=None)


def add_address(name, address):
    for user in USERS:
        if user.name == name:
            user.update(address=address)


def find_something(som):
    som_st = ' '.join(som)
    for s in USERS:
        birthday = s.birthday.strftime("%Y-%m-%d")
        if som_st in s.name or som_st in s.phone or som_st in birthday or som_st in s.email or som_st in s.address:
            print(f'User {s.name}, phone: {s.phone}, birthday: {s.birthday}, email: {s.email}, address: {s.address}')
