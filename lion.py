import csv  # библиотека для CSV-таблиц
import matplotlib.pyplot as plt  # библиотека для графиков
f = open('lion.txt', 'r', encoding='UTF-8')  # открываем файл lion.txt для чтения
text = f.read().lower()  # читаем весь текст и переводим в нижний регистр
f.close()  # закрываем файл
for zn in '.,!?:;-—()"\'«»\n\r\t0123456789':  # перебираем лишние символы
    text = text.replace(zn, ' ')  # заменяем на пробел
words = text.split()  # делим на слова
total = len(words)  # всего слов
word_dict = {}  # словарь для подсчета частоты каждого уникального слова в тексте
for w in words:  # перебираем слова
    if w in word_dict:  # слово уже есть
        word_dict[w] = word_dict[w] + 1  # увеличиваем счетчик
    else:  # слово встретилось впервые
        word_dict[w] = 1  # ставим единицу
rows = []  # список для сортировки
for w in word_dict:  # перебираем словарь
    rows.append([word_dict[w], w])  # добавляем пару
rows.sort(reverse=True)  # сортируем слова по убыванию частоты встречаемости
outfile = open('lion_words.csv', 'w', encoding='utf-8-sig', newline='')  # открываем CSV-файл для записи таблицы в кодировке для эксель
writer = csv.writer(outfile, delimiter=';', quotechar='"')  # создаем объект записи с разделителем точка с запятой 
writer.writerow(['Слово', 'Частота встречи, раз', 'Частота встречи в %'])  # записываем заголовки столбцов
for item in rows:  # записываем все отсортированные слова в таблицу
    count = item[0]  # берем частоту
    word = item[1]  # берем слово
    percent = (count / total) * 100  # считаем процент
    writer.writerow([word, count, f"{percent:.2f}"])  # пишем строку в таблицу
outfile.close()  # закрываем файл таблицы
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'  # строка алфавитов
letters = []  # список букв
counts = []  # список количеств
for ch in alphabet:  # подсчитываем частоту каждой буквы по алфавиту
    cnt = text.count(ch)  # считаем букву
    if cnt > 0:  # буква есть в тексте
        letters.append(ch)  # добавляем букву
        counts.append(cnt)  # добавляем количество
plt.bar(letters, counts)  # строим столбчатую гистограмму встречаемости букв на экране
plt.title('Частота встречаемости букв в тексте')  # заголовок графика
plt.xlabel('Буквы')  # подпись оси X
plt.ylabel('Частота встречи, раз')  # подпись оси Y
plt.show()  # показываем график