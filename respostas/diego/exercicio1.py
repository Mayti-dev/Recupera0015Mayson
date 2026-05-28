aluno = input("Digite o nome do aluno: ")
n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) /2
    return media



media_calculada = calcular_media(nota1=n1, nota2=n2)

print(f"O aluno {aluno} obteve a seguinte média: {media_calculada}")
