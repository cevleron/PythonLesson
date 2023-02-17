# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.
# Ввод:                Ввод:
# 5                    5
# 1 2 3 4 5            1 5 1 5 1
# Вывод:               Вывод:
# 0                    2

def list_init(el_count):
    result_list=[]
    for i in range(el_count):
        num = int(input("Введите num "))
        result_list.append(num)
    return result_list
n = int(input("Введите число N: "))
list = list_init(n)
print(list)

count = 0
for i in range(1,len(list)-1):
    if list[i-1]<list[i]>list[i+1]:
        count+=1
print(count)