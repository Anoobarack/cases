# -*- coding: utf-8 -*- 

"""Case-study#6 Генерация предложений
Разработчики:
Абраменко А.А.(), Головко И.Н.(), Зырянова О.О.()
"""

import random

def main():
    # Вывод шапки.  
    filename = input('Имя файла: ')
    amount_of_senstences = int(input('Количество генерируемых предложений: '))

    # Создаём строку разрешённых символов.  
    LETTERS1 = 'аАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъыьэЭюЮяЯ'
    LETTERS2 = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    LETTERS = LETTERS1 + LETTERS2
    NUMBERS = '0123456789'
    SIGNS = '.,!? '
    ALLOWED_SYMBS = LETTERS + NUMBERS + SIGNS

    # Отбираем текст из файла.  
    f = open(filename, 'r', encoding = 'utf8')
    text = ''
    for line in f:
        for symbol in line:
            if symbol == ' ' and line[line.find(symbol) - 1] == ' ':
                line = line.replace(symbol, '')
            if symbol not in ALLOWED_SYMBS:
                if symbol == '\n':
                    line = line.replace(symbol, ' ')
                else: line = line.replace(symbol, '')
        text += line
    print(text)
    f.close()

    # Установление связей.  
    List_of_words = text.split(' ')
    List_of_capitals = []    # Список заглавных слов  
    for element in List_of_words:
        if element == element.capitalize():
            List_of_capitals.append(element)
    Num_of_capitals = len(List_of_capitals)
    d = {}
    for i in range(len(List_of_words) - 1):
        if List_of_words[i] != '' and List_of_words[i+1] != '':
            if d.get(List_of_words[i]):
                if List_of_words[i+1] != d[List_of_words[i]]:
                    a = []
                    a.append(d[List_of_words[i]])
                    a.append(List_of_words[i+1])
                    d[List_of_words[i]] = a
            else:
                d[List_of_words[i]] = List_of_words[i+1]
    print(d)

    # Создание предложений.
    string = ''
    for i in range(amount_of_senstences):
        random.seed()
        sentence = List_of_capitals[random.randint(0, Num_of_capitals - 1)]
        iterations = random.randint(4, 19)
        sentence = list(sentence)
        for j in range(iterations):
            links = len(d[sentence[len(sentence) - 1]])
            if links == 1:
                word = d[sentence(len(sentence) - 1)]
            else:
                word = d[sentence(len(sentence) - 1)][random.randint(0,links-1)]
            sentence.append(word)
        for k in sentence:
            string += k + ' '
    print(string, end = '')
        

main()
