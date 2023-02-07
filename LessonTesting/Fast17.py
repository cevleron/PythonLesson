# # Множества
# my_set = {1,2,3,4}
# my_set.add(5)
# my_set.remove(1)
# print(my_set)

# # Словарь
# my_dict = {
#     1:'Oleg',
#     2:'Misha'
# }
# # Добавление в словарь ключа
# my_dict[3] = 'Mishka'


# Задача 17.
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 3, 4, 4]
# Output: 6

# my_list = [1, 1, 2, 3, 4, 4]
# my_list_1 = set(my_list)
# print(f'Уникальных элементов: {len(my_list_1)}')


# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Первое решение
# staert_list = [1, 2, 3, 4, 5]
# num = 50
# k = num%len(staert_list)
# staert_list_temp = [0]*len(staert_list)

# for i in range(len(staert_list)):
#     if (i+k)>= len(staert_list):
#         staert_list_temp[i+k-len(staert_list)]=staert_list[i]
#     else:
#         staert_list_temp[i+k] = staert_list[i]
# print(staert_list_temp)


# Второе решение
# start_list = [1,2,3,4,5]
# k = int(input('Enter K: '))
# k = k%len(start_list)
# result_list = [0,0,0,0,0]
# i=0
# while i<len(start_list):
#     if (i+k) >= len(start_list) -1:
#         result_list[i+k-len(start_list)] = start_list[i]
#     else:
#         result_list[i+k]=start_list[i]
#     i+=1
# print(result_list)

# Третье решение
# k=2
# start_list=[1,2,3,4]
# new_list=[]

# k=-(k%len(start_list))
# for i in start_list:
#     new_list.append(start_list[k])
#     k+=1
# print(new_list)


# Напишите программу для печати всех уникальных значений в словаре.
# {
#     1:'Vlad',
#     2:'Vlad',
#     3:'Oleg'
# }
# -> 2

# my_dict = {
#     1:'Vlad',
#     2:'Vlad',
#     3:'Oleg'
# }
# my_set = set()
# for i in my_dict.values():
#     my_set.add(i)
# print(my_set)

# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: start_list = [3,7,1,7,1,4,9]
# Output: 4

start_list = [3,7,1,7,1,4,9]
count = 0
for i in range(len(start_list)-1):
    if (start_list[i] < start_list[i+1]):
        count+=1
print(count)

    