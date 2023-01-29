# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
from random import randint

def print_field(list):
    print('\ | 1 | 2 | 3 |')
    print('---------------')
    for i in range(3):
        for j in range(3):
            if j == 0:
                print(f'{i + 1} | ', end = '')
            print(f'{list[i * 3 + j]} | ', end = '')
            # if j != 2:
                # print(' | ', end = '')
        print('')

def check_win(fields, simbol):
    for i in range(3):
        if fields[i] == fields[i + 3] == fields[i + 6] == simbol:
            return True
        elif fields[i * 3] == fields[i * 3 + 1] == fields[i * 3 + 2] == simbol:
            return True
    if fields[0] == fields[4] == fields[8] == simbol or fields[2] == fields[4] == fields[6] == simbol:
        return True
    return False


def bot_make_move(list):
    while 1:
        i = randint(0, 2)
        j = randint(0, 2)
        if list[i * 3 + j] == ' ':
            list[i * 3 + j] = 'X'
            if check_win(list, 'X'):
                return True
            return False

def make_move(list, player_num, player_name):
    list_simbol = ['0', 'X']
    print(f'Ходит игрок {player_name}\nЧто бы сделать ход введите номер строки и номер столбца')
    print_field(list)
    while 1:
        while 1:
            i = int(input('Введите номер строки (от 1 до 3):'))
            if i > 0 and i < 4:
                break
        while 1:
            j = int(input('Введите номер столбца (от 1 до 3):'))
            if i > 0 and i < 4:
                break
        if list[(i-1) * 3 + (j - 1)] == ' ':
            list[(i-1) * 3 + (j - 1)] = list_simbol[player_num]
            if check_win(list, list_simbol[player_num]):
                return True
            return False
        print('Выбранная ячейка уже занята! Введите новую ячейку!')

def game(player):
    list_of_fields= [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while 1:
        for i, name in enumerate(player):
            if list_of_fields.count(' ') == 0:
                print_field(list_of_fields)
                return 'дружба'
            if name == 'бот Сергей':
                stop = bot_make_move(list_of_fields)
            else:
                stop = make_move(list_of_fields, i, name)
            if stop:
                print_field(list_of_fields)
                return name



print('Начало игры')
while 1:
    play_mode = int(input('Введите режим игры: 0 - игра с ботом, 1 - два игрока '))
    if play_mode < 0 or play_mode > 1:
        print('Вы ввели неверный режим!')
    else:
        break
player_list = [input(f'Введите имя игрока номер {i + 1}: ') for i in range(play_mode + 1)]
if play_mode == 0:
    player_list.append('бот Сергей')
win_name = game(player_list)
print(f'Поздравляем, выиграл игрок {win_name}')





#  \ | 1 | 2 | 3 |
# ----------------
#  1 |   |   |   |
#  ---------------
#  2 |   |   |   |
#  ---------------
#  3 |   |   |   |