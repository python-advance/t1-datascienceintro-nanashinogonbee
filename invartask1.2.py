import csv
import numpy


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

    print('Среднее значение: {}'.format(numpy.mean(data)))
    print('Дисперсия: {}'.format(numpy.var(data)))
    print('Среднее квадратичное отклонение: {}'.format(numpy.std(data)))

