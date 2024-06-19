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
                            - Mínimo 10 caracteres
                            - Mínimo 1 letra maiúscula
                            - Mínimo 1 letra minúscula
                            - Mínimo 1 número
                            - Sem caracter especial
                     
                        >>> Crie sua senha <<< \n\n
                     ''')
        if len(password) < 10 or re.search(r'\W',password):
            print('Senha inválida! Digite novamente')
        else:
            break
    reg.setdefault('Senha', password)
    senha = reg['Senha']
    users_data.update(reg)
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
        time.sleep(5)
        print('Login bem sucedido!!')
        time.sleep(10)
        print(f'Bem-Vindo {username}!!')
    elif username == usuario and password != senha:
        print('Senha incorreta')
        while password != senha:
            return login(password(input('Digite novamente a sua senha: ')))
#página inicial
def homepage():
    print('''
         >>>     WELCOME!!!     <<<
''')
    time.sleep(5)
    opcao = input("""
             --- Digite login para entrar com usuário e senha --- \n\n
             --- Digite sign in para criar cadastro --- \n\n:
""")
    opcao = opcao.lower()
    if opcao == "login":
        login()
    elif opcao == "sign in":
        new_user()
    else:
        print('Digite uma opção válida!!\n\n')
        return homepage()
    
homepage()