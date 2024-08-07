from datetime import datetime, timedelta, date
from collections import UserDict
from prettytable import PrettyTable
import pickle


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, name):
        return self.data.get(name)

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            return "Record not found"

    def __str__(self):
        table = PrettyTable()
        table.field_names = ["Name", "Phones", "Birthday"]
        for obj in self.data.values():
            phone = '; '.join(p.value for p in obj.phones)
            table.add_row([obj.name.value, phone, obj.birthday.value if obj.birthday else 'N/A'])
        return table.get_string()

    @staticmethod
    def string_to_date(date_string):
        return datetime.strptime(date_string, "%d.%m.%Y").date()

    @staticmethod
    def date_to_string(date_str):
        return date_str.strftime("%d.%m.%Y")

    @staticmethod
    def find_next_weekday(start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5:
            return self.find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self, days=7):
        table = PrettyTable()
        table.field_names = ["Name", "Birthday people"]
        today = date.today()
        for record in self.data.values():
            birthday_this_year = self.string_to_date(record.birthday.value).replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            if 0 <= (birthday_this_year - today).days <= days:
                congratulation_date = self.adjust_for_weekend(birthday_this_year)
                congratulation_date_str = self.date_to_string(congratulation_date)
                table.add_row([record.name.value, congratulation_date_str])
        return table.get_string()


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
