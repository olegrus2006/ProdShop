# ЭТО РЕШЕНИЕ 2-ой ЗАДАЧИ
import csv

# открываем исходный файл products.csv
with open("products.csv", mode="r", encoding="utf8") as csvf:
    reader = csv.reader(csvf, delimiter=";",quotechar=",")

    #создаем список строк из таблицы
    lines = []
    for x in reader:
        lines.append(x)

    # выполняем мортировку всех строк таблицы методом выборки
    N = len(lines)
    for i in range(1, N):
        for j in range(i, 0, - 1):
            if lines[j - 1] > lines[j]:
                lines[j - 1], lines[j] = lines[j], lines[j - 1]
    lines2 = lines[1:]

    # находим самую первую категорию товаров
    first_cat = lines2[0][0]

    # составляем список всех строк таблицы с товаром первой категории
    tovars = []
    for x in lines2:
        if x[0]==first_cat:
            tovars.append(x)

    # переменная с максимальной ценой итовара за единицу
    ANSWER = -10**99

    # переменная с самым дорогим товаром
    ANWER_TOVAR = ""

    # Определяем самый дорогой товар и его цену за единицу
    for x in tovars:
        if float(x[-2]) > ANSWER:
            ANSWER = float(x[-2])
            ANWER_TOVAR = x[1]
    print(f"В категории: {first_cat} самый дорогой товар {ANWER_TOVAR} его цена за единицу товара составляет {ANSWER}")

