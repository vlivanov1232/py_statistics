from math import sqrt


def get_range(lst: list) -> float:
    """
    Размах - разница между самым большим и маленьким элементом
    :param lst: список для нахождения разницы
    :return: разница между элементами
    """

    return max(lst) - min(lst)


def get_variance(lst: list) -> float:
    """
    Дисперсия - средние значение квадрата отклонений каждого элемента от среднего значения всех элементов
    :param lst: список для нахождения дисперсии
    :return: дисперсия
    """

    lst_len = len(lst)
    mean = sum(lst) / lst_len
    arr_to_variance = [(x - mean)**2 for x in lst]

    return sum(arr_to_variance) / (lst_len - 1)


def get_standart_deviation(lst: list) -> float:
    """
    Среднеквадратическое отклонение - корень из дисперсии. Необходим чтобы получить настоящее отклонение от среднего значения
    :param lst: список для нахождения среднеквадратичного отклонения
    :return: среднеквадратичное отклонение
    """

    return sqrt(get_variance(lst))


