class Contato:
    def __init__(self, nome, telefone,email,endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

novo_contato = []

def criar_contato():
    global novo_contato
    while True:
        opcao = int(input('Deseja adicionar novo, contato? Sim[1] | Não[0]'))
        if opcao == 1:
            Contato.nome = input('Digite o nome completo do contato:')
            Contato.telefone = int(input('Digite o número de telefone: '))
            Contato.email = input('Digite o email do contato: ')
            Contato.endereco = input('Digite seu endereço no formato: [logradouro, numero da casa e complemento[caso tenha], bairro, cidade, sigla estado]: ')
            novo_contato.append({'Nome': Contato.nome, 'Telefone': Contato.telefone, "Email": Contato.email, "Endereço": Contato.endereco})
        elif opcao == 0:
            print(novo_contato)
        else:
            break

criar_contato()