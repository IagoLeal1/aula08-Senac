aluno = {
    "Nome": 'Maria',
    "Idade": 29,
    "Curso": 'Análise de Dados',
}

print(aluno)
print(aluno['Nome'])

aluno['Nome'] = 'Pedro'
print(aluno)

aluno["E-mail"] = 'pedro@gmail.com'
print(aluno)

aluno.pop("E-mail")
print(aluno)

if 'E-mail' in aluno:
    aluno.pop('E-mail')
print(aluno)

# aluno.clear()
# print(aluno)

# del aluno
# print(aluno)

for chave, valor in aluno.items():
    print(chave, valor)