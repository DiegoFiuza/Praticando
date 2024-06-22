'''
 Solicitar um cadastro de usuario.
 Depois solicitar login e validar entrada com senha
'''
import time
import re

users_data = {}
usuario = ''
senha = ''
def new_user():
    global users_data
    global usuario
    global senha
    reg = {}
    reg.setdefault('Username', input('Digite seu nome de usuário: '))
    usuario = reg['Username']
    while True:
        password = input('''
                        >>> Regras da criação de senha <<< 
                            - Possuir 10 caracteres
                            - Mínimo 1 letra maiúscula
                            - Mínimo 1 letra minúscula
                            - Mínimo 1 número
                            - Sem caracter especial
                     
                        >>> Crie sua senha <<< \n\n
                     ''')
        if len(password) < 10 or re.search(r'\W',password) or len(password) > 10:
            if not password.isupper() or password.islower() or password.isalnum():
                time.sleep(2)
                print("Senha inválida! Digite novamente")
        else:
            break
    reg.setdefault('Senha', password)
    senha = reg['Senha']
    users_data.update(reg)
    time.sleep(2)
    return homepage()

#validar login
def login():
    global users_data
    global usuario
    global senha
    username = input('Digite seu usuário no sistema: \n\n')
    if username != usuario:
       print('Usuário não existe!')
       opcao = input('Deseja criar cadastro? [ s/n ]')
       opcao.lower()
       if opcao == 's':
            new_user()
            return login()
       elif opcao == 'n':
            return login()
       
    password = input('Digite sua senha: \n\n')
    if username == usuario and password == senha:
        time.sleep(1)
        print('Login bem sucedido!!')
        print('\n\n\n')
        time.sleep(2)
        print(f'Bem-Vindo {username.capitalize()}!!')
    elif username == usuario and password != senha:
        print('Senha incorreta')
        while password != senha:
            password = input('Digite Novamente a sua senha: ')
        time.sleep(1)
        print('Login bem sucedido!!')
        print('\n\n\n')
        time.sleep(2)
        print(f'Bem-Vindo {username.capitalize()}!!')

#página inicial
def homepage():
    print('''
         >>>     WELCOME!!!     <<<
''')
    opcao = int(input("""
             --- Digite 1 para realizar login --- \n\n
             --- Digite 2 para sign up --- \n\n Digite: """))
    if opcao == 1:
        login()
    elif opcao == 2:
        new_user()
    else:
        print('Digite uma opção válida!!\n\n')
        return homepage()
    
homepage()