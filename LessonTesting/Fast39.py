# Задача No39.
# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)


def list_init(el_count):
    # n=(int(input("Введите число N элементов: ")))
    result_list=[]
    # num_list_1=[]
    for i in range(el_count):
        num = int(input("Введите num "))
        result_list.append(num)
    return result_list

n = int(input("Введите число N: "))
m = int(input("Введите число M: "))
first_list = list_init(n)
second_list = list_init(m)
result = []
for item in first_list:
    if item not in second_list:
        result.append(item)
print(result)

