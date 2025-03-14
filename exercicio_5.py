numeros = []

quantidade = int(input("Quantos números deseja inserir? "))

for i in range(quantidade):
    numero = int(input(f"Digite o número: "))
    numeros.append(numero) 

numero_procurado = int(input("Digite o número que deseja contar: "))

contador = 0

for numero in numeros:
    if numero == numero_procurado:
        contador += 1

print(f"O número {numero_procurado} aparece {contador} vezes na lista.")
