Combustivel= input("Digite o tipo de combustivel: E: Etanol ou G:Gasolina")
Litros =float(input("Digite a quantidade de litros"))

if Combustivel == "E":

    total = Litros*4.90

elif Combustivel == "G":


    total = Litros*5.80


print(f"O valor total foi de:{total}")

