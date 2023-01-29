# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def compress(string):
    out_string = ''
    char = ''
    count = 0
    for item in string:
        if item != char:
            if count != 0:
                out_string += str(count) + char
            char = item
            count = 1
        else:
            count += 1
    if count != 0:
        out_string += str(count) + char
    print(out_string)
    return out_string


def decompression(string):
    out_string = ''
    count = ''
    for item in string:
        if item.isdigit():
            count += item
        else:
            out_string += int(count) * item
            count = ''
    print(out_string)
    return out_string


in_f = open('in_text.txt', 'r')
out_f = open('out_text.txt', 'w')
for string in in_f:
    if string[0].isdigit():
        out_f.write(decompression(string))
    else:
        out_f.write(compress(string))
in_f.close()
out_f.close()