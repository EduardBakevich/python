count = int(input('Введите количество монет: '))
side1 = 0
side2 = 0
for _ in range(count):
    side = int(input('Если монета лежит орлом вверх, то введите 0, если — вниз, то 1: '))
    if side%2 == 0:
        side1 += 1
    else:
        side2 += 1
if side1>=side2:
    print(f'наименьшее число монет, которые нужно переложить — {side1}')
else:
    print(f'наименьшее число монет, которые нужно переложить — {side2}')