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
def escolha(digitado):
    digitado = input('O jogo é Pedra,Papel e Tesoura. Escolha entre um dos três para jogar: ').title()
    if maquina == digitado:
        print('Empate')
    elif maquina == 'Pedra' and digitado == 'Tesoura':
        print('Pedra amassa Tesoura. Você Perdeu..')
    elif maquina == 'Pedra' and digitado == 'Papel':
        print('Papel cobre Pedra. Você venceu!!')
    elif maquina == 'Papel' and digitado == 'Pedra':
        print('Papel cobre Pedra. Você perdeu..')
    elif maquina == 'Papel' and digitado == 'Tesoura':
        print('Tesoura corta Papel. Você venceu!!')
    elif maquina == 'Tesoura' and digitado == 'Pedra':
        print('Pedra amassa Tesoura. Você venceu!!')
    elif maquina == 'Tesoura' and digitado == 'Papel':
        print('Tesoura corta Papel. Você perdeu..')
    else:
        print('Digite uma escolha válida..')
        return escolha(digitado)
while True:
    maquina = random.choice(jogo_lista)
    escolha(escolha)
    controle(controle)