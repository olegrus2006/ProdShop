# ЭТО РЕШЕНИЕ 1-ой ЗАДАЧИ
import csv

# открываем исходный файл products.csv
with open("products.csv", mode="r", encoding="utf8") as csvf:
    reader = csv.reader(csvf, delimiter=";",quotechar=",")

    #создаем список строк из таблицы
    lines = []
    for x in reader:
        lines.append(x)


# открываем и создаем новый файл products_new.csv
with open("products_new.csv", mode="w", encoding="utf8", newline="") as csvf:
    writer = csv.writer(csvf, delimiter=";", quotechar="'")
    newlines = []

    # переменная в которой хранится сумма выручки по категории Закуски
    ANSWER = 0
    for line in lines:
        x = line
        if "Count" in line:
            x.append("total")
        else:
            x.append(float(x[3]) * float(x[4]))
            # Если категория товара закуски, то добавлем в ANSWER
            if x[0] == "Закуски":
                ANSWER += float(x[3]) * float(x[4])
        newlines.append(x)
    # записываем результаты в новый файл products_new.csv
    for x in newlines:
        writer.writerow(x)
# Вывод ответа в консоли
print(ANSWER)
