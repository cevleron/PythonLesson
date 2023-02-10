# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1234 5
# 6 -> 5

n = int(input("Введите количество элементов в массиве: "))
num_list = []
for i in range (n):
    num = int(input("Введите num "))
    num_list.append(num)
print(num_list)

x = int(input("Введите число Х что бы узнать сколько значений ближайших к нему встречается в массиве: "))
min = abs(num_list[0]-x)
max = abs(num_list[0]+x)
for i in range(n):
    if num_list(num)<min:
        min = num_list[num]
    print (min)


# num_list.append(x)
# print(num_list)
# num_list.sort()
# print(num_list)

# for i in range(len(num_list)):



#     print(i)