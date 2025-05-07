produto = {
    'Nome': 'Notebook',
    'Preco': 3500.00,
    'Estoque': 15,
}

if 'Estoque' in produto:
    produto.pop('Estoque')

produto['Preco'] = 4000.00

print(f"{produto['Nome']}: R${produto['Preco']}")