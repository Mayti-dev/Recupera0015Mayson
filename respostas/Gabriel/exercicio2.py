aluno = input("digite o nome do aluno:")
n1 = float (input("digite a primeira nota do aluno:"))
n2 = float (input("Digite a segunda nota do aluno:"))

def calcular_media(nota1,nota2):
    return (nota1 + nota2) / 2

print (f"O aluno {aluno} obteve a seguinte média: {calcular_media(n1,n2)}")


