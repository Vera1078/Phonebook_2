import logger
# Запись конакта в телефонную книгу

def add_contact():
    contact = []
    sirname = input('Введите фамилию: ')
    contact.append(sirname.title())

    name = input('Введите имя: ')
    contact.append(name.title())

    any_info = input('Введите отчество: ')
    contact.append(any_info.title())

    status_info = input ('Введите статус (учащийся/родитель): ')
    contact.append(status_info)

    phone_number = input('Введите номер телефона: ')
    contact.append(phone_number)

    
    
    print('Абонент записан: ', contact)
    return contact
