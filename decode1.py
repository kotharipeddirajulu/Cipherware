###Simple substitution Cipher
import string
import sys
import math


def checkValidityOfKey(mykey):  ## Test condition for the key input
    keyli = list(mykey)
    masterli = list(string.ascii_lowercase)
    keyli.sort()
    masterli.sort()
    if keyli != masterli:
        sys.exit("Please give a string of lowercase letters which consists of all 26 alphabets surely!!")


def Simple_Substitution(text, key):
    global words, symIndex
    word = []
    master = string.ascii_lowercase
    checkValidityOfKey(key)
    charA = master
    charB = key
    charA = charB
    charB = charA
    for alpha in text:
        if alpha.lower() in charA:
            symIndex = charA.find(alpha.lower())
        if alpha.isupper():
            p = charB[symIndex].upper()
            word.append(p)
            words = ''.join(word)
        elif alpha.islower():
            e = charB[symIndex].lower()
            word.append(e)
            words = ''.join(word)
        else:
            word.append(alpha)
            words = ''.join(word)
    print(words)
    return words


# Columnar_Transposition cipher.
def Columnar_Transposition_decode(text, key):
    decrypted = " "
    key_index = 0
    text_index = 0
    text_length = float(len(text))
    textli = list(text)
    keyli = sorted(list(key))
    no_col = len(key)
    no_row = int(math.ceil(text_length / no_col))
    decryt_cipher = []
    for _ in range(no_row):
        decryt_cipher += [[None] * no_col]
    for _ in range(no_col):
        current_index = key.index(keyli[key_index])
        for j in range(no_row):
            decryt_cipher[j][current_index] = textli[text_index]
            text_index += 1
        key_index += 1
    try:
        decrypted = ''.join(sum(decryt_cipher, []))
    except TypeError:
        raise TypeError('This program cannot handle repeating words')

    null_count = decrypted.count('_')

    if null_count > 0:
        return decrypted[: -null_count]
    return decrypted

#Autokey cipher decoder
def Autokey_decode(text, key):
    text1 = text.lower()
    text2 = "".join(text1.split())
    alphabet = string.ascii_lowercase
    ans = ""
    for i in range(len(text2)):
        m = text2[i]
        if i < len(key):
            k = key[i]
        else:
            k = ans[i - len(key)]
        alphI = alphabet.index(m)
        alphI += -1 * alphabet.index(k)
        alphI = alphI % len(alphabet)
        enc = alphabet[alphI]
        ans += enc
    return ans

def Autokey_decode_org(text,key):
    decrypted = ''
    j=0
    auto_te = Autokey_decode(text,key)
    for i in text:
        if i == ' ':
            decrypted += ' '
        else:
            decrypted += auto_te[j]
            j += 1
    print(decrypted)
    return decrypted

Autokey_decode_org('LLG XIKFHR GXKMCX','secret')

#Beaufort cipher
def Beaufort_decode(text, key):
    text1 = text.lower()
    text2 = "".join(text1.split())
    alphabet = string.ascii_lowercase
    ans = ""
    for i in range(len(text2)):
        if len(key)<len(text):
            sys.exit("Please give a string of lowercase letters which is of length of text given!!")
        else:
            char = text2[i]
            keychar = key[i % len(key)]
            alphaIndex = alphabet.index(keychar)
            alphaIndex -= alphabet.index(char)
            alphaIndex %= len(alphabet)
            enc = alphabet[alphaIndex]
            ans += enc
    return ans

def Beaufort_decode_org(text,key):
    decrypted = ''
    j=0
    beau_te = Beaufort_decode(text,key)
    for i in text:
        if i == ' ':
            decrypted += ' '
        else:
            decrypted += beau_te[j]
            j += 1
    return decrypted

##Porta Cipher -........................................................................

def Porta_key_generator(key):
    alphabet = {
        "A": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]],
        "B": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]],
        "C": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]],
        "D": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]],
        "E": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]],
        "F": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]],
        "G": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]],
        "H": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]],
        "I": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]],
        "J": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]],
        "K": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U"]],
        "L": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U"]],
        "M": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T"]],
        "N": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T"]],
        "O": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S"]],
        "P": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S"]],
        "Q": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R"]],
        "R": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R"]],
        "S": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q"]],
        "T": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q"]],
        "U": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P"]],
        "V": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P"]],
        "W": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O"]],
        "X": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O"]],
        "Y": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N"]],
        "Z": [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
              ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N"]]}

    tab = []
    for alpha in key.upper():
        tab.append(alphabet[alpha])
    return tab

def Porta_getPositions(tab,alpha):
    row = -1
    if alpha in tab[0]:
        row=0
    elif alpha in tab[1]:
        row=1

    if row != -1:
        return(row,tab[row].index(alpha))
    else:
        return(None,None)

def Porta_getOpponent(tab,alpha):
    row,col = Porta_getPositions(tab,alpha.upper())
    if row ==1:
        return tab[0][col]
    elif row ==0:
        return tab[1][col]
    else:
        return alpha

def Porta_decode(text, key):
    decrypted = ''
    count = 0
    tab = Porta_key_generator(key)
    for alpha in text.upper():
        decrypted += Porta_getOpponent(tab[count],alpha)
        count = (count + 1)%len(tab)
    return decrypted

## Running key cipher.
def Running_key_decode(text,key):
    alphabet =  [
        None, 'a', 'b',
        'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z']
    decrypted = ''
    for i,j in enumerate(text):
        if j == ' ':
            decrypted += ' '
        else:
            temp = ''
            key_chars = key[i%len(key)]
            key_chars_index = alphabet.index(key_chars)
            text_chars_index = alphabet.index(j)
            decrypted_char_index = text_chars_index - key_chars_index
            decrypted_char = alphabet[
                text_chars_index + 26-key_chars_index
                if text_chars_index<=key_chars_index else text_chars_index - key_chars_index
            ]

            decrypted += decrypted_char
            temp += (
                "key char index: %s - %s\n"
                "text char index: %s - %s\n"
                "Output: %s - %s\n")%(
                key_chars,key_chars_index,alphabet
                ,text_chars_index,decrypted_char,decrypted_char_index
            )
    return decrypted

def Running_key_decode_org(text,key):
    decrypted_org =''
    for alpha in text.split(' '):
        decrypted_org += Running_key_decode(text,key)
        decrypted_org += ' '
    return decrypted_org

### Kamasutra Cipher --------------------------------
def Kamasutra_decode(text,key1):
    global Kamasutra_Tab
    key = key1.upper()
    key_li_temp = list(key)
    key_li = []
    for i in key_li_temp:
        if i not in key_li:
            key_li.append(i)
    key_len = len(key)
    key_split = key_len//2
    li1=key_li[:key_split]
    li2=key_li[key_split:]
    table=[li1,li2]
    Kamasutra_Tab = table
    decrypted = ''
    for letter in text:
        if str.isalpha(letter):
            letter = Kamasutra_getOpponent(table,letter)
        decrypted += letter
    print(decrypted)
    print(table)
    print(len(key))
    return decrypted

def Kamasutra_getPosition(Kamasutra_Tab,letter):
    row = -1
    if letter in Kamasutra_Tab[0]:
        row = 0
    elif letter in Kamasutra_Tab[1]:
        row = 1

    if row!= -1:
        return(row,Kamasutra_Tab[row].index(letter))
    else:
        return(None,None)


def Kamasutra_lower(letter,sign):
    if sign:
       return letter.lower()
    else:
        return letter


def Kamasutra_getOpponent(Kamasutra_Tab,letter):
    sign = False
    if letter.islower():
        sign = True

    row,col = Kamasutra_getPosition(Kamasutra_Tab,letter.upper())

    if row==1:
        return Kamasutra_lower(Kamasutra_Tab[0][col],sign)
    elif row==0:
        return Kamasutra_lower(Kamasutra_Tab[1][col],sign)
    else:
        return letter

Kamasutra_decode('Igllz Tawdmd','ZXCVBNMASDFGHJKLQWERTYUIOP')























