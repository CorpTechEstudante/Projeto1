contotal = contpreço = barato = contador = 0
maisbarato = ''
while True:
    print('='*30)
    nome = str(input('Digite o nome do produto: ')).strip()
    valor = float(input('Digite o preço do produto: '))
    contotal += valor
    contador += 1
    if valor > 1000:
        contpreço += 1
    if contador == 1:
        barato = valor
        maisbarato = nome
    else:
        if barato > valor:
            barato = valor
            maisbarato = nome
    if contador >= 2:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar not in ('S','N'):
            while continuar not in ('S','N'):
                continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
print('='*50)
print(f'O valor total dos produtos deu: R${contotal:.2f}')
print(f'Possui {contpreço} produto com valor acima de R$1000,00')
print(f'O {maisbarato} foi o produto mais barato custando apenas R${barato:.2f}')
print('='*50)
