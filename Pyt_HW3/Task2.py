#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
#*Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5


N = int(input('ведите количество элементов списка А: '))
elements_spiska = input("Введите через пробел элементы списка: ").split()
A = list(map(int, elements_spiska))
if len(A) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = X - A[0]
    index = 0
    for i in range(1, N):
        count = X - A[i]
        if count < min:
            min = count
            index = i
    print(f'Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}')
    