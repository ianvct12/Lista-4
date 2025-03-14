palavras = []

quantidade = int(input("Quantas palavras deseja inserir? "))

for i in range(quantidade):
    palavra = input(f"Digite a  palavra: ")
    palavras.append(palavra)  

for i in range(len(palavras)):
    palavras[i] = palavras[i][::-1] 


palavras.reverse()

print("Lista com palavras invertidas e em ordem reversa:", palavras)

#Explicação:

#O start e stop não foram definidos, então pegamos a string inteira.
#O step é -1, então a string é percorrida do final para o começo.

#Estrutura do fatiamento [start:stop:step]

#start: Índice inicial (padrão é o início da string).
#stop: Índice final (padrão é o final da string).
#step: Passo (se for -1, significa que vamos percorrer a string de trás para frente).