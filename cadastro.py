contidade = conthomem = contmulher = 0
while True:
    print('====== CADASTRO DE PESSOA ======')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
    if sexo not in ('F','M'):
        while sexo not in ('F','M'):
            sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
    if sexo in ('F','M'):
        if idade >= 18:
            contidade += 1
        elif sexo == 'M':
            conthomem += 1
        elif idade < 20 and sexo == 'F':
            contmulher += 1
    print('=' * 32)
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont not in ('S','N'):
        while cont not in ('S','N'):
            cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('=' * 43)
print(f'Possui {contidade} pessoa que possui mais de 18 anos.')
print(f'Possui {conthomem} homens.')
print(f'Possui {contmulher} mulher abaixo de 20 anos.')
print('=' * 43)
