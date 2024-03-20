#Criar um sistema de banco, de depósito, saque e extrato
#depósito somente valores positivos
#todo deposito devem mostrar no extrato
#saque 3 diários, com valor maximo de 500 reais
#caso não esteja com saldo, deverá mostrar mensagem de saldo insuficiente
#todo saque deve ser mostrado no extrato
#extrato deve listar todos os saques e dep e deve mostrar o saldo atual
#criar duas funções de cadastrar cliente
#cadastrar conta corrente
#saque keyword only
#dep positional only
# extrato positional only e keyword only
#função usuario(cliente): nome, data nasc, cpf e endereço(logradouro, nmro,bairro,cidade,sigla estado). Usuário cpf diferente
#conta corrente em lista deve conter agencia, nmro conta e usuário(nmro da conta inicia em 1 e agencia fixo em 0001)
import random
import sys

extrato_1 = ""
saldo = 0
clientes = {}
usuario = ''
conta = ''
#login
def login():
    global usuario
    global clientes
    opcao = int(input('\n\nVocê possui um cadastro? Sim [1]  |  Não[0]: '))
    if opcao == 1:
        user = input('Digite seu usuário: ')
        if user == usuario:
            print(f'Bem Vindo!!!\n\n  User: {user}')
            menu()
        else:
            print('Você não possui cadastro, indo à novo cadastro de cliente.')
            cliente()
    elif opcao == 0:
        print('Você não possui cadastro, indo à novo cadastro de cliente.')
        cliente()
    else:
        print('Digite um caracter válido!! ')
        return login()


##consulta os clientes já criados
def cadastros():
    global clientes
    print('Possui cadastro? [s | n] ')
    resposta = input()
    if resposta.lower() == 's':
        print(clientes)
    elif resposta.lower() == 'n':
        return cliente()
    else:
        print('Digite um caracter válido!! ')

##cadastro de clientes   
def cliente():
    cliente = {}
    global clientes
    global usuario
    clientes ={}
    while True:
        cliente.setdefault("Nome",input('Digite seu nome: ')) 
        data_nascimento = input("Digite a data de nascimento. Números e dê espaço entre as datas [dd/mm/yy]: ")
        splitando_data = data_nascimento.split()
        data = '/'.join(splitando_data)
        cliente.setdefault("Data de Nascimento", data) 
        cliente.setdefault("CPF",input('Digite seu CPF [separando com "." e com "-"]: '))
        if cliente['CPF'] in clientes.keys():
            print('CPF em uso')
        else:
            endereco = []
            for i in range(5):
                logrado = input('Digite seu endereço no formato: [logradouro, numero da casa, bairro, cidade, sigla estado]: ')
                endereco.append(logrado)
            cliente.setdefault("Endereço",endereco)
            usuario = cliente['Nome']
            conta_corrente()
            clientes.update(cliente)
        break
#gera numero de conta aleatório
def conta_corrente():
    numero_conta = ''
    global conta
    agencia = '0001'
    for i in range(9):
        numero = '0123456789'
        pegar_numero = random.choice(numero)
        numero_conta += pegar_numero
    conta = numero_conta + '/' +"0001"

def menu(): 
    global usuario
    global conta
    print('********************')
    print(usuario)
    print('********************')
    print(conta)
    print("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair
        [9] Cliente

        Escolha a operação desejada: """, end=" ")
    opcao = int(input())
    if opcao == 1:
        deposito(0)
    elif opcao == 2:
        saque(sacar = 0)
    elif opcao == 3:
        extrato()
    elif opcao == 0:
        sys.exit('Saindo...')
    elif opcao == 9:
        cadastros()

def deposito(depositar,/):
    print('>>> Depósito <<<')
    print('\n')
    global extrato_1
    global saldo
    continuar = 's'
    while continuar !='n':
        depositar = float(input('Digite o quanto deseja depositar: '))
        if depositar > 0:
            saldo+= depositar
            print(f'Você depositou {depositar:.2f} , seu saldo atual é de {saldo:.2f}')
            extrato_1 += f'Depósito de R$ {depositar:.2f}\n'
            continuar = input('Deseja continuar? Digite [s] caso deseje.\n')
            if continuar.lower() == 's':
                continue
            else:
                return menu()
        else:
            print('Não é possível depositar valores abaixo ou iguais a ZERO')

def saque(*,sacar):
    global saldo
    global extrato_1
    numero_saque = 0
    LIMITE_SAQUE = 3
    print('>>> Saque <<<')
    print("\n")
    while numero_saque < LIMITE_SAQUE:
        sacar = float(input('Digite o quanto deseja Sacar: '))
        if sacar > saldo:
            print(f'Saldo insuficiente. Seu saldo atual é de {saldo:.2f}')
        elif sacar > 0 and sacar <= 500:
            saldo -= sacar
            print(f'Você sacou {sacar:.2f} e seu saldo atual é de {saldo:.2f}')
            extrato_1 += f'Saque de R$ {sacar:.2f}\n'
            numero_saque +=1
            continuar = input('Deseja continuar? Digite [s] caso deseje.\n')
            if continuar.lower() == 's':
                continue
            else:
                print('Retornando ao Menu')
                return menu()
        elif sacar > 500:
            print("Digite um valor válido. Limite de saque é de R$ 500.00")
    print('Você atingiu o limite de saque diário...')
    print('Retornando ao Menu')
    menu()
    
def extrato():
    print('\n*************** EXTRATO ***************\n')
    global extrato_1
    print(extrato_1)
    if extrato_1 == '':
        print('Você não realizou nenhuma operação hoje.')
    print('\n\n')
    print(f'Seu saldo atual é de R$ {saldo:.2f}\n')
    print('\n****************************************')
    print('\n\n')
    opcao = int(input('Continuar no Extrato [1] || Retornar ao Menu[0]'))
    if opcao == 1:
        return extrato()
    elif opcao == 0:
        return menu()
    else:
        print('Digite uma opção válida!! ')


while True: 
    login()