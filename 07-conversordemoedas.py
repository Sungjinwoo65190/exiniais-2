real = float(input('quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.43 
euro = real / 6.06
print('Com R${:.2f} você pode comprar U${:.2f}' .format(real,dolar))
print('Com R${:.2f} você pode comprar €{:.2f}' .format(real,euro))