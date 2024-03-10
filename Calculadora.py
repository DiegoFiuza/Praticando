#Calc
import math
import decimal
import sys
decimal.getcontext().prec = 100
print("""
           >>>>  Calculadora:  <<<<

""")
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

soma = 0
subtracao = 0
subtracao_2 = 0
divisao = 0
divisao_2 = 0
multiplicacao = 0
raiz = 0
raiz_2 = 0
log = 0
log_2 = 0
potencializacao = 0
potencializacao_2 = 0
seno = 0
seno_2 = 0
cos = 0
cos_2 = 0
tan = 0
tan_2 = 0
while True:
    numero_1 = float(input('Digite o primeiro número da operação: '))
    numero_2 = float(input('Digite o segundo número de sua operação: '))
    operacao = input('''Digite a operação. Escolha entre:  [ soma | subtracao | divisao | multip | raiz | potencializacao | log | sin | cos | tan ]
                     =  ''')
    operacao.lower()
    if operacao == 'soma':
        soma = decimal.Decimal(numero_1) + decimal.Decimal(numero_2)
        print(f'A Soma do numero 1 pelo numero 2 é: {soma}')
    elif operacao == 'subtracao':
        subtracao = decimal.Decimal(numero_1) - decimal.Decimal(numero_2)
        subtracao_2 = decimal.Decimal(numero_2) - decimal.Decimal(numero_1)
        print(f'A Subtração do numero 1 pelo numero 2 é: {subtracao}')
        print(f'A Subtração do numero 1 pelo numero 2 é: {subtracao_2}')
    elif operacao =='divisao':
        divisao = decimal.Decimal(numero_1)/decimal.Decimal(numero_2)
        divisao_2 = decimal.Decimal(numero_2)/decimal.Decimal(numero_1)
        print(f'A Divisão do numero 1 pelo numero 2 é: {divisao}')
        print(f'A Divisão do numero 2 pelo numero 1 é: {divisao_2}')
    elif operacao =='multip':
        multiplicacao = decimal.Decimal(numero_1)*decimal.Decimal(numero_2)
        print(f'A Multiplicação do numero 1 pelo numero 2 é: {multiplicacao}')
    elif operacao =='raiz':
        raiz = decimal.Decimal(numero_1)**(1/2)
        raiz_2 = decimal.Decimal(numero_2)**(1/2)
        print(raiz)
        print(raiz_2)
    elif operacao =='potencializacao':
        potencializacao = decimal.Decimal(numero_1)**decimal.Decimal(numero_2)
        potencializacao_2 = decimal.Decimal(numero_2)**decimal.Decimal(numero_1)
        print(f'A Potencialização do numero 1 pelo numero 2 é: {potencializacao,10}')
        print(f'A Potencialização do numero 2 pelo numero 1 é: {potencializacao_2}')
    elif operacao =='log':
        log = math.log(numero_1)
        log_2 = math.log(numero_2)
        print(f'O logaritimo do número 1 é {decimal.Decimal(log)}')
        print(f'O logaritimo do número 2 é {decimal.Decimal(log_2)}')
    elif operacao =='sin':
        seno = math.sin(numero_1)
        seno_2 = math.sin(numero_2)
        print(f'O Seno do número 1 é {decimal.Decimal(seno)}')
        print(f'O Seno do número 2 é {decimal.Decimal(seno_2)}')
    elif operacao =='cos':
        cos = math.cos(numero_1)
        cos_2 = math.cos(numero_2)
        print(f'O Cosseno do número 1 é {decimal.Decimal(cos)}')
        print(f'O Cosseno do numero 2 é {decimal.Decimal(cos_2)}')
    elif operacao == 'tan':
        tan = math.sin(numero_1)/math.cos(numero_1)
        tan_2 = math.sin(numero_2)/math.cos(numero_2)
        print(f'A Tangente do número 1 é {decimal.Decimal(tan)}')
        print(f'A Tangente do numero 2 é {decimal.Decimal(tan_2)}')
    else:
        print('Digite um operador válido!!')
    controle(controle)