# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data_input = open('HW\input.txt', 'r')
data_output = open('HW\output.txt', 'w')
string_input = data_input.read()
string_output = ''
element = string_input[0]
count = 1
for i in range(1, len(string_input)):
    if element == string_input[i]:
        count+= 1
    else:
        string_output = string_output + str(count) + str (element)
        count = 1
        element = string_input[i]
    
string_output = string_output + str(count) + str (element)
data_output.write(string_output)
data_input.close
data_output.close
