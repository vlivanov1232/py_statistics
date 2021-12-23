from central_trend_measures import get_mean as mean
from measures_of_variability import get_standart_deviation as stdev


def z_standart(lst: list) -> list:
    """
    Z-преобразование или стандартизация - приведение наших данных к такой шкале, где cреднее становится 0,
    а стандартное отклонение 1
    :param lst: список для стандартизации
    :return: список над которым произведено z преобразование
    """
    lst_mean = mean(lst)
    st_dev = stdev(lst)
    return [(val - lst_mean)/st_dev for val in lst]
