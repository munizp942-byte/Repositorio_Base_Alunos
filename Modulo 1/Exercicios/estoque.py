estoque={ "ferrari 488 GTB": [ 1000, 190.000],
          "Lamborghini": [ 500, 130.000],
          "porshe 911": [ 2001, 263.095],
          "mclaren 720s": [100, 336.000], 
          "aston martin vantage": [200, 191.000],
          "chevrolet corvette": [500, 310.990],
          "audi r8 v10": [100, 95.000],
          "nissan gt-r": [780, 222.885],
          "bmw m4": [560, 89.400],
          "mercedes amg gt r": [290, 199.900 ],
          "jaguar f type r": [1000, 200.900],
          "toyota gr supra": [340, 56.900], 
          "ford mustang": [100, 10.000],
          "dodge challenger srt": [400, 96.666],
          "rx7": [680, 243.000],
          "skyline r34": [190, 90.000],
          "maserati mc20": [590, 700.900],
          "lexus lc 500": [100, 20.000],
          "pagani huayra": [300, 70.000],
          "koenigsegg jesko": [100, 100.000],
          "bugatti chiron": [290, 60.000],
          "lotus evora gt": [340, 100.00]}
produto = input("Digite o produto selecionado: ")
quantidade = int(input("Digite a quantidade: "))
venda = [ [produto, quantidade] ]
total = 0
if produto in estoque:
    print("vendas:\n")
    for operacao in venda:
        produto, quantidade = operacao
        preço = estoque[produto][1]
        custo = preço * quantidade 
        print("%12s: %3d x %6.2f" %
        (produto, quantidade, preço, custo))
        estoque[produto][0] -= quantidade
        total+=custo
print(" custo total: %21.2f\n" % total)
print("estoque:\n")
