meu_dicionario = {
    "codigo1": {"linguagem": "Python"},
    "codigo2": {"linguagem": "Java"},
    "codigo3": {"linguagem": "PHP"}
}
print(meu_dicionario)

print(type(meu_dicionario))

print(meu_dicionario.get("codigo1").get("linguagem"))

print(len(meu_dicionario))

dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}
print(dicionario_frutas)
