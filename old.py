"""
TODO Оптимизировать рассчеты. Добавить рекурсию. Добавить обработку альтернативного пути.
Алгоритм высчитывает кротчайшее расстояние из точки СТАРТ до всех непройденных, после возвращается в первую точку.
Формирует общий путь из таких векторов.
в ходе тестирования с количеством точек более 20-ти. обнаружила погрешность вычислений. Метод грубой силы находит
более короткий путь, чем мой скрипт. Есть идеи, как это исправить без метода грубой  силы. Так же алгоритм не
обрабатывает альтернативные варианты.
"""


list_of_best_ways = []
dict_of_points = {"point_1": (0, 2),
                  "point_2": (2, 5),
                  "point_3": (5, 2),
                  "point_4": (6, 6),
                  "point_5": (8, 3),
                  }


def calculate_way(*args):
    """
    args - новые стартовые координаты х, у, от которых считаем самый короткий путь к оставшимся точкам в списке входных
    данных.
    Если список пустой - выходим из рекурсии
    Если список не пустой, по формуле высчитываем самый короткий путь до оставшихся точек в списке.
    Формируется временный список, в котором происходит сравнение полученных рассчетов.
    Результат - минимальное значение, добавляется в общий словарь. Ключем являются координаты, значением -
    минимальный путь из последней точки до оставшихся на карте.
    Возвращает вызов функции work_with_dicts(), передавая параметры( ключ и координаты следующей точки)
    """

    if not dict_of_points:
        point_x, point_y = list_of_best_ways[0][0], list_of_best_ways[0][1]
        some_distance = ((point_x - args[0]) ** 2 + (point_y - args[1]) ** 2) ** 0.5
        list_of_best_ways.append(list_of_best_ways[0])
        list_of_best_ways.append(some_distance)
        return

    dict_of_distance = dict()

    for keys in dict_of_points:
        point_x, point_y = dict_of_points.get(keys)[0], dict_of_points.get(keys)[1]
        some_distance = ((point_x - args[0]) ** 2 + (point_y - args[1]) ** 2) ** 0.5
        dict_of_distance.update({keys: some_distance})

    for key, value in dict_of_distance.items():
        if len(dict_of_distance.keys()) > 1:
            if value != min(*(dict_of_distance.values())):
                pass
            else:
                list_of_best_ways.append(dict_of_points.get(key))
                list_of_best_ways.append(min(*(dict_of_distance.values())))
                point_x, point_y = dict_of_points.get(key)
                return work_with_dicts(key, point_x, point_y)
        else:
            list_of_best_ways.append(dict_of_points.get(key))
            list_of_best_ways.append(*(dict_of_distance.values()))
            point_x, point_y = dict_of_points.get(key)
            return work_with_dicts(key, point_x, point_y)


def work_with_dicts(key=[*(dict_of_points.keys())][0],
                    point_x=(dict_of_points.get([*(dict_of_points.keys())][0]))[0],
                    point_y=(dict_of_points.get([*(dict_of_points.keys())][0]))[1]):
    """
    Аргументы по умолчанию берем из словаря входных данных. В процессе работы, аргументы берутся из косвенной рекурсии.
    key - первый ключ в словаре
    х, у - координаты х, у стартовой точки, values for key.
    Возвращает вызов функции calculate_way(), с новыми значениями стартовых "х" и "у"
    """
    if dict_of_points.get(key) not in list_of_best_ways:
        list_of_best_ways.append(dict_of_points.get(key))
    point_x_start, point_y_start = point_x, point_y
    dict_of_points.pop(key)
    return calculate_way(point_x_start, point_y_start)


def calculate_and_print_best_way(list_of_best_ways):
    result = 0
    for_print = ""
    for item in list_of_best_ways:
        if item == list_of_best_ways[0] and result == 0:
            for_print += f'{item} -> '
        elif isinstance(item, tuple):
            for_print += f"{item}"
        else:
            result += item
            for_print += f'{[result]} -> '

    print(for_print.rstrip(" -> "), "=", result)


def reversed_list():
    """
    Так как наш алгоритм всегда возвращается к началу пути, мы всегда будем иметь минимум два самых оптимальных пути.
    Составляет маршрут в обратную сторону по тому же оптимальному пути. Возвращает новый список.
    """
    i = 2
    temp = list_of_best_ways.copy()
    start = temp[0]
    reversed_list_of_best_ways = [start]

    while start in temp:
        temp.remove(start)

    for k in temp[::-1]:
        if isinstance(k, tuple):
            reversed_list_of_best_ways.append(k)
    reversed_list_of_best_ways.append(start)

    for j in temp[::-1]:
        if isinstance(j, float):
            reversed_list_of_best_ways.insert(i, j)
            i += 2

    return reversed_list_of_best_ways


while dict_of_points:
    work_with_dicts()

calculate_and_print_best_way(list_of_best_ways)
calculate_and_print_best_way(reversed_list())
