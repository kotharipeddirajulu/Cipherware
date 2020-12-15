import random

def rand(min, max):
    return int((max - min) * random.random() + min)

def generate_table():
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]

    for y in range(5):
        for x in range(5):
            table[x][y] = alphabet[rand(0, len(alphabet))]
            alphabet = alphabet.replace(table[x][y], '')
    return table

def getStr(x, format='%02s'):
    return ''.join(format % i for i in x)


def print_table(table):
    print(' ' + getStr(range(1, 6)))
    for row in range(0, len(table)):
        print(str(row + 1) + getStr(table[row]))


def encrypt(table, words):
    cipher = ''

    for ch in words.upper():
        for row in range(len(table)):
            if ch in table[row]:
                x = str((table[row].index(ch) + 1))
                y = str(row + 1)
                cipher += y + x
    return cipher


#
# 解密
#
def decrypt(table, numbers):
    text = ''
    for index in range(0, len(numbers), 2):
        y = int(numbers[index]) - 1
        x = int(numbers[index + 1]) - 1
        text += table[y][x]
    return text


if __name__ == '__main__':

    table = generate_table()

    print_table(table)


    ciphertext = encrypt(table, "hello, world")

    print(ciphertext)

    print(decrypt(table, ciphertext))