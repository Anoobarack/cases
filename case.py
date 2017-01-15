# Default project

from turtle import setpos, forward, right, shape, fillcolor, pendown, speed, goto, penup, begin_fill, end_fill

def draw_hexagon(x, y, side_len, color):
    fillcolor(color)
    setpos(x, y)
    pendown()
    begin_fill()
    for i in range(6):
        forward(side_len)
        right(60)
    end_fill()
    penup()

def get_num_hexagons():
    print('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ', end = '')
    while True:
        try:
            num = int(input(''))
            break
        except ValueError:
            print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ', end = '')
    return num

def get_color_choice():
    print('Пожалуйста, введите цвет: ', end = '')
    k = 2
    while k:
        color = input().lower().strip()
        if color == 'желтый':
            color = 'yellow'
            k = 0
        elif color == 'красный':
            color = 'red'
            k = 0
        elif color == 'синий':
            color = 'blue'
            k = 0
        elif color == 'фиолетовый':
            color = 'violet'
            k = 0
        elif color == 'оранжевый':
            color = 'orange'
            k = 0
        elif color == 'зеленый':
            color = 'green'
            k = 0
        else:
            print("'{}' не является верным значением. Пожалуйста, повторите попытку: ".format(color), end = '')
    return color

def draw_pairs(x, y, num, color1, color2, side_len):
    x_of_hex = x
    y_of_hex = y
    for q in range(int(500/(3*side_len))):
        for i in range(num):
            if i % 2:
                color = color1
            else:
                color = color2
            draw_hexagon(x_of_hex, y_of_hex, side_len, color)
            x_of_hex = x_of_hex + 3**0.5 * side_len
        x_of_hex = -200
        y_of_hex = y_of_hex - 1.5*side_len
        for i in range(num):
            if i % 2:
                color = color1
            else:
                color = color2
            draw_hexagon(x_of_hex, y_of_hex, side_len, color)
            x_of_hex = x_of_hex + 3**0.5 * side_len
        color1, color2 = color2, color1
        x_of_hex = x
        y_of_hex = y_of_hex - 1.5*side_len
    if abs((y_of_hex + 1.5*side_len) + 200) > 2*side_len:
        for i in range(num):
            if i % 2:
                color = color1
            else:
                color = color2
            draw_hexagon(x_of_hex, y_of_hex, side_len, color)
            x_of_hex = x_of_hex + 3**0.5 * side_len

def main():
    shape('turtle')
    print('Допустимые цвета заливки:\n красный\n оранжевый\n желтый\n \
зеленый\n синий\n фиолетовый')
    penup()
    color1 = get_color_choice()
    color2 = get_color_choice()
    right(270)
    goto(-200, -200)
    pendown()
    for i in 'four':
        forward(500)
        right(90)
    penup()
    num = get_num_hexagons()
    side_len = (500 / (num+0.5)) / (3**0.5)
    x = -200 + 500 / ((num+0.5) * 2)
    y = 300 - side_len * 1.5
    speed(10)
    draw_pairs(x, y, num, color1, color2, side_len)
    
main()
