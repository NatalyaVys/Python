 #Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3
# -> 1

N = int(input('Введите количество элементов списка А: '))
elements_spiska = input("Введите через пробел элементы списка: ").split()
A = list(map(int, elements_spiska))
if len(A) != N:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, которое необходимо найти в списке: '))
    k = 0
    for i in range(N):
        if A[i] == X:
            k += 1
    print(f'Число {X} встречается в списке A: {k} раз(а)') 
    
   