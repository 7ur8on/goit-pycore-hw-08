from addressbook import AddressBook, load_data, save_data
from record import Record
from decorator import input_error


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(book.get_upcoming_birthdays())

        elif command == "delete-record":
            print(del_record(args, book))

        else:
            print("Invalid command.")
    save_data(book)


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find_record(name)
    if phone.isdigit() and len(phone) != 10:
        return "The phone must have 10 digits"
    if record is None:
        record = Record(name)
        book.add_record(record)
        if phone.isdigit() and len(phone) == 10:
            record.add_phone(phone)
            return "Contact added."
    else:
        if phone.isdigit() and len(phone) == 10:
            record.add_phone(phone)
            return "Contact updated."


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find_record(name)
    record.edit_phone(old_phone, new_phone)
    return f"Contact {name} updated with number {new_phone}."


@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.find_record(name)
    return record.show_phones()


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find_record(name)
    if record is None:
        return f"Name {name} does not exist"
    if record.birthday is not None:
        return f"Name {name} with birthday {record.birthday} is exist"
    record.add_birthday_in_class(birthday)
    return f"Birthday for {name} added"


@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find_record(name)
    return record.birthday.value


@input_error
def del_record(args, book: AddressBook):
    name, *_ = args
    if book.find_record(name) is None:
        return f"Record with {name} not found."
    else:
        book.delete_record(name)
        return f"Record with name {name} is deleted"


if __name__ == "__main__":
    main()
