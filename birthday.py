from field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value):
        try:
            value = datetime.strptime(value, "%d.%m.%Y").date()
            if value > datetime.now().date():
                raise ValueError("Birthday cannot be in the future.")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value.strftime("%d.%m.%Y"))
