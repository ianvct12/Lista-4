
numeros = []

quantidade = int(input("Quantos números deseja inserir? "))


for i in range(quantidade):
    numero = int(input(f"Digite o  número: "))
    numeros.append(numero)  


maior = numeros[0]
menor = numeros[0]


for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero


print("O maior número da lista é:", maior)
print("O menor número da lista é:", menor)
