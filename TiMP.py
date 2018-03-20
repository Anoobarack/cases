def CardCheck(f, cardId):   # Проверка на наличие пользователя в базе
    uData = 0
    for line in f:
        if line.split(' ')[0] == cardId:
            uData = line.strip().split(' ')
    return uData    # Возвращает копию информации о пользователе. Если его нет, возвращает 0

def PinCheck(attempt, truePin):    # Проверка соответствия pin и номера карты
    if attempt and attempt < 4:
        if attempt > 1:
            print('Неверный pin-код. Повторите попытку')
        pin = input('Введите pin-код: ')
        if pin == truePin:
            return True
        else:
            return PinCheck(attempt+1, truePin)     # Функция выполняется, пока не будет введён правильный pin, или попытки истекут
    else:
        return 0

def Operations(uData):    # Исполнение команд пользователя после успешной авторизации
    print('Приветствуем вас в нашем банке!')
    print('Ваши возможные операции:')
    print('1) Проверка вашего счёта')
    print('2) Списание со счёта определённой суммы')
    print('3) Отмена операции')
    choice = 0
    while(choice == 0):    # Пока не отменит операцию или не снимет деньги
        choice = int(input('Выберите операцию нажатием кнопки 1, 2 или 3: '))
        if choice > 3:
            print('Вы нажали на неверную кнопку. Повторите попытку')
            choice = 0
        else:
            if choice == 1:
                print('На вашем счёте %s денег' % uData[2])
                choice = 0
            elif choice == 2:
                amount = int(input('Введите сумму списывания: '))
                if amount > int(uData[2]):
                    print('На вашем счёте недостаточно денег')
                    choice = 0
                else:
                    uData[2] = str(int(uData[2]) - amount)
                    print('Заберите деньги')
            else:
                print('Удачного вам дня')
    return uData    # Возвращает обновлённые данные о пользователе

def CardBlock(uData):
    print('Лимит ваших попыток исчерпан. Ваша карта будет заблокирована')
    print('Чтобы избежать блокировки карты, введите уникальный код')
    print('Также на ваш номер телефона был выслан аналогичный код')
    print('Вы можете связаться с оператором службы безопасности по телефону')
    print('8-800-555-35-35')
    if uData[4] != input('Введите код: '):
        print('Карта была заблокирована')
        uData = ['']
    else:
        print('Карта не была заблокирована. Подождите перед следующей попыткой')
    return uData

def Authorised(uData):    # Возвращает результаты работы пользователя
    attempt = 1
    if PinCheck(attempt, uData[1]):     # Если прошёл сверку pin
        newData = Operations(uData)
    else:       # Если не прошёл сверку pin
        newData = CardBlock(uData)
    print('Заберите карту')
    return newData

def main():
    filename = ('doc.txt')
    with open(filename) as f1:
        text = f1.read()    # В text хранится строковая копия базы данных
    text = text.split('\n')     # В text записывается список строк
    text_list = []
    for i in text:
        a = i.strip().split(' ')
        text_list.append(a)     # В text_list записывается список списков, элементы которых - элементы БД
    f2 = open(filename)
    cardId = input('Вставьте карту: ')
    cardId = cardId.replace(' ', '')
    uData = CardCheck(f2, cardId)
    f2.close()
    if uData != 0:
        f3 = open(filename, 'w')
        newData = Authorised(uData)     # В newData записываются обновлённые данные о пользователе
        newText = ''
        if text_list[0][0] == uData[0]:     # Восстановление базы данных
            for j in newData:
                newText += j+' '
        else:
            for j in text_list[0]:
                newText += j+' '
        text_list.pop(0)
        for i in text_list:
            newText += '\n'
            if i[0] == uData[0]:
                for j in newData:
                    newText += j+' '
            else:
                for j in i:
                    newText += j+' '
        f3.write(newText)     # Запись новой базы данных
        f3.close()
    else:
        print('Ваша карта не принадлежит нашему банку. Заберите карту')
    return 0

main()
