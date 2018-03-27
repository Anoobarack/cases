def CardCheck(f, cardId):
    uData = 0
    for line in f:
        if line.split(' ')[0] == cardId:
            uData = line.strip().split(' ')
    return uData

def PinCheck(attempt, truePin):
    if attempt and attempt < 3:
        if attempt > 1:
            print('Неверный pin-код. Повторите попытку')
        pin = input('Введите pin-код: ')
        if pin == truePin:
            return True
        else:
            return PinCheck(attempt+1, truePin)
    else:
        print('2')
        return 0

def Operations(uData):
    print('Приветствуем вас в нашем банке!')
    print('Ваши возможные операции:')
    print('1) Проверка вашего счёта')
    print('2) Списание со счёта определённой суммы')
    print('3) Отмена операции')
    choice = 0
    while(choice == 0):
        choice = int(input('Выберите операцию нажатием кнопки 1, 2 или 3: '))
        if choice > 3:
            print('Вы нажали на неверную кнопку. Повторите попытку')
            choice = 0
        else:
            if choice == 1:
                print('8')
                print('На вашем счёте %s денег' % uData[2])
                choice = 0
            elif choice == 2:
                print('5')
                amount = int(input('Введите сумму списывания: '))
                if amount > int(uData[2]):
                    print('6')
                    print('На вашем счёте недостаточно денег')
                    choice = 0
                else:
                    print('7')
                    uData[2] = str(int(uData[2]) - amount)
                    print('Заберите деньги')
            else:
                print('9')
                print('Удачного вам дня')
    return uData

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

def Authorised(uData):
    attempt = 1
    if PinCheck(attempt, uData[1]):
        if attempt == 1:
            print('1')
        else:
            print('3')
        newData = Operations(uData)
    else:
        print('4')
        newData = CardBlock(uData)
    print('Заберите карту')
    return newData

def main():
    filename = ('doc.txt')
    with open(filename) as f1:
        text = f1.read()
    text = text.split('\n')
    text_list = []
    for i in text:
        a = i.strip().split(' ')
        text_list.append(a)
    f2 = open(filename)
    cardId = input('Вставьте карту: ')
    cardId = cardId.replace(' ', '')
    uData = CardCheck(f2, cardId)
    f2.close()
    if uData != 0:
        f3 = open(filename, 'w')
        newData = Authorised(uData)
        newText = ''
        if text_list[0][0] == uData[0]:
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
        f3.write(newText)
        f3.close()
    else:
        print('Ваша карта не принадлежит нашему банку. Заберите карту')
    return 0

main()
