import random
def birthday(i):
    b=0
    a = [0, 1, 0]
    for z in range(0,i):
        if random.choice(a)==1:
            b=b+1
    print ('Вероятность победить если не менять выбор равна',b*100/i,'%')
birthday(int(input()))

