def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler)
print(mytripler)

print(mydoubler(11))
print(mytripler(11))


def teste(a):
    return lambda c: c + a


def teste_lambda(a, b): return a + b


print(teste(4)(3))
print(teste_lambda(1, 2))


names = ['Shivani', 'Jason', 'Yusef', 'Sakura']
greeted_names = map(lambda x: 'Hi ' + x, names)

print(greeted_names)
for name in greeted_names:
    print(name)
