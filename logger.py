import output
import user_interface
import add_contact
import output


def log_to_file(contact):

    with open('spisok1.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{contact[0]}; {contact[1]}; {contact[2]}; {contact[3]}; {contact[4]}\n')

    with open('spisok2.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{contact[0]} {contact[1]} {contact[2]}; {contact[3]}; {contact[4]}\n\n')


def reading_file(param):
    b = output.view()
    if b == 2:
        with open('spisok2.txt', 'r', encoding='UTF-8') as file:
            filecontents= file.read().splitlines()
            for line in filecontents:
                if param in line:
                    print (line)
          

    elif b == 1:
        list = []
        with open('spisok1.csv', 'r', encoding='UTF-8') as file:  
            filecontents = file.readlines()  
            for line in filecontents:
                if param in line:
                    list = line.split(';')
                    print(f'{list[0]};{list[1]};{list[2]};{list[3]};{list[4]}\n')



def reading_all():
    b = output.view()
    if b == 1:
        with open('spisok1.csv', 'r', encoding='UTF-8') as file:
            for line in file:
                print(line)
    if b == 2:
        with open('spisok2.txt', 'r', encoding='UTF-8') as file:
            for line in file:
                print(line)
