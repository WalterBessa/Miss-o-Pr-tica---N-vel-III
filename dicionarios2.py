meu_dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}
print(meu_dicionario)

meu_dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'brasileiro'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'portuguesa'}
})
print(meu_dicionario)

copia_dicionario = meu_dicionario.copy()
print(copia_dicionario)

removido = meu_dicionario.pop(2)
print(removido)
print(meu_dicionario)

ultimo_removido = meu_dicionario.popitem()
print(ultimo_removido)
print(meu_dicionario)

meu_dicionario.clear()
copia_dicionario.clear()
print(meu_dicionario)
print(copia_dicionario)

chaves = ['a', 'b', 'c']
novo_dicionario = dict.fromkeys(chaves, 'valor_padrao')
print(novo_dicionario)

print(novo_dicionario.items())
print(novo_dicionario.keys())
print(novo_dicionario.values())
