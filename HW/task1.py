# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint 

game_type = int(input('Выберите тип игры 1 (человек против человека) или 2 (человек против компьютера) 1/2: '))
while True:
    if game_type == 1:
        gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
        break
    elif game_type == 2:
        gamer_1, gamer_2 = input('введите имя игрока: '), 'BOT'
        break
    else:
        game_type = int(input('Вы ошиблись с вводом, введите 1 (чел vs чел) или 2 (чел vs компьютер): '))
count_of_sweets = int(input('введите количество конфет для игры (2021 - очень много, надоест играть): '))
sortition = randint(0,2)
if sortition == 0:
    current_gamer = gamer_1
else:
    current_gamer = gamer_2
print (f'Игру начинает {current_gamer}')
arr_bot = [i for i in range(29, count_of_sweets+1) if i%29 == 0]
while count_of_sweets > 0:
    print(f'количество оставшихся конфет: {count_of_sweets}')
    while True:
        if current_gamer == gamer_1 or gamer_2 != 'BOT':
            number_to_delete = int(input(f'ход игрока {current_gamer} (1 - 28): '))
        else:
            if count_of_sweets <= 28:
                number_to_delete = count_of_sweets
            elif count_of_sweets in arr_bot:
                number_to_delete = randint (1, 28)
            elif count_of_sweets not in arr_bot:
                for i in range (1, 29):
                    if ((count_of_sweets - i) in arr_bot):
                        number_to_delete = i
            print (f'ход игрока {current_gamer} (1 - 28): {number_to_delete}')
        if number_to_delete >= 1 and number_to_delete <= 28:
            break
    count_of_sweets -= number_to_delete
    if count_of_sweets != 0:
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
print(f'Победил {current_gamer}')
