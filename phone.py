from field import Field


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() and not len(value) == 10:
            raise ValueError(f"Invalid of number, must contain 10 digits")
        super().__init__(value)
