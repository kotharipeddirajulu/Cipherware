# atbash cipher


def atbash_encode(text):
    word = []
    for c in text:
        if c.isupper():
            total = ord('A') + ord('Z')
            s = chr(total - ord(c))
            word.append(s)
            words = ''.join(word)
        elif c == ' ':
            word.append(' ')
            words = ''.join(word)
        else:
            t = ord('a') + ord('z')
            q = chr(t - ord(c))
            word.append(q)
            words = ''.join(word)
    return words


# rot13
def rot13_encode(text):
    word=[]
    for i in text:
        if i.isupper():
            c_index = ord(i) - ord("A")
            new_index = (c_index + 13) % 26
            q = chr(new_index + ord("A"))
            word.append(q)
            words = ''.join(word)
        elif i ==' ':
            word.append(' ')
            words = ''.join(word)
        else:
            c_index = ord(i) - ord("a")
            new_index = (c_index + 13) % 26
            q = chr(new_index + ord("a"))
            word.append(q)
            words = ''.join(word)
    return words

# caesar
def caesar_encode(text, shift):
    word = []
    text = text.lower()

    for i in text:
        if i.isupper():
            c_index = ord(i) - ord("A")
            new_index = (c_index + shift) % 26
            s = chr(new_index + ord("A"))
            word.append(s)
            words = ''.join(word)
        elif c == ' ':
            word.append(' ')
            words = ''.join(word)
        else:
            c_index = ord(i) - ord("a")
            new_index = (c_index + shift) % 26
            q = chr(new_index + ord("a"))
            word.append(q)
            words = ''.join(word)

    return words


# affine
def affine_encode(text, key):
    # E = (a*x + b) % 26
    return ''.join(
        [chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])


# rail fence
def railfence_encode(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ("".join(result))


# baconian
def baconian_encode(message):
    lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
              'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
              'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
              'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
              'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}
    words = ''
    message = message.upper()
    for letter in message:
        if (letter != ' '):
            words += lookup[letter]
        else:
            words += ' '

    return words


# Simple substitution Cipher
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


# Columnar_Transpositions Cipher.
def Columnar_Transposition(text, key):
    encrypted = " "
    key_index = 0
    text_length = float(len(text))
    textli = list(text)
    keyli = list(key)
    no_col = len(key)
    no_row = int(math.ceil(text_length / no_col))
    fill_null = int((no_col * no_row) - text_length)
    textli.extend('_' * fill_null)
    matrix = [textli[i:i + no_col] for i in range(0, len(textli), no_col)]
    for _ in range(no_col):
        current_index = key.index(keyli[key_index])
        encrypted = encrypted + ''.join([no_row[current_index] for no_row in matrix])
        key_index = key_index + 1
    return encrypted


# Autokey Cipher
def Autokey(text, key):
        key_new = generate_key(text, key)
        encrypted = ""
        text = text.lower()
        keyli = list(key_new)

        i = 0
        for alpha in text:
            if alpha == ' ':
                encrypted += ' '
            else:
                x = (ord(alpha) - 2 * ord('a') + ord(keyli[i])) % 26
                i += 1
                encrypted += chr(x + ord('a'))
        return encrypted

def generate_key(text, key):
        text = text.lower()
        key = key.lower()
        i = 0
        while True:
            if len(key) == len(text):
                break
            if text[i] == ' ':
                i += 1
            else:
                key += text[i]
                i += 1
        return key

##Beaufort cipher implementation
def Beaufort(text, key):
    text1 = text.lower()
    text2 = "".join(text1.split())
    alphabet = string.ascii_lowercase
    ans = ""
    for i in range(len(text2)):
        char = text2[i]
        keychar = key[i % len(key)]
        alphaIndex = alphabet.index(keychar)
        alphaIndex -= alphabet.index(char)
        alphaIndex %= len(alphabet)
        enc = alphabet[alphaIndex]
        ans += enc

    return ans

def Beaufort_encode(text,key):
    encrypted = ''
    j=0
    beau_te = Beaufort(text,key)
    for i in text:
        if i == ' ':
            encrypted += ' '
        else:
            encrypted += beau_te[j]
            j += 1
    return encrypted

##Porta Cipher -
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


def Porta_getPositions(tab, alpha):
    row = -1
    if alpha in tab[0]:
        row = 0
    elif alpha in tab[1]:
        row = 1

    if row != -1:
        return (row, tab[row].index(alpha))
    else:
        return (None, None)


def Porta_getOpponent(tab, alpha):
    row, col = Porta_getPositions(tab, alpha.upper())
    if row == 1:
        return tab[0][col]
    elif row == 0:
        return tab[1][col]
    else:
        return alpha


def Porta_encode(text, key):
    encrypted = ''
    count = 0
    tab = Porta_key_generator(key)
    for alpha in text.upper():
        encrypted += Porta_getOpponent(tab[count], alpha)
        count = (count + 1) % len(tab)
    return encrypted

##Running_key_cipher......................
def Running_key_encode(text,key):
    alphabet = [
        None, 'a', 'b',
        'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z']

    encrypted = ''
    for i,j in enumerate(text):
        if j == ' ':
            encrypted += ' '
        else:
            temp = ''
            key_chars = key[i%len(key)]
            key_chars_index = alphabet.index(key_chars)
            text_chars_index = alphabet.index(j)
            encrypted_char_index = text_chars_index - key_chars_index
            encrypted_char = alphabet[
                text_chars_index + 26-key_chars_index
                if text_chars_index<=key_chars_index else text_chars_index - key_chars_index
            ]

            encrypted += encrypted_char
            temp += (
                "key char index: %s - %s\n"
                "text char index: %s - %s\n"
                "Output: %s - %s\n")%(
                key_chars,key_chars_index,alphabet
                ,text_chars_index,encrypted_char,encrypted_char_index
            )
    return encrypted

def Running_key_encode_org(text,key):
    encrypted_org =''
    for alpha in text.split(' '):
        encrypted_org += Running_key_encode(text,key)
        encrypted_org += ' '
    return encrypted_org

### Kamasutra cipher.........................................
def Kamasutra_encode(text,key1):
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
    encrypted = ''
    for letter in text:
        if str.isalpha(letter):
            letter = Kamasutra_getOpponent(table,letter)
        encrypted += letter
    return encrypted

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













