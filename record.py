from name import Name
from birthday import Birthday
from phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday_in_class(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def delete_phone(self, number):
        for num in self.phones:
            if num.value == number:
                self.phones.remove(num)
                break

    def edit_phone(self, old_number, new_number):
        if self.find_phone(old_number):
            self.delete_phone(old_number)
            self.add_phone(new_number)

    def find_phone(self, number):
        for num in self.phones:
            if num.value == number:
                return num.value
        return None

    def show_phones(self):
        return '; '.join(p.value for p in self.phones)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
