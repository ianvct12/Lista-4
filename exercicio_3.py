
numeros = []


quantidade = int(input("Quantos números deseja inserir? "))


for i in range(quantidade):
    numero = int(input(f"Digite o número: "))
    numeros.append(numero)  


numeros_sem_duplicatas = []


for numero in numeros:
    if numero not in numeros_sem_duplicatas:
        numeros_sem_duplicatas.append(numero)

print("Lista sem números repetidos:", numeros_sem_duplicatas)
