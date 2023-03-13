
#Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Количество долек шоколодки в длину (n): \n'))
m = int(input('Количество долек шоколадки в ширину (m): \n'))
k = int(input('Количество долек в отломленном кусочке (k): \n'))
if k < m*n and (k % m == 0 or k % n == 0):
    print(f'да, можно отломить, {k} долек')
else:
    print(f'нет, нельзя отломить, {k} долек')