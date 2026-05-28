# Exercício 1 - Variáveis e Funções

Crie um programa em Python que:

1. Solicite o nome do aluno.
2. Solicite duas notas.
3. Crie uma função chamada calcular_media().
4. A função deve retornar a média das notas.
5. Exiba:
- nome do aluno
- média calculada

aluno  = input ("digite o nome do aluno:")


def calcular_media (n1,n2):
  media = (n1 + n2 ) / 2 
  return calcular_media

n1 = float(input("DIgite a primeira nota: "))
n2 = float(input("digite a segunda nota:")) 
print(" a media do", aluno,"é: ", media(n1,n2))