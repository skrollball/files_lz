import csv  # модуль для csv
import pandas as pd  # модуль для таблиц
import matplotlib.pyplot as plt  # модуль для графиков
tab = pd.read_parquet('titanic.parquet')  # читаем исходный файл parquet в таблицу pandas
tab.to_csv('titanic.csv', index=False)  # сохраняем таблицу в формат csv без индексов
sur = {1: 0, 2: 0, 3: 0}  # словарь для подсчета выживших по трем классам
fil = open('titanic.csv', 'r', encoding='UTF-8')  # открываем файл csv
rdr = csv.reader(fil, delimiter=',')  # читаем строки csv с разделителем запятая
hdr = next(rdr)  # пропускаем заголовки столбцов
s = hdr.index('Survived')  # индекс столбца выживших
c = hdr.index('Pclass')  # индекс столбца класса
for row in rdr:  # перебираем пассажиров и считаем выживших в каждом классе
    if row[s] == '1':  # проверяем статус выжившего
        cls = int(row[c])  # определяем номер класса
        sur[cls] += 1  # прибавляем к счетчику
fil.close()  # закрываем файл
kls = ['1 класс', '2 класс', '3 класс']  # названия столбцов графика
kol = [sur[1], sur[2], sur[3]]  # значения по классам
plt.bar(kls, kol)  # строим столбчатую гистограмму выживаемости пассажиров по классам
plt.title('Выживаемость пассажиров по классам билетов')  # заголовок графика
plt.xlabel('Класс билета')  # подпись оси X
plt.ylabel('Количество выживших')  # подпись оси Y
plt.show()  # выводим график
