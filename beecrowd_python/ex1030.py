import time
quant = 30
cont = 0
c = 1
while True:
    c = c*3
    print(f"É a vez da {c}° pessoa")
    cont +=1
    if cont==quant:
        break