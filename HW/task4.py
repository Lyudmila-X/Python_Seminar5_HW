# Шифр Юлия

data_input = open('HW\Juliusinput.txt', 'r')
data_output = open('HW\Juliusoutput.txt', 'w')
string_input = data_input.readline().strip()
k = int(data_input.readline())
string_output = ''
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
for i in string_input:
    if i in [" ", ",", ":", ";", "-"]:
        string_output = string_output + i
    else:
        index_letter = alphabet.index(i)
        string_output = string_output + str(alphabet[index_letter-k])
data_output.write(string_output)
data_input.close
data_output.close
