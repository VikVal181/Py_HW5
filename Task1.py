# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint


def bot_bring(candy):
    max_turn = 28
    if max_turn > candy:
        max_turn = candy
    if candy % (max_turn + 1) == 0:
        bot_candy = max_turn
    else:
        bot_candy = candy - (candy // (max_turn + 1) * (max_turn + 1) + 1)
        if bot_candy == 0:
            bot_candy = randint(1, max_turn)
    print(f'бот Сергей взял {bot_candy}')
    return candy - bot_candy


def bring_candy(candy, name):
    if name == 'бот Сергей':
        return bot_bring(candy)
    else:
        while 1:
            candy_number = int(input(f'{name}, введите количество конфет, которое хотите взять: '))
            if candy_number > candy:
                print('На столе меньше кофет')
            elif candy_number < 1 or candy_number > 28:
                print('Введено неверное чило')
            else:
                return candy - candy_number


def check_win(candy, name):
    if candy == 0:
        print(f'Игорок {name} проиграл!')
        return True
    return False


print('НАЧАЛО ИГРЫ')
while 1:
    play_mode = int(input('Введите режим игры: 0 - игра с ботом, 1 - два игрока '))
    if play_mode < 0 or play_mode > 1:
        print('Вы ввели неверный режим!')
    else:
        break
while 1:
    current_candy = int(input('Введите количество конфет на столе: '))
    if current_candy <= 0:
        print('Количество конфет должно быть больше 0')
    else:
        break
player_list = [input(f'Введите имя игрока номер {i + 1}: ') for i in range(play_mode + 1)]
if play_mode == 0:
    player_list.append('бот Сергей')
while 1:
    for item in player_list:
        print(f'Оставшееся количество конфет: {current_candy}')
        current_candy = bring_candy(current_candy, item)
        win_flag = check_win(current_candy, item)
        if win_flag:
            break
    if win_flag:
        break
