# 1. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# 3! = 1 * 2 * 3

n = int (input ('Введите число: '))
f = 1
while n > 0:
    f = f*n
    n -= 1
print (f)
