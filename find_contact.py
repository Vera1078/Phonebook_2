import user_interface
import output

def find():
    print('По какому параметру ищем контакт: \n\
            1 - Фамилия;\n\
            2 - Имя;\n\
            3 - Отчество;\n\
            4 - Статус;\n\
            5 - Номер телефона.\n')
    a = int(input('Введите номер поиска: '))
    if a == 1:
        contact = input('Введите фамилию: ').title()
    if a == 2:
        contact = input('Введите имя: ').title()
    if a == 3:
        contact = input('Введите отчество: ').title()
    if a == 4:
        contact = input('Введите статус (учащийся/родитель): ')   
    if a == 5:
        contact = input('Введите номер телефона: ')

    print('Будем искать по: ', contact)
    return contact
