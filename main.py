import getpass

database = {'ivan': '123456', 'petr':'654321'}
username = input('Введите имя(логин): ')
password = getpass.getpass('Введите пароль: ')
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass('Введите пароль: ')
        print('Верно')
        break
    else:
        print('Неверно')
        break