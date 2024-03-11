#Criar um sistema de banco, de depósito, saque e extrato
#depósito somente valores positivos
#todo deposito devem mostrar no extrato
#saque 3 diários, com valor maximo de 500 reais
#caso não esteja com saldo, deverá mostrar mensagem de saldo insuficiente
#todo saque deve ser mostrado no extrato
#extrato deve listar todos os saques e dep e deve mostrar o saldo atual

menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        Escolha a operação desejada: """
saldo = 0
limite = 500
extrato =""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao =='d':
        print('Depósito: ')
        deposito = float(input('Digite o quanto deseja depositar: '))
        if deposito > 0:
            saldo += deposito
            print(f'Você depositou {deposito} , seu saldo atual é de {saldo}')
            extrato += f'Depósito de R$ {deposito} \n'
        else:
            print('Não é possível depositar valores abaixo ou iguais a ZERO')
    elif opcao =='s':
        print('Sacar: ')
        saque = float(input('Digite o valor do saque da sua conta: '))
        if saldo < saque:
            print(f'Saldo insuficiente. Seu saldo atual é de {saldo}')
        elif saque > 0 and saque <= 500:
            saldo -= saque
            if numero_saque == LIMITE_SAQUE:
                print('Você atingiu o limite de saque diário... Operação inválida')
            else:
                print(f'Você sacou {saque} e seu saldo atual é de {saldo}')
                extrato += f'Saque de R$ {saque} \n'
            numero_saque +=1
        elif saque > 500:
            print('Limite de saque é de R$ 500.00')
        else:
            print('Digite um valor válido')
            
    elif opcao == 'e':
        print(extrato)
        print(f'Seu saldo atual é de {saldo}')
        if extrato == '':
            print('Você não realizou nenhuma operação hoje.')
    elif opcao == 'q':
        print('Saindo da conta...')
        break
    else:
        print('Digite uma opção válida')