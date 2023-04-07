import model
import view


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                pass
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                contact = view.add_contact()
                model.add_contact(contact)
            case 5:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
                index = view.input_index('Введите номер измяемго контакта')
                contact = view.change_contact(pb, index)
                model.change_contact(contact, index)
            case _:
                pass


