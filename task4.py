# ЭТО РЕШЕНИЕ 4-ей ЗАДАЧИ
import csv

"""Ф-ия , создающая промокоды на товары,
 в аргументе принимает название файла, 
 из которого вы их создаем"""
def create_action(filename):

    # открываем поданный файл и составляем список со всеми его строками
    with open(filename, mode="r", encoding="utf8") as csvf:
        reader = csv.reader(csvf, delimiter=";", quotechar=",")

        # создаем список строк из таблицы
        lines = []
        for x in reader:
            lines.append(x)
        lines2 = []

        # составляем промокоды
        for x in lines[1:]:
            c = x
            c.append(x[1][:2].upper()+x[-3].split(".")[0]+x[1][-2:][::-1].upper()+x[-3].split(".")[1][::-1])
            lines2.append(c)
    # записываем результаты в итоговый файлproduct_promo.csv
    with open("product_promo.csv", mode="w", encoding="utf8",newline="") as f:
        writer = csv.writer(f, delimiter=";", quotechar="'")
        writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'total', 'promocode'])
        for x in lines2:
            writer.writerow(x)

create_action("products.csv")