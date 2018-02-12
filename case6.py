# -*- coding: utf-8 -*- 

"""Case-study#6 Генерация предложений
Разработчики:
Абраменко А.А.(5), Головко И.Н.(70), Зырянова О.О.(20)
"""

import random

def main():
    # Вывод шапки.  
    filename = input('Имя файла: ')
    amount_of_sentences = int(input('Количество генерируемых предложений: '))

    # Создаём строку разрешённых символов.  
    LETTERSBIG = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERSSMALL = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
    LETTERS = LETTERSBIG + LETTERSSMALL
    NUMBERS = '0123456789'
    SIGNS = '-.,!? '
    ALLOWED_SYMBS = LETTERS + NUMBERS + SIGNS

    # Отбираем текст из файла.  
    f = open(filename, 'r', encoding = 'cp1251')
    text = ''
    for line in f:
        for symbol in line:
            if symbol not in ALLOWED_SYMBS:
                if symbol == '\n':
                    line = line.replace(symbol, ' ')
                else: line = line.replace(symbol, '')
        text += line
    text = text.replace(' ,', ',')
    text = text.replace(' .', '.')
    text = text.replace(' !', '!')
    text = text.replace(' ?', '?')
    text = text.replace('  ', ' ')
    f.close()

    # Первичная обработка текста.  
    List_of_words = text.split(' ')
    if '' in List_of_words:
        List_of_words.remove('')
    List_of_capitals = []    # Список заглавных слов  
    List_of_endings = []    # Список конечных слов  
    for element in List_of_words:
        if element == '':
            continue
        if element[0] in LETTERSBIG:
            List_of_capitals.append(element)
        if element[len(element)-1] in '.?!':
            List_of_endings.append(element)
    Amount_of_capitals = len(List_of_capitals)
    
    # Создание словаря связей.  
    d = {}
    for i in range(len(List_of_words) - 1):
        if List_of_words[i] != '' and List_of_words[i+1] != '':
            if d.get(List_of_words[i]):
                if type(d.get(List_of_words[i])) == list:
                    a = []
                    a.append(List_of_words[i+1])
                    a.extend(d.get(List_of_words[i]))
                    d[List_of_words[i]] = a
                else:
                    if List_of_words[i+1] != d[List_of_words[i]]:
                        a = []
                        a.append(d[List_of_words[i]])
                        a.append(List_of_words[i+1])
                        d[List_of_words[i]] = a
            else:
                d[List_of_words[i]] = List_of_words[i+1]
    
    # Создание предложений.
    string = ''
    for i in range(amount_of_sentences):
        random.seed()
        lastword = List_of_capitals[random.randint(0, Amount_of_capitals - 1)]
        iterations = random.randint(4, 19)    # Количество слов в предложении  
        ended = False
        for j in range(iterations):
            if lastword not in List_of_endings:
                string += ' '
                if type(d[lastword]) == list:
                    links = len(d[lastword])
                else:
                    links = 1
                if links == 1:
                    word = d[lastword]
                    if word in List_of_endings:
                        j = iterations
                else:
                    word = d[lastword][random.randint(0,links-1)]
                    if word in List_of_endings:
                        j = iterations
                string += lastword
                lastword = word
            elif lastword in List_of_endings:
                string += ' ' + lastword
                ended = True
                break
        if ended == False:
            string+=' '+List_of_endings[random.randint(0,len(List_of_endings)-1)]
    print(string, end = '')

main()
