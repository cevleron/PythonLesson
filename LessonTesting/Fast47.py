# Задача No47. Решение в группах
# У вас есть код, который вы не можете менять 
# (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
# а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Пример ввода и вывода данных представлены на следующем слайде 
 
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values)) 
# if values == transformed_values:
#    print(‘ok’) 
# else:
#    print(‘fail’)

# Вывод:
# ok


# transformation = lambda list_item:list_item
# values = [1,4,5,2,'adadf',3,12,True]
# result = list(map(lambda list_item:list_item,values))

# if result == values:
#     print('ok')
# else:
#     print('not ok')


# def kudr (num):
#   return num*num


result = [1, 5, 7, 3, 7]
# new_list = []
# for item in result:
#     new_list.append(kudr(item))


result = [1, 5, 7, 3, 7]
new_list_1 = list(map(lambda num: num*num, result))
#           что сделать   где взять     при каком условии
new_list_2 = [item*item for item in result if item > 4]
print (new_list_2)


result = [1, 5, 7, 3, 7]
new_list_1 = list(map(lambda num: num*num, result))
new_list_2 = [item*item for item in result ]
print (new_list_2)