def aumentar(n=0, t=0, f=False):
    a = n + n * t / 100
    return a if f is False else moeda(a)

def diminuir(n=0, t=0, f=False):
    d = n - n * t / 100
    return d if f is False else moeda(d)

def dobro(n=0, f=False):
    d = n * 2
    return d if f is False else moeda(d)

def metade(n=0, f=False):
    m = n / 2
    return m if f is False else moeda(m)


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


def resumo(n=0, a=10, d=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço:":<20}{moeda(n):>10}')
    print(f'{"Dobro:":<20}{dobro(n, True):>10}')
    print(f'{"Metade:":<20}{metade(n, True):>10}')
    print(f'Com {a}% de aumento: {aumentar(n, a, True):>10}')
    print(f'Com {d}% de redução:  {diminuir(n, d, True):>10}')
