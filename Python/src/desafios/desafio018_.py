quantoGanha = float(input('quanto você ganha por hora? '))
quantasHorasDeTrabalho = float(input('quantas horas trabalhadas no mês? '))

salarioBruto = quantasHorasDeTrabalho * quantoGanha

inss = salarioBruto *  0.11
sindicado = salarioBruto * 0.05
ir = salarioBruto * 0.08
salarioLiquido = ir - sindicado - inss - salarioBruto

print(f"seu salario bruto é = R${salarioBruto}")
print(f"seu pagamento ao sindicado é = R${sindicado}")
print(f"seu pagamento ao importo de renda é = R${ir}")
print(f"seu pagamento ao inss é = R${inss}")
print(f"seu salario liquido é = R${salarioLiquido}")


