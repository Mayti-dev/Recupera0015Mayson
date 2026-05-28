aluno  = input ("digite o nome do aluno:")
n1 = float(input("DIgite a primeira nota: "))
n2 = float(input("digite a segunda nota:")) 

def calcular_media (n1,n2):
  media = (n1 + n2 ) / 2 
  return media 


mediacalculada = calcular_media(n1,n2)

print(f"a media do, {aluno},é: ,{mediacalculada}")