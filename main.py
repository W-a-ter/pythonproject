from src.utils import my_file, my_file_csv, my_file_xlsx
from src.get_info import get_info
from src.processing import sort_by_date
from src.generators import filter_by_currency
from src.widget import get_data, mask_account_card

def main():
    print('Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    user_input= input('''Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
    if user_input == '1':
        print('Программа: Для обработки выбран JSON-файл.')
        result = my_file('../Data/operations.json')
    elif user_input == '2':
        print('Программа: Для обработки выбран CSV-файл.')
        result = my_file_csv('../Data/transactions.csv')
    else:
        print('Программа: Для обработки выбран xlsx-файл.')
        result = my_file_xlsx('../Data/transactions_excel.xlsx')

    user_input_ = input('''Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''').lower()
    while user_input_ not in ['executed', 'canceled', 'pending']:
        print(f'Статус операции {user_input_} недоступен.')
        print(user_input_)
    else:
        if user_input_ == 'executed':
            print('Операции отфильтрованы по статусу "EXECUTED"')
            result = get_info(result, user_input_.upper())
        elif user_input_ == 'canceled':
            print('Операции отфильтрованы по статусу "canceled"')
            result = get_info(result, user_input_.upper())
        elif user_input_ == 'pending':
            print('Операции отфильтрованы по статусу "PENDING"')
            result = get_info(result, user_input_.upper())

    print('Отсортировать операции по дате? Да/Нет')
    user_input = input().lower()
    if user_input == 'да':
        user_input_1 = input("Отсортировать по возрастанию или по убыванию?").lower()
        if user_input_1 == 'по возрастанию':
            result = sort_by_date(result)
        else:
            result = sort_by_date(result, False)

    print('Выводить только рублевые тразакции? Да/Нет')
    user_input = input().lower()
    if user_input == 'да':
        result = filter_by_currency(result, 'RUB')

    print('''Программа: Отфильтровать список транзакций по определенному слову 
            в описании? Да/Нет''')
    user_input = input().lower()
    if user_input == 'да':
        enter = input().title()
        result = get_info(result, enter)

    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке:{len(result)}')
    if result is []:
        print('''Не найдено ни одной транзакции, подходящей под ваши
                условия фильтрации''')
    else:
        for i in result:
            date = get_data(i['date'])
            description = i['description']
            account_from = mask_account_card(i.get('from', ''))
            account_to = mask_account_card(i.get('to', ''))
            amount = i['operationAmount']['amount']
            name = i['operationAmount']['currency']['code']
            print(f'{date}, {description},\n {account_from}, {account_to}, \n {amount}, {name} ')

    return 'finish'