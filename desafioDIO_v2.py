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
from random import randint
import sys

extrato_1 = ""
saldo = 0
clientes = []
#login
def login():
    global clientes
    while True:
        opcao = int(input('\n\nVocê possui um cadastro? Sim [1]  |  Não[0]: '))
        if opcao == 1:
            nome = input('Digite seu usuário: ')
            user_encontrado = filtro_cliente_2(nome,clientes)
            if user_encontrado:
                menu(user_encontrado)
            else:
                print('@@@ Usuário não encontrado! retornando ao início @@@')
                return login()
        elif opcao == 0:
            print('Abrindo cadastro de cliente.')
            cliente(clientes)
        else:
            print('Digite um caracter válido!! ')
            return login()

#verifica se cliente já está cadastrado
def filtro_cliente(cpf,clientes):
    usuario_filtrado = [usuario for usuario in clientes if usuario["CPF"] == cpf ]
    return usuario_filtrado[0] if usuario_filtrado else None

def filtro_cliente_2(nome,clientes):
    usuario_filtrado = [usuario for usuario in clientes if usuario["Nome"] == nome ]
    return usuario_filtrado[0] if usuario_filtrado else None


##cadastro de clientes   
def cliente(clientes):
    cpf =input('Informe o seu CPF [SOMENTE NÚMEROS]')
    usuario = filtro_cliente(cpf,clientes)
    if usuario:
        print('@@@ Usuário já cadastrado com este CPF @@@')
        return
    nome = input('Digite seu nome completo: ')
    data_nascimento = input("Digite a data de nascimento. Números e dê espaço entre as datas [dd/mm/yy]: ")
    splitando_data = data_nascimento.split()
    data = '/'.join(splitando_data)
    endereco = []
    for i in range(5):
        logrado = input('Digite seu endereço no formato: [logradouro, numero da casa, bairro, cidade, sigla estado]: ')
    endereco.append(logrado)
    numero_conta = conta_corrente()
    clientes.append({'Nome': nome, 'Data_de_Nascimento': data, "CPF": cpf, "Endereço": endereco, "Numero_Da_Conta": numero_conta})
        
#gera numero de conta aleatório
def conta_corrente():
    numero_conta = ''
    i = 0
    while i < 10:
        numero = randint(0,9)
        numero_conta += str(numero)
        i += 1
    return numero_conta + '/' + '0001'

def menu(user): 
    print('********************')
    print(f"""
           Agência: {user["Numero_Da_Conta"]}
           Titular: {user['Nome']}
""")

    print('********************')
    print("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair
        [9] Cliente
        [7] Lista Clientes

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
    elif opcao == 7:
        mostra_cliente()
    else:
        print('Digite uma opção válida!!')
        menu(user)

def deposito(depositar,/):
    print('>>> Depósito <<<')
    print('\n')
    global extrato_1
    global saldo
    while True:
        depositar = float(input('Digite o quanto deseja depositar: '))
        if depositar > 0:
            saldo+= depositar
            print(f'Você depositou {depositar:.2f} , seu saldo atual é de {saldo:.2f}')
            extrato_1 += f'Depósito de R$ {depositar:.2f}\n'
            continuar = int(input('Deseja continuar? Digite [1] para SIM | [0] para NÃO\n'))
            if continuar == 1:
                continue
            elif continuar == 0:
                return menu(user)
            else:
                print('Digite uma  opção válida!!')
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
            continuar = int(input('Deseja continuar? Digite [1] para SIM | [0] para NÃO\n'))
            if continuar == 1:
                continue
            elif continuar == 0:
                print('Retornando ao Menu')
                return menu(user)
            else:
                print('Digite uma  opção válida!!')

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
        return menu(user)
    else:
        print('Digite uma opção válida!! ')


def mostra_cliente():
    global clientes
    print(clientes)

while True: 
    login()