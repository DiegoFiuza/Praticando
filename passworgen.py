#precisa ter 10 caracteres
# 1 letra maiúscula
#1 minuscula
#caracter especial
#1 numero pelo menos
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password =''.join(random.choice(caracteres) for i in range(tamanho))
    return password

password_size = 10
new_password = gerar_senha(password_size)
print(new_password)