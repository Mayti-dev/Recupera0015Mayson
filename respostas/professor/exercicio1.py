# Declaração de variáveis
aluno = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Declaração da função
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

# Invocando a função
media_calculada = calcular_media(nota1=n1, nota2=n2)

# Mostrando o resultado
print(f"O aluno {aluno} obteve a seguinte média: {media_calculada}")
