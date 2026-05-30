alunos = []

def calcular_media(n1, n2, n3):
    
    media = (n1 + n2 + n3) 

    return media

    
def verificar_situacao(media):
    
    if media >= 18:
        return "Aprovado"
    
    elif media >= 12:
        return "Recuperação"
    else:
        return "Reprovado"
    
for i in range(5):

    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))

    media = calcular_media(nota1, nota2, nota3)

    situacao = verificar_situacao(media)

    alunos.append((nome, media, situacao))

#depois que os dados dos alunos foram coletados, exibe as informações

print("\nNome\tNota final\tSituação")
print("-" * 30)

for aluno in alunos:

    print(f"{aluno[0]}\t{aluno[1]:.2f}\t\t{aluno[2]}")

aprovados = 0
reprovados = 0
recuperacao = 0

notas = []

for aluno in alunos:
    notas.append(aluno[1])

    if aluno[2] == "Aprovado":
        aprovados += 1
    elif aluno[2] == "Reprovado":   
        reprovados += 1
    else:
        recuperacao += 1

maior_nota = max(notas)
menor_nota = min(notas)

media_turma = sum(notas) / len(notas)

print("\nEstatísticas da turma:")
print("-" * 30)

print(f"aprovados: {aprovados}")
print(f"reprovados: {reprovados}")
print(f"recuperação: {recuperacao}")
print(f"maior nota: {maior_nota:.2f}")
print(f"menor nota: {menor_nota:.2f}")
print(f"média da turma: {media_turma:.2f}")

def pesquisar_aluno(alunos, nome_procurado):

    for aluno in alunos:

        if aluno[0].lower() == nome_procurado.lower():

            print("\nAluno encontrado!")

            print(f"Nome: {aluno[0]}")
            print(f"Nota Final: {aluno[1]:.2f}")
            print(f"Situação: {aluno[2]}")

            return

    print("\nAluno não encontrado.")

nome_procurado = input("\nDigite o nome do aluno que deseja pesquisar: ")

pesquisar_aluno(alunos, nome_procurado)


    

