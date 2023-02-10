# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

# def fibonacci(n):
#     if n in [1,2]:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(int(input())))

# def fibonacci(n):
#     if n ==0:
#         return 0
#     elif n in [1,2]:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# n=int(input('--> '))
# result = fibonacci(n)
# print(result)


# 2. Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# [4, 2, 2, 1, 5, 5]

# def replace_marks(nums):
#     minimum = min(nums) 
#     maximum = max(nums)
#     for i in range(len(nums)):
#         if nums[i] == maximum:
#             nums[i] = minimum
#     return nums



# list1 = []
# list2 = []


# # Тайпхинтинг
# def replace_marks(marks_list):
#     for i in range(len(marks_list)):
#         if(marks_list[i]==5)or (marks_list[i]==4):
#             marks_list[i] = 2
#     return marks_list



# marks= [4, 2, 2, 1, 5, 5]
# print(replace_marks(marks))


# def revers_nums(n):
#     if n==0:
#         return ''
#     k = input('--> ')
#     return k+revers_nums(n-1)


# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# def natural_num(num):
#     for i in range(2,num):
#         if num%i==0:
#             return True
        

n = int(input("Введите число: "))
def test(num):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(test(n))