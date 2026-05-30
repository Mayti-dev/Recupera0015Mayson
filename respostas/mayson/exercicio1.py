numeros = []

for i in range(5):

    numero = float(input("Digite um número: "))

    numeros.append(numero)


def maior_numero(lista):

    return max(lista)


maior = maior_numero(numeros)

print(f"O maior número informado foi: {maior}")