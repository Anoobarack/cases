# Дарья:
def card_block(user_inf):       # блокировка карты после трёх неудачных попыток
    print('Лимит ваших попыток исчерпан. Ваша карта будет заблокирована')
    print('Чтобы избежать блокировки карты, введите уникальный код')
    print('Также на ваш номер телефона был выслан аналогичный код')
    print('Вы можете связаться с оператором службы безопасности по телефону')
    print('8-800-555-35-35')
    if user_inf[4] != input('Введите код: '):   # если ввод не совпадает с кодом
        print('Карта была заблокирована')
        new_info = ['']     # обнуление информации о карте
        return new_info
    else:   # если ввод совпадает с кодом
        print('Карта не была заблокирована. Подождите перед следующей попыткой')
        new_info = user_inf     # ничего не меняется
        return new_info

# Илья:
def main():
    f = open('doc.txt', 'r', encoding = 'utf8')
    cardId = input('Вставьте карту: ')
    cardId = cardId.replace(' ', '')
    uData = CardCheck(f, cardId)
    f.close()
    text = [].append([line.strip().split(' ') for line in f])
    # text - это список, элементами которого являются списки
    # в этих списках хранятся элементы базы данных о каждом пользователе
    f = open('doc.txt', 'w', encoding = 'utf8')
    if uData != ['']:
        newData = Authorised(uData)
        for i in text:  # замена старых данных новыми
            if i[0] == uData[0]:
                i = newData
        newText = ''
        for i in text:   # запись
            for j in i:
                newText = newText + j + ' '
            newText = newText + '\n'
        f.write(newText)
    else:
        print('Ваша карта не принадлежит нашему банку. Заберите карту')
    f.close()
    return 0

# Мария:
def Operations(userData):
    print('Приветствуем вас в нашем банке!')
    print('Ваши возможные операции:')
    print('1) Проверка вашего счёта')
    print('2) Списание со счёта определённой суммы')
    print('3) Отмена операции')
    choice = 0
    while(choice == 0):
        choice = int(input('Выберите операцию нажатием кнопки 1, 2 или 3:'))
        if choice > 3:
            print('Вы нажали на неверную кнопку. Повторите попытку')
            choice = 0
        else:
            if choice == 1:
                print('На вашем счёте %s денег' % userData[2])
                choice = 0
            elif choice == 2:
                amount = int(input('Введите сумму списывания: '))
                if amount > userData[2]:
                    print('На вашем счёте недостаточно денег')
                    choice = 0
                else:
                    userData[2] = str(int(userData[2]) - amount)
                    print('Заберите деньги')
            else:
                print('Удачного вам дня')
    return userData

# Полина:
def Card_Check(file, cardId):
    userData = 0
    for line in file:
        if line.split(' ')[0] == cardId:
            userData = line.strip().split(' ')
    return userData     # Возвращает копию информации о пользователе

def Authorised(userData):
    attempt = 1
    if PinCheck(attempt, userData[1]):
        newData = Operations(userData)
    else:
        newData = CardBlock(userData)
    print('Заберите карту')
    return newData      # Возвращает обновлённые данные о пользователе
