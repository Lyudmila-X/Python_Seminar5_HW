# Создайте программу для игры в ""Крестики-нолики"".

from optparse import Values
from random import randint

def display (val): 
    print("\n") 
    print("\t     |     |") 
    print(f"\t  {val[0]}  |  {val[1]}  |  {val[2]}") 
    print('\t_____|_____|_____') 
    print("\t     |     |") 
    print(f"\t  {val[3]}  |  {val[4]}  |  {val[5]}") 
    print('\t_____|_____|_____') 
    print("\t     |     |") 
    print(f"\t  {val[6]}  |  {val[7]}  |  {val[8]}") 
    print("\t     |     |") 
    print("\n") 

gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
sortition = randint(0,2)
if sortition == 0:
    current_gamer = gamer_1
else:
    current_gamer = gamer_2
print (f'Игру начинает {current_gamer}')
value_input = {}
val_inp = input('Выберите x или O: ')
value_input[current_gamer] = val_inp
current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
value_input[current_gamer] = "x" if (val_inp == 'O' or val_inp == 'О' or val_inp == 'o' or val_inp == 'о' or val_inp == '0') else 'O'
current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    display(values)
    current_value = input(f"{current_gamer}, выберете поле для хода: ")
    if current_value in values:
        val_index = values.index(current_value)
        values[val_index] = value_input[current_gamer]
        if ((values[0] == values[1] and values[1] == values[2])
            or (values[3] == values[4] and values[4] == values[5])
            or (values[6] == values[7] and values[7] == values[8])
            or (values[0] == values[4] and values[4] == values[8])
            or (values[2] == values[4] and values[4] == values[6])
            or (values[0] == values[3] and values[3] == values[6])
            or (values[1] == values[4] and values[4] == values[7])
            or (values[2] == values[5] and values[5] == values[8])):
            display(values)
            print(f'Победил {current_gamer}')
            break
        if (values.count('x') + values.count(val_inp)) == 9:
            print('Ничья')
            break
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    else:
        print("Поле занято или вы ввели неверную цифру")
