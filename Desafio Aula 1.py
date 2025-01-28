vNome = input('Digite seu nome: ')
vSalario = float(input('Digite o valor do seu salário: '))
vBonusPorcentagem = float(input('Digite o valor do bônus (de 0 a 100): '))
vBonusTotal = 1000 + vSalario * vBonusPorcentagem/100

print (f'Olá {vNome}! seu salário é de  {vSalario} e seu bônus é de {vBonusTotal}')