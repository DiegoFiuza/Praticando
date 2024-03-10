from random import * 
choice

lista = ['rivaldo', 'ronaldo','kaka','ronaldinho','alisson','neymar','casemiro','roberto carlos','zico','pele']
palavra = choice(lista)
print('''
                                     >>>>  Jogo da Forca  <<<<
      
>>> O jogo irá escolher um nome de algum jogador que já jogou na Seleção Brasileira. Adivinhe o escolhido!! <<<
''')
letra_usuário = []
chances = 5
ganhou = True
while True:
#Se a letra estiver na palavra, vai aparecer a letra, caso contrário aparecerá _
    for letra in palavra:
        if letra in letra_usuário:
            print(letra, end='')
        else:
            print('_', end='')
    print('\n')
    ganhou = True
    tentativa = input('Digite uma letra: ')
    #A letra digitada será adicionada na lista
    letra_usuário.append(tentativa.lower())
#Se a letra digitada não estiver na palavra, irá diminuir a chance em 1
    if tentativa.lower() not in palavra:
        chances = chances - 1
        print(f'Você possui {chances} chances')
    for letra in palavra:
    #se a letra digitada não estiver na letra da palavra, você ainda não ganhou
        if letra.lower() not in letra_usuário:
            ganhou = False
#se as chances chegarem a 0 ou se você ganhar, o programa finaliza
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'Parabéns, você ganhou!!! O nome era {palavra.title()}!!')
else:
    print(f'Você perdeu!! O nome era {palavra.title()}!!')