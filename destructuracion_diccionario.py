def sumar(a,b):
    return a+b

print(sumar(10,5))
print(sumar(a=10, b=5))
parametros = {
    'a': 10,
    'b': 5
}
print(sumar (**parametros))
print(sumar(**{'a': 10,'b': 5}))

def restar(**Kwargs):
    print(Kwargs)
print(restar(x=1,y=2,z=3))




























