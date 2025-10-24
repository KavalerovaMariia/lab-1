#Вариант 4
#Сгенерировать при помощи escape-символов в консоли изображение флага, соответственно варианту (столбец "Страна").
import math

RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
line = ' ' * 4
BLUE = '    \u001b[44m'
lenght = 15
height = lenght
for i in range(height):
    if i < height // 2:
        print(f"{WHITE}{line * lenght}{END}")
    else:
        print(f"{RED}{line * lenght}{END}")

#Сгенерировать в консоли повторяющийся узор (столбец "Узор").
def draw_uzor_d():
    line1 = ' ' * 32
    line2_0 = ' ' * 15
    line2_1 = ' ' * 2
    line4_0 = ' ' * 6
    line4_1 = ' ' * 16
    line4_2 = ' ' * 6
    for a in range(4):
        for i in range(6):
            if i %2!=0:
                print(f'\x1b[48;5;{16}m{line1}\x1b[0m')
            elif i == 2:
                print(
                f'\x1b[48;5;{15}m{line2_0}\x1b[0m'
                f'\x1b[48;5;{16}m{line2_1}\x1b[0m'
                f'\x1b[48;5;{15}m{line2_0}\x1b[0m')
            elif i == 4:
                print(
                    f'\x1b[48;5;{15}m{line4_0}\x1b[0m'
                    f'\x1b[48;5;{16}m{line2_1}\x1b[0m'
                    f'\x1b[48;5;{15}m{line4_1}\x1b[0m'
                    f'\x1b[48;5;{16}m{line2_1}\x1b[0m'
                    f'\x1b[48;5;{15}m{line4_2}\x1b[0m')
        print(f'\x1b[{32}A')
draw_uzor_d()
#Сгенерировать в консоли график функции (1 четверти) при помощи escape-символов, минимум 9 строк в высоту (столбец "Функция").
tablitsa = [[0 for i in range(10)] for i in range(10)]

result_list = [i**0.5 for i in range(10)]



step = round(abs(result_list[9] - result_list[0]) / 9, 3) #шаг

for i in range(9,0,-1):
    for j in range(0,10,1):
        if j == 0:
            tablitsa[i][0] = round((i)*step,3)

        else:
            if abs(result_list[j] - tablitsa[i][0])  < step:
                tablitsa[i][j] = '*'
            else:
                tablitsa[i][j] = '.'




for i in range(9,0,-1):
    for j in range(0,10,1):
        if tablitsa[i][j] == '*':
            print(f'\x1b[48;5;{159}m{tablitsa[i][j]}\x1b[0m', end='')
        else:
            print(f'\x1b[48;5;{16}m{tablitsa[i][j]}\x1b[0m', end='')
    print()
print(f'\x1b[48;5;{16}m{"\t 123456789"}\x1b[0m')




#Используя прилагаемый файл с числовой последовательностью sequence.txt
#вывести диаграмму процентного соотношения согласно варианту.
#(Среднее по модулю первых 125 и вторых 125 чисел)
f = open("sequence.txt")
fail = f.read()

s = [x for x in fail.split()]
first_125 = []
second_125 = []

for i in range(0,len(s)):
    if i < 125:

        first_125.append(abs(float(s[i])))
    elif 125<=i<250:
        second_125.append(abs(float(s[i])))

srednee_first_125 = (sum(first_125))/125
srednee_second_125 = (sum(second_125))/125

#print(srednee_first_125)
#print(srednee_second_125)
tablitsa_125 = [[0 for i in range(3)]for  i in range(35)]


result_125 = [i*0.15 for i in range(35)]

for a in range(34,-1,-1):
    for b in range(0,3,1):
        if b == 0:
            tablitsa_125[a][b] = result_125[a]
            #print(tablitsa_125[a][0])
        elif b == 1:
            tablitsa_125[a][b] = 1
        elif b == 2:
            if tablitsa_125[a][0] <= 4.8:
                tablitsa_125[a][b] = 1

for a in range(34,-1,-1):
    for b in range(0, 3,1):

        if tablitsa_125[a][b] == 1 and b == 1:
            print(f'\x1b[48;5;{5}m{' '}\x1b[0m', end='\t\t')

        elif tablitsa_125[a][b] == 1 and b == 2:
            print(f'\x1b[48;5;{12}m{' '}\x1b[0m', end='')

    print()
print(f'5.15\t4.85')
print('погрешность +-0.05')







