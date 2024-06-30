class Planta:
    def __init__(self, reino='Plantae', tipo=''):
        self.reino = reino
        self.tipo = tipo

    def fazer_fotossintese():
        return "Absorvendo raios solares..."
    
class Verdura(Planta):
    def __init__(self,nome,**kw):
        super().__init__(**kw)
        self.nome = nome
    def __str__(self):
        return (f'''
                Reino: {self.reino}, Nome: {self.nome},
                Tipo: {self.tipo},''')

class Animal:
    def __init__(self,reino='Animalia' ,pata=0):
        self.reino = reino
        self.pata = pata

    def fazer_som():
        return "Som de animal..."
    
#super para chamar as caracteristicas da classe pai
class Mamifero(Animal):
    def __init__(self, familia,raca, nome, cor_pelo, pelagem,classe='Mamífero', **kw):
        super().__init__(**kw)
        self.familia= familia
        self.raca = raca
        self.nome = nome
        self.pelagem = pelagem
        self.cor_pelo = cor_pelo
        self.classe= classe

    def __str__(self):
        return (f'''
                Reino: {self.reino}, Patas: {self.pata}, 
                Família: {self.familia}, Classe: {self.classe},
                Raça: {self.raca}, Nome: {self.nome},
                Pelagem: {self.pelagem}, Cor: {self.cor_pelo}''')
    
class Ave(Animal):
    def __init__(self, classe='Ave', pelagem='', cor='', voa= True,bota_ovo =True,**kw):
        super().__init__(**kw)
        self.classe = classe
        self.pelagem = pelagem
        self.cor = cor
        self.voa = voa
        self.bota_ovo = bota_ovo

class Ornitorrinco(Mamifero,Ave):
    def __init__(self, familia='', raca='', nome='', pelagem='', cor_pelo='', pata=0, bota_ovo=True, **kw):
        super().__init__(familia=familia, raca=raca, nome=nome, pelagem=pelagem, cor_pelo=cor_pelo, pata=pata, **kw)
        self.bota_ovo = bota_ovo

    def __str__(self):
        return (f'''
                Reino: {self.reino}, Família: {self.familia}, 
                Raça: {self.raca}, Nome: {self.nome},
                Classe: {self.classe},
                Patas: {self.pata}, Bota Ovo: {self.bota_ovo},
                Pelagem: {self.pelagem}, Cor: {self.cor_pelo}
                ''')


cao_1 = Mamifero(pata=int( input('Digite a quantidade de Patas: ')),familia=input('Digite a Família: '), raca=input('Digite a raça: '), nome=input('Digite o nome do animal: '), pelagem=input('Digite o tamanho da pelagem [curto\medio\longo]: '), cor_pelo=input('Digite a cor do pelo: '))
print(cao_1)
print(Animal.fazer_som())
print('\n\n\n')
verdura_1 = Verdura(nome= input('Digite o nome da planta: '), tipo= input('Digite o tipo da planta: '))
print(verdura_1)
print(Planta.fazer_fotossintese())
animal = Ornitorrinco(familia=input('Digite a Família: '),pata=int( input('Digite a quantidade de Patas: ')), raca=input('Digite a raça: '), nome=input('Digite o nome do animal: '),pelagem=input('Digite o tamanho da pelagem [curto\medio\longo]: '), cor_pelo=input('Digite a cor do pelo: '))
print(animal)