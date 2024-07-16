def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovado(media):
    return media < 6

def exibir_reprovados(dados_alunos, matriculas_reprovados):
    reprovados = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos[matricula]
        reprovados.append(
            f"Aluno Reprovado: {aluno['nome']} – Matrícula: {matricula} – Média Final: {aluno['media']:.2f}"
        )
    return reprovados

# Estrutura de dados para armazenar os dados dos alunos e as notas de cada bimestre
dados_alunos = {
    1001: {'nome': 'Alice', 'notas': [7, 8, 6, 9]},
    1002: {'nome': 'Bob', 'notas': [4, 5, 6, 5]},
    1003: {'nome': 'Carlos', 'notas': [9, 9, 10, 8]},
    1004: {'nome': 'Diana', 'notas': [2, 3, 4, 5]}
}

# Calculando a média de cada aluno
for matricula, dados in dados_alunos.items():
    media = calcular_media(dados['notas'])
    dados['media'] = media

# Verificando se o aluno foi reprovado
matriculas_reprovados = [matricula for matricula, dados in dados_alunos.items() if verificar_reprovado(dados['media'])]

# Identificando os alunos reprovados e imprimindo os dados
reprovados = exibir_reprovados(dados_alunos, matriculas_reprovados)
for reprovado in reprovados:
    print(reprovado)
