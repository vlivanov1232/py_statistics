from math import nan
"""
Файл для создания и изучения свойств мер центральной тенденции
"""


def get_median(lst: list) -> float:
    """
    Медиана - значение, которое находится по середине
    :param lst: список для нахождения медианы
    :return: медиана для списка
    """
    lst_len = len(lst)
    if lst_len == 0:
        return nan

    if lst_len == 1:
        return lst[0]

    sort_list = sorted(lst)

    if lst_len % 2 != 0:
        return float(sort_list[int(lst_len / 2)])
    else:
        return (sort_list[int(lst_len / 2)] + sort_list[int(lst_len / 2) - 1]) / 2.0


def get_mean(lst: list) -> float:
    """
    Среднее значение - сумма значений поделенная на их количество
    :param lst: список для нахождения среднего
    :return: среднее значение списка
    """
    lst_len = len(lst)
    if lst_len == 0:
        return nan

    return sum(lst) / lst_len


def get_mode(lst: list) -> float | None:
    """
    Мода - максимальное количество элементов одного значения
    :param lst: список для нахождения моды
    :return: мода значение списка
    """
    lst_len = len(lst)
    if lst_len == 0:
        return nan

    res_dict = dict()

    cur_max = 0
    mode = None

    for val in lst:
        if val in res_dict:
            res_dict[val] += 1
        else:
            res_dict[val] = 1

        if cur_max < res_dict[val]:
            cur_max = res_dict[val]
            mode = val

    return mode
