import random 
import sys
import time
#pedra,papel e tesoura
def encerrar():
    sys.exit()
def controle(x):
    x=input('Deseja continuar [s / n]:')
    x.lower()
    while True:
        if x == 'n' or x =='nao':
            print('Saindo...')
            encerrar()
        elif x =='s' or x=='sim':
            print('Continuando')
            break
        else:
            print('Digite um caracter válido!')
            return controle(x)

jogo_lista = ['Pedra','Papel','Tesoura']
while True:
    maquina = random.choice(jogo_lista)
    jogador = input('O jogo é Pedra,Papel e Tesoura. Escolha entre um dos três para jogar: ').title()
    if maquina == jogador:
        print('Empate')
    elif maquina == 'Pedra' and jogador == 'Tesoura':
        print('Pedra amassa Tesoura. Você Perdeu..')
    elif maquina == 'Pedra' and jogador == 'Papel':
        print('Papel cobre Pedra. Você venceu!!')
    elif maquina == 'Papel' and jogador == 'Pedra':
        print('Papel cobre Pedra. Você perdeu..')
    elif maquina == 'Papel' and jogador == 'Tesoura':
        print('Tesoura corta Papel. Você venceu!!')
    elif maquina == 'Tesoura' and jogador == 'Pedra':
        print('Pedra amassa Tesoura. Você venceu!!')
    elif maquina == 'Tesoura' and jogador == 'Papel':
        print('Tesoura corta Papel. Você perdeu..')
    else:
        print('Digite uma escolha válida..')
    controle(controle)