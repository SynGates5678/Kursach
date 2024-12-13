from store import Store

def main():
    store = Store()

    # Загружаем данные из файла при запуске приложения (если файл существует)
    try:
        store.load_from_file('store_data.json')
    except FileNotFoundError:
        print("Файл данных не найден. Создан новый магазин.")

    while True:
        print("\n--- Музыкальный Магазин | До | Ре | Ми | До | Ре | До | ---")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Добавить клиента")
        print("4. Создать заказ")
        print("5. Сохранить данные")
        print("6. Вывести список товаров")
        print("7. Вывести список клиентов")
        print("8. Вывести список заказов")
        print("9. Выход")

        choice = input("Выберите действие: ")

        # Обработка выбора пользователя
        if choice == "1":
            name = input("Введите название товара: ")
            price = float(input("Введите цену товара: "))
            stock = int(input("Введите количество на складе: "))
            store.add_product(name, price, stock)

        elif choice == "2":
            store.remove_product()

        elif choice == "3":
            name = input("Введите имя клиента: ")
            email = input("Введите электронную почту клиента: ")
            store.add_customer(name, email)

        elif choice == "4":
            store.create_order()

        elif choice == "5":
            store.save_to_file('store_data.json')
            print("Данные сохранены в файл.")

        elif choice == "6":
            store.display_products()

        elif choice == "7":
            store.display_customers()

        elif choice == "8":
            store.display_orders()

        elif choice == "9":
            break


if __name__ == "__main__":
    main()