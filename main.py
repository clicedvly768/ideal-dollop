from random import *

words = ['Mi bombo', 'Dima V Pivas', 'Pyak.ru', 'Pyak Recors', 'Bombo clar']
secret_words = choice(words)
use_letthe = []
display = ['_'] * len(secret_words)
attempt = 3

while attempt > 0 and '_' in display:
    print('Word:',''.join(display))
    print('Use letthe: '.join(use_letthe))
    print('Used attempt: ', attempt)

    inputer = input('Enter letthe: ')

    if len(inputer) != 1 or not inputer.isalpha():
        print('Pleas enter letthe.')
        continue

    if inputer in use_letthe:
        print('Fuck you, dude.')
        continue

    use_letthe.append(inputer)
    
    if inputer in secret_words:
        print('YAYAYYAYAYYAYAYAYAYYAYAYAYY!')
        print()
        for i, letthe in enumerate(secret_words):
            if letthe == inputer:
                display[i] = inputer
    else:
        print('Fuck')
        print()
        sattempt -= 1 
if '_' not in display:
    print('YAYAYAYAYAYAYASYAYAYAYAYAYAYAY!!!')
else:
    print('NONONONONONOONONONONONONONONONOON!!!')


