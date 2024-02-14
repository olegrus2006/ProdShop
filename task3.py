import csv

while True:

    # Ввод категории товара пользователем
    category = input("Введите категорию товара:\n")

    # Если пользователь ввел молоко, то завершаем работу
    if category == "молоко":
        break
    fl = True

    # открываем исходный файл products.csv
    with open("products.csv", mode="r", encoding="utf8") as csvf:
        reader = csv.reader(csvf, delimiter=";", quotechar=",")

        # создаем список строк из таблицы
        lines = []
        for x in reader:
            lines.append(x)

        # создаем список всех товаров из нужной категории
        tovars_from_category = []
        for x in lines[1:]:
            if x[0] == category:
                tovars_from_category.append(x)

        # Если товар определен, то выводим товар с наименьшим числом продаж, иначе же выводим ошибку
        if tovars_from_category:
            min_sold_tovar = min(tovars_from_category, key=lambda x: float(x[-1]))
            print(f"В категории: {min_sold_tovar[0]} товар: {min_sold_tovar[1]} был куплен {min_sold_tovar[-1]} раз")
        else:
            print("Такой категории не существует в нашей БД")