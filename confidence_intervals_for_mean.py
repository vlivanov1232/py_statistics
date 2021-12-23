from central_limit_theorem import get_se
from central_trend_measures import get_mean


def get_95_interval(lst: list) -> (float, float):
    """
    95 доверительный интервал = среднее значение +- 1.96 стандартной ошибки
    :param lst:
    :return: 95% доверительный интервал
    """

    se = get_se(lst)
    mean = get_mean(lst)

    return mean - se * 1.96, mean + se * 1.96
