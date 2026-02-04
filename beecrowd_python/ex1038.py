item, quant = map(int, input().split())

if item == 1:
    valor = 4.00*quant
elif item == 2:
    valor = 4.50*quant
elif item == 3:
    valor = 5.00*quant
elif item == 4:
    valor = 2.00*quant
elif item == 5:
    valor = 1.50*quant
else:
    valor = 0

    print(f"Total: R$ {valor:.2f}")