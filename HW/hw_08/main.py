def read_txt(filename): 
    """Функция для чтения данных из файла"""
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = line.strip().split(',')
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    """Функция для записи данных в файл"""
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            values = ','.join(record)
            phout.write(f"{values}\n")


def work_with_phonebook():
    """Функция для работы с телефонным справочником"""
    choice = show_menu()
    phone_book = read_txt('HW/hw_08/phonebook.txt')
    
    while choice != 8:  # Выход из программы при выборе пункта 8
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            add_user(phone_book)
        elif choice == 5:
            write_txt('HW/hw_08/phonebook.txt', phone_book)
        elif choice == 6:
            delete_user(phone_book)
        elif choice == 7:
            change_number(phone_book)
            
        choice = show_menu()


def show_menu():
    """Функция для отображения меню"""
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента из справочника\n"
          "7. Изменить номер абонента\n"
          "8. Закончить работу")
    choice = int(input("Ваш выбор: "))
    return choice


def print_result(phone_book):
    """Функция для отображения данных о абонентах"""
    for record in phone_book:
        print('Фамилия:', record[0])
        print('Имя:', record[1])
        print('Телефон:', record[2])
        print('Описание:', record[3])
        print()


def find_by_lastname(phone_book, last_name):
    """Функция для поиска абонента по фамилии"""
    results = [record for record in phone_book if record[0] == last_name]
    if results:
        return results
    else:
        return "Абонент с такой фамилией не найден"


def find_by_number(phone_book, number):
    """Функция для поиска абонента по номеру телефона"""
    results = [record for record in phone_book if record[2] == number]
    if results:
        return results
    else:
        return "Абонент с таким номером телефона не найден"


def add_user(phone_book):
    """Функция для добавления абонента в справочник"""
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    description = input("Введите описание: ")
    
    new_record = [last_name, first_name, phone, description]
    phone_book.append(new_record)


def delete_user(phone_book):
    """Функция для удаления абонента из справочника"""
    last_name = input("Введите фамилию абонента, которого хотите удалить: ")
    for record in phone_book:
        if record[0] == last_name:
            phone_book.remove(record)
            print(f"Абонент {last_name} удален из справочника.")
            return
    print(f"Абонент {last_name} не найден в справочнике.")


def change_number(phone_book):
    """Функция для изменения номера абонента"""
    last_name = input("Введите фамилию абонента, у которого нужно изменить номер: ")
    for record in phone_book:
        if record[0] == last_name:
            new_number = input("Введите новый номер телефона: ")
            record[2] = new_number
            print(f"Номер телефона абонента {last_name} успешно изменен на {new_number}.")
            return
    print(f"Абонент {last_name} не найден в справочнике.")

work_with_phonebook()
