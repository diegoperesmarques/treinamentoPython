real = float (input('Quanto dinheiro você tem na carteira? R$: '))
dolar = real / 3.27
print('Com R${:2f} você pode comprar UR${:.2f}'.format(real, dolar))