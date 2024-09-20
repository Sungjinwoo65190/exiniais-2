salario_atual = float(input('Informe o salario: R$ '))
percentual_aumento = float(input('Informe o percentual de aumento: '))

novo_salario = salario_atual + (salario_atual * (percentual_aumento / 100))

print(f"O novo salario é: E$ {novo_salario:.2f}")