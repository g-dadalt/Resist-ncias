resistencia1 = float(input("insira o valor da Resistência 1: "))
resistencia2 = float(input("insira o valor da Resistência 2: "))
resistencia3 = float(input("insira o valor da Resistência 3: "))
valorSerie = resistencia1 + resistencia2 + resistencia3
valorParalelo = 1/((1/resistencia1) + (1/resistencia2) + (1/resistencia3))
if not (resistencia1<0 or resistencia2<0 or resistencia3<0):
    print(valorSerie)
    print("%.2f" %valorParalelo)
else:
    print("Resistencia(s) inválida(s)")