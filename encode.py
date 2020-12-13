#atbash cipher
def atbash_encode(text):
    word=[]
    for c in text:
        if c.isupper():
            total = ord('A') + ord('Z')
            s = chr(total-ord(c))
            word.append(s)
            words = ''.join(word)
        elif c ==' ':
            word.append(' ')
            words = ''.join(word)
        else:
            t = ord('a') + ord('z')
            q = chr(t-ord(c))
            word.append(q)
            words = ''.join(word)
    return words

#rot13
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

#caesar
def caesar_encode(text,shift):
    word=[]
    for i in text:
        if i.isupper():
            c_index = ord(i) - ord("A")
            new_index = (c_index + shift) % 26
            s = chr(new_index + ord("A"))
            word.append(s)
            words = ''.join(word)
        elif c ==' ':
            word.append(' ')
            words = ''.join(word)
        else:
            c_index = ord(i) - ord("a")
            new_index = (c_index + shift) % 26
            q = chr(new_index + ord("a"))
            word.append(q)
            words = ''.join(word)

    return words

#affine
def affine_encode(text,key):
        #E = (a*x + b) % 26
        return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ])

#rail fence
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
    return("" . join(result))

#baconian
def baconian_encode(message):
    lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
              'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
              'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
              'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
              'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
    words = ''
    message = message.upper()
    for letter in message:
        if(letter != ' '):
            words += lookup[letter]
        else:
            words += ' '

    return words

#polybius
def polybius_encode(text):
    word=[]
    for t in text:
        if t.isupper():
            row = int((ord(t) - ord('a')) / 5) + 1
            col = ((ord(t) - ord('a')) % 5) + 1

            # if character is 'k'
            if t == 'K':
                row = row - 1
                col = 5 - col + 1

            # if character is greater than 'j'
            elif ord(t) >= ord('J'):
                if col == 1 :
                    col = 6
                    row = row - 1

                col = col - 1

            word.append(str(row))
            word.append(str(col))
        elif t ==' ':
            word.append(' ')
        #lowercase
        else:
            row = int((ord(t) - ord('a')) / 5) + 1
            col = ((ord(t) - ord('a')) % 5) + 1

            # if character is 'k'
            if t == 'k':
                row = row - 1
                col = 5 - col + 1

            # if character is greater than 'j'
            elif ord(t) >= ord('j'):
                if col == 1 :
                    col = 6
                    row = row - 1

                col = col - 1

            word.append(str(row))
            word.append(str(col))
    words = ''.join(word)
    return words


print(rot13_encode('mlk'))

