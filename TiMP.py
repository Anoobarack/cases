# -*- coding: utf-8 -*-

def CardCheck(f, cardId):
    uData = 0
    for line in f:
        if line.split(' ')[0] == cardId:
            uData = line.split(' ')
    return uData

def PinCheck(attempt, truePin):
    if attempt and attempt < 4:
        if attempt > 1:
            print('Неверный pin-код. Повторите попытку')
        pin = input('Введите pin-код: ')
        if pin == truePin:
            return True
        else:
            return PinCheck(attempt+1, truePin)
    else:
        return 0

def Operations(uData):
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
                print('На вашем счёте %s денег' % uData[2])
                choice = 0
            elif choice == 2:
                amount = int(input('Введите сумму списывания: '))
                if amount > uData[2]:
                    print('На вашем счёте недостаточно денег')
                    choice = 0
                else:
                    uData[2] = str(int(uData[2]) - amount)
                    print('Заберите деньги')
            else:
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
        uData = {}
    else:
        print('Карта не была заблокирована. Подождите перед следующей попыткой')
    return uData

def Authorised(uData):
    attempt = 1
    if PinCheck(attempt, uData[1]):
        newData = Operations(uData)
    else:
        newData = CardBlock(uData)
    print('Заберите карту')
    return newData

def main():
    filename = ('doc.txt')
    f = open(filename, 'r', encoding = 'utf8')
    cardId = input('Вставьте карту: ')
    cardId = cardId.replace(' ', '')
    uData = CardCheck(f, cardId)
    text = [line.split('\n') for line in f]
    f.close()
    print(text)
    f = open(filename, 'w', encoding = 'utf8')
    if uData != 0:
        newData = Authorised(uData)
        for i in text:
            if i[0] == newData[0]:
                i = newData
        newText = ''.join(a+'\n' for a in text)
        f.write(newText)
    else:
        print('Ваша карта не принадлежит нашему банку. Заберите карту')
    f.close()
    return 0

main()
