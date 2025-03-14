
numeros = []

quantidade = int(input("Quantos números deseja inserir? "))


for i in range(quantidade):
    numero = int(input(f"Digite o número: "))
    numeros.append(numero)  

soma = 0

for numero in numeros:
    soma += numero

print("A soma dos elementos da lista é:", soma)
