class Pessoa:

        olhos = 2
        def __init__(self, *filhos, nome=None, idade=26):
                self.idade = idade
                self.nome = nome
                self.filhos = list(filhos)
        def cumprimentar(self):
            return f'Olá {id(self)}'

if __name__ == '__main__':
        Pereira = Pessoa(nome='Pereira')
        Martinho = Pessoa (Pereira, nome='Martinho')
        print(Pessoa.cumprimentar(Martinho))
        print(id(Martinho))
        print (Martinho.cumprimentar())
        print(Martinho.nome)
        print(Martinho.idade)
        for filho in Martinho.filhos:
                print(filho.nome)
        Martinho.sobrenome = 'Eduardo'
        del Martinho.filhos
        Martinho.olhos = 1
        del Martinho.olhos
        print(Martinho.__dict__)
        print(Pereira.__dict__)
        Pessoa.olhos = 3
        print(Pessoa.olhos)
        print(Martinho.olhos)
        print(Pereira.olhos)
        print(id(Pessoa.olhos)), id(Martinho.olhos), id(Pereira.olhos)