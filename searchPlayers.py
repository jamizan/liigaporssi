aloitusbalanssi = 12
edellinenraja = 1
x = 1
LPP = 1
random = 0

if aloitusbalanssi < 0:
    aloitusbalanssi = aloitusbalanssi * -1
    random = -1

if aloitusbalanssi != 0:
    if aloitusbalanssi > 0:
        while x < aloitusbalanssi:
            print(f'x = {x}, LPP = {LPP}')
            if x == edellinenraja + 3:
                LPP += 1
                edellinenraja = x + 1
                

            x += 1

    if random < 0:
        LPP = LPP * -1

else:
    LPP = 0

print(f'LPP = {LPP}')