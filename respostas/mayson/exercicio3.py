numeros =[]

for i in range(5):

    numero = int(input("Digite um número inteiro: "))

    numeros.append(numero)

def maior_numero(lista):

    return max(lista)

maior = maior_numero(numeros)

print(f"O maior número digitado é: {maior}")
