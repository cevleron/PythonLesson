# Задача No49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не 
# учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий
# длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя 
# кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле 
# S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# print(*find_farthest_orbit(orbits))

# Вывод:
# 2.5 10

def find_farthest_orbit_1(list_of_orbits):  
    # Первый вариант решения
    func_list_orbits = list_of_orbits.copy()
    func_list_orbits = list(filter(lambda orbits: orbits[0] != orbits[1], func_list_orbits))
    s_orbits = tuple(map(lambda orbits: orbits[0]*orbits[1], func_list_orbits))
    max_orbits = max(s_orbits)
    index_max_s = s_orbits. index (max_orbits)
    return func_list_orbits[index_max_s]



    # Второй вариант решения
def find_farthest_orbit_2(list_of_orbits):
    s_orbita = {(orbita[0]*orbita[1]): orbita for orbita in list_of_orbits if orbita[0]!=orbita[1]}
    return s_orbita[max(s_orbita)]

def find_farthest_orbit_3(list_of_orbits):
    #                                                           тернарный оператор
    s_orbits = list(map(lambda orbits: orbits[0]*orbits[1] if orbits[0] != orbits[1] else 0, list_of_orbits)) 
    max_orbits = max(s_orbits)
    index_max_s = s_orbits.index(max_orbits)
    return list_of_orbits[index_max_s]



def find_farthest_orbit_4(list_of_orbits: list[tuple]):
    s_max = 0
    i_max = -1
    for i in range(len(list_of_orbits)):
        if list_of_orbits[i][0] != list_of_orbits[i][1]:
            s_item = list_of_orbits[i][0] * list_of_orbits[i][1]
            if s_item > s_max:
                i_max = i
                s_max = s_item
    return list_of_orbits[i_max]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# print(*find_farthest_orbit(orbits))

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit_1(orbits))
print(find_farthest_orbit_2(orbits))
print(find_farthest_orbit_3(orbits))
print(find_farthest_orbit_4(orbits))
