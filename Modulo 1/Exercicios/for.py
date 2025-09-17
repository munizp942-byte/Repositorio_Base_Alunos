'''L=[8,9,15]
for e in L:
    print(e)


L=["chocolate", "volei", "altinha", "manga", "dancar", "familia", "piercings", "preto", "celular", "melão"]
for s in L:
    for letra in s:
        print(letra)
'''

L=[1,7,2,4]
máximo=L[0]
for e in L:
    if e > máximo:
        máximo = e
print(máximo)
  
L=[1,7,2,4]
mínimo=L[0]
for e in L:
    if e < mínimo:
        mínimo = e
print(mínimo)

for v in range(10):
    print(v)

for v in range(5, 8):
    print(v)

for t in range(50,50000,160):
    print(t, end=" ")

nome = "pyetra muniz"
idade = 16 
grana = 50000
print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))



