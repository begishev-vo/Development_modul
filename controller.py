# import model
# import view
#
#
# def start():
#     while True:
#         pb = model.get_phone_book()
#         choice = view.main_menu()
#         match choice:
#             case 1:
#                 model.open_file()
#                 view.show_message('Файл успешно открыт')
#             case 2:
#                 model.save_file()
#                 view.show_message('Файл успешно сохранен')
#             case 3:
#                 view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
#             case 4:
#                 contact = view.add_contact()
#                 model.add_contact(contact)
#             case 5:
#                 if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
#                     index = view.input_index('Введите номер изменяемого контакта')
#                     contact = view.change_contact(pb, index)
#                     model.change_contact(contact, index)
#                     view.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен!')
#             case 6:
#                 search = view.input_search('Введите искомый элемент: ')
#                 result = model.find_contact(search)
#                 view.show_contacts(result, 'Конаткты не найдены')
#             case 7:
#                 return
#
#

import phone_book
from phone_book import PhoneBook

pb = phone_book.PhoneBook('phone.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите номер телефона: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input('Введите индекс изменяемого контакта: '))
            name = input('Введите имя (или Enter, чтобы пропустить): ')
            phone = input('Введите номер телефона (или Enter, чтобы пропустить): ')
            comment = input('Введите комментарий (или Enter, чтобы пропустить): ')
            pb.change(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input('Введите индекс контакта, котороый хотите удалиить: '))
            pb.delete(index-1)
        case 6:
            pb.save()
        case 7:
            break


