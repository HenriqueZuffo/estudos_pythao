thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


preco_produto = [200, 500, 385]
produtos = ['Vinho', 'Carne', 'Arroz']

produtos_precos = list(zip(preco_produto, produtos))
print(produtos_precos)


def calcular_imposto(preco, imposto):
    return preco * imposto


impostos_calculados = [calcular_imposto(
    preco, 0.5) for preco, _ in produtos_precos]

print(impostos_calculados)
