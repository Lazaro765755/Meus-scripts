# Simulador de Rendimentos - Reserva de Emergência
print("--- SIMULADOR DE RENDIMENTOS ---")

# Entradas de dados
aporte = float(input("Valor total aportado (R$): "))
cdi_anual = float(input("Taxa do CDI anual (ex: 13.25): "))
meses = int(input("Quantidade de meses para simular: "))

# Cálculo da taxa mensal (Conversão de taxa anual para mensal)
# A fórmula correta de juros compostos para converter anual em mensal
taxa_mensal = ((1 + (cdi_anual / 100))**(1/12) - 1) * 100

print(f"\nTaxa mensal equivalente: {taxa_mensal:.4f}%")
print("-" * 30)

saldo = aporte
for mes in range(1, meses + 1):
    rendimento_mes = saldo * (taxa_mensal / 100)
    saldo += rendimento_mes
    print(f"Mês {mes}: Rendimento R$ {rendimento_mes:.2f} | Saldo Total: R$ {saldo:.2f}")

print("-" * 30)
lucro_total = saldo - aporte
print(f"RESULTADO FINAL após {meses} meses:")
print(f"Total Acumulado: R$ {saldo:.2f}")
print(f"Lucro Líquido: R$ {lucro_total:.2f}")

