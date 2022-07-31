dicionario = {
    "carro": "c4",
    "fabricante": "citroen",
    "tabela_fipe": 35.000
}

print(dicionario)


keys = dicionario.keys()
print(keys)

print(dicionario["carro"])
print(dicionario.get("tabela_fipe"))
print(dicionario.values())
print(dicionario.items())

if "carro" in dicionario:
    print("Tem carro no dicionario")

if "c4" in dicionario:
    print("Tem c4 no dicionario")

vendedores_dicionario = {
    'Joao': 300,
    'Maria': 900,
    'Jose': 1000,
    'Henrique': 50,
    'Eloisa': 100
}
meta_vendas = 100
bonificacao = [vendedores_dicionario[item] * 0.2 if vendedores_dicionario[item]
               >= meta_vendas else 0 for item in vendedores_dicionario]
print(bonificacao)
