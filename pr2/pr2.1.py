import random
j=0
a = int(input('Введите количество человек: '))
p = int((a*(a-1))/2)
print ('Количество пар: ', p)
for n in range (0, 10000):
    for i in range(p):
        d=random.randint(1, 365)
        if d==1:
            j=j+1
            break
print ('Вероятность того, что в группе есть совпадения дней рождения равна',j/100,'%')