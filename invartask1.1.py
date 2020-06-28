import csv
import math


def mean_quadratic_deviation(data):
    """
    Среднее квадратичное отклонение данных из переданного списка.
    :param data:
    :return:
    """
    return math.sqrt(dispersion(data))


def dispersion(data):
    """
    Дисперсия данных из переданного списка.
    :param data:
    :return:
    """
    data_disp = [(i - average(data)) ** 2 for i in data]
    return sum(data_disp) / len(data_disp)


def average(data):
    """
     Среднее значение данных из переданного списка.
    :param data:
    :return: average
    """
    return sum(data) / len(data)


def csv_reader(file_csv, col_num):
    """
    Функция для считывания данных из csv файла.
    """
    reader = csv.reader(file_csv, delimiter=';')
    return [float(line[col_num - 1].replace(',', '.')) for line in reader]


if __name__ == '__main__':
    csv_path = 'data.csv'
    col_num = 1

    with open(csv_path, encoding='utf-8', newline='') as f_obj:
        data = csv_reader(f_obj, col_num)

    print('Среднее значение: {}'.format(average(data)))
    print('Дисперсия: {}'.format(dispersion(data)))
    print('Среднее квадратичное отклонение: {}'.format(mean_quadratic_deviation(data)))
    
