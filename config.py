alphabet = {
    1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f',
    7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l',
    13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r',
    19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 
    25:'y', 26:'z' 
}

cipher = []

def my_cipher(text, num_bits=1):
    global cipher
    key = 0
    for i in range(0, len(text)):
        if text[i] == ' ':
            cipher.append(text[i])
        for j in range(1, len(alphabet)+1):
            if text[i].lower() == alphabet[j]:
                key = j + num_bits
                if key > 26:
                    key = 1
                if key < 1 or key < 2:
                    key = 1 or 2
                cipher.append(alphabet[key])
                break
    return