import string, secrets

dict_snowii = {'a': '^fXbKmuIij', 'b': 'A}(rsC-NO0', 'c': '$gQax0ozEA', 'd': '4{aF,-*Bum', 'e': 'TNUhP4s9$b', 'f': 'g^p#olxAeq', 'g': 'x6O-`3wssp', 'h': 'azV^  ]%b;', 'i': "L?2:('x!bs", 'j': 'be@~B%+?KI', 'k': '6<r#)JG"nS', 'l': "UW'a=66C]]", 'm': 'K9qPj5R) A', 'n': '{TU-2\\[_l0', 'o': 'R:6u)=9[|[', 'p': '-qs{1MQ"\\]', 'q': 'hr)EP`WBCJ', 'r': 'csP:YM!P6(', 's': "J']H'>aHy&", 't': '8!o:8cvFg,', 'u': 'M7]SyI!.u)', 'v': "zjX(mgc'c,", 'w': ';OF!#/& q^', 'x': '!5XZh*)l{>', 'y': 'w+>/$Bn0H+', 'z': ':Xxvh0q%&Z', 'A': 'HWK6"3Ee!\'', 'B': '"Ep0k&|;fF', 'C': 'cQ_WO|E7kM', 'D': 'O_$X^ez=4R', 'E': '}:4)3?aoz;', 'F': '{;hpX(=6vJ', 'G': 'BK_.v-:Q^]', 'H': "qnyfE]c;'H", 'I': '%\\tsZAit<|', 'J': '#pagc^A&[>', 'K': 'EPWZVr!"ez', 'L': '"%9D`q7SwX', 'M': '[3WJl~:k.O', 'N': '{p:D~FGlw`', 'O': 'G)C&^lr\\)J', 'P': ',QuYT\\l:Xp', 'Q': 'G~0o1oiZjg', 'R': '2JoY4:H*zY', 'S': '0:.0(wHde#', 'T': '63%1gcPzBe', 'U': 'e6bV{\\Oy# ', 'V': '5/Kd7pO\\T2', 'W': '~M7e4GgB4)', 'X': '?bf=C|-E5G', 'Y': 'H}h/E^yu _', 'Z': 'UM-~aaEyYK', '0': 'e/wogj7W(K', '1': 'z;<i9_\\h9u', '2': 'KvC2\\8sC:\\', '3': '@Og<m\\q|4Y', '4': 'D`@CkKPb2_', '5': ' XvdCODz@"', '6': '=kF=%cUm$n', '7': '^>Z+<X|3tU', '8': 'KV F{$cTV"', '9': ':uyz*_+@N6', ' ': 'aPDzrO6*%"', '!': 'pDV-n%ALKZ', '"': 'f7DmhGB"1c', '#': 'SE;.C)PAE!', '$': 'Ot5=Y9kN`9', '%': 'h4yP&ut,07', '&': '&]5e_ybDj*', "'": "A*Vn1'G:iY", '(': 'Fp.ehKRx}h', ')': '!XD)A0~o[#', '*': 'z"gH~*(P0.', '+': '4W vpg/7N=', ',': 'l<H$e~F-b"', '-': 'em?/,tq|Os', '.': '/1Mv,C#Eme', '/': 'QZVd|h`4!-', ':': '}8YLg%X<g`', ';': '4QCl$XW4nP', '<': '/w0kNwb=)n', '=': '|9?!D%F`G*', '>': '\\~H_@Mr#Ye', '?': 'e!w/-`QGMT', '@': 'UJ2*u^g!WN', '[': "r'FKOEfB7M", '\\': '53Q*/L|X?x', ']': "N<I'r#\\FQ#", '^': 'uV&`pVSLZR', '_': '=+DSVb0WbL', '`': 'g7r=rE)!y0', '{': ' 3d>^=n=F%', '|': "DCN`l'Sxdt", '}': "AJN v'Jai@", '~': 'VgEam Bz"`'}

def create_dict_encryted():

    '''
    Returns an encrypted dictionary. I dubbed it of snowwii, that's my cat's name, but you can change.
    '''

    letters  = string.ascii_letters + string.digits + ' ' +  string.punctuation
    list_letter = []

    for index in range(len(letters)):
        list_letter.append(letters[index])

    values = ''
    snowii = []

    for keeps in range(len(list_letter)):
        for do in range(10):
            choice = secrets.choice(letters)
            values += choice
        snowii.append(values)
        values = ''

    dict_snowii = dict(zip(list_letter, snowii))

    return dict_snowii

def encryped_text(string):

    '''
    Returns a text encrypted in snowii. Receive a string.
    '''

    text = string
    already_encryted = ''

    for index in range(len(text)):
        letter = dict_snowii.get(text[index])
        already_encryted+=letter
    
    return already_encryted

def decrypting(string):

    '''
    Returns a decrypted text in snowii. Receive a string encrypted in snowii.
    '''

    end = len(string)
    unencrypted = ''
    for index in range(0, end, 10):
        value = string[index:(index+10)]

        for k, v in dict_snowii.items(): 
            if value in v:
                unencrypted+=k

    return unencrypted

def main(string):

    '''
    Receive a text and do: encrypted, decrypted and print the results.
    '''

    text = str(string)
    encry_text = encryped_text(text)
    print(f'\nOok. Your text was encrypted, here it is:\n{encry_text}')
    
    decry_text = decrypting(encry_text)
    print(f'\nNow, we decrypted your text. Follow:\n{decry_text}\n')

main('Your password')
