from measures_of_variability import get_standart_deviation as std_method


def get_se(lst: list) -> float:
    """
    Центральная предельная теорема - распределние средних значений выборки из генеральной совокупности
     стремится к нормальному распределени.
    :param lst:
    :return: se
    """
    lst_len = len(lst)
    std = std_method(lst)

    return std/(lst_len**0.5)
