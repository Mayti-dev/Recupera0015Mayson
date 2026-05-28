def verificar_aprovacao(media):

    if media >= 60:
        return "Aprovado"

    elif media >= 40:
        return "Recuperação"

    else:
        return "Reprovado"


media = float(input("Digite a média do aluno: "))

resultado = verificar_aprovacao(media)

print(f"O aluno está: {resultado}")