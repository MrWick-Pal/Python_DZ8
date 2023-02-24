import os
import csv

def read_data():
    with open('phonebook.csv', 'r') as file:
        my_list = file.readlines()
        return my_list

# Добавление пользователя.
def add_user(my_list):
    
    user_info = []
    uniq_id = str(len(my_list) + 1)
    user_info.append(uniq_id)
        
    first_name = input('Введите имя: ')
    user_info.append(first_name)

    second_name = input('Введите фамилию: ')
    user_info.append(second_name)

    tel_number = input('Введите номер телефона: ')
    user_info.append(tel_number)

    email = input('Введите email: ')
    user_info.append(email)

    my_list.append(user_info)

    return my_list

# Сохранения изменений.
def save_data(my_list):
    for user in my_list:
        with open('phonebook.csv', 'a', newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(user)
    return my_list

# Вывод содержимого.
def print_data(my_list):
    for i in my_list:
        try:
            print(i.replace(';', ' | '))
        except:
            print(i)

# Удаление данных.
def delete_data(my_list):
    print('Удаление данных.')
    user_command = input('Введите Y/N: ')
    if user_command == 'Y' or user_command == 'y':
        my_list.clear()
        print('Данные удалены.\n')
        return my_list
    else:
        return my_list

# Поиск контакта.
def user_search(my_list):
    print("Найти контакт")
    find_input = str(input("Введите данные пользователя: \n"))
    for user in my_list:
        flag = 0
        for data in user:
            if find_input in data:
                if flag == 0:
                    print(user)
                flag += 1
                if flag == 1:
                    continue

# Меню.
def menu(my_list):
    print('Меню справочника.\n')
    print('1 - чтобы просмотреть справочник.')
    print('2 - чтобы добавть пользователя.')
    print('3 - чтобы сохранить изменения.')
    print('4 - чтобы удалить данные.')
    print('5 - чтобы найти контакт.')
    print('6 - чтобы закрыть программу.\n')
    
    flag = True
    while flag:
        try:
            command = int(input('Введите число: '))
        except:
            print('Введите число!')
        if command == 1:
            print_data(my_list)
            return menu(my_list)
        
        elif command == 2:
            my_list = add_user(my_list)
            return menu(my_list)
        
        elif command == 3:
            my_list = save_data(my_list)
            return menu(my_list)

        elif command == 4:
            my_list = delete_data(my_list)
            return menu(my_list)
        
        elif command == 5:
            my_list = user_search(my_list)
            return menu(my_list)

        elif command == 6:
            print('Завершение программы...')
            flag = False
my_list = []
def main():
    my_list = read_data()
    menu(my_list)
main()