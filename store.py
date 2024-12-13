import json
from product import Product
from customer import Customer
from order import Order


class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []

    def add_product(self, name, price, stock):
        product_id = len(self.products) + 1  # Генерация уникального ID товара
        new_product = Product(product_id, name, price, stock)
        self.products.append(new_product)
        print(f"Товар '{name}' добавлен.")

    def remove_product(self):
        self.display_products()
        product_id = int(input("Введите ID товара для удаления: "))

        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                del self.products[i]
                print(f"Товар с ID {product_id} удален.")
                return

        print(f"Товар с ID {product_id} не найден.")

    def add_customer(self, name, email):
        customer_id = len(self.customers) + 1  # Генерация уникального ID клиента
        new_customer = Customer(customer_id, name, email)
        self.customers.append(new_customer)
        print(f"Клиент '{name}' добавлен.")

    def create_order(self):
        self.display_customers()

        customer_id = int(input("Введите ID клиента для заказа: "))

        customer = next((c for c in self.customers if c.customer_id == customer_id), None)

        if not customer:
            print(f"Клиент с ID {customer_id} не найден.")
            return

        order = Order(len(self.orders) + 1, customer)

        while True:
            self.display_products()

            product_id = int(input("Введите ID товара для заказа (или 0 для завершения): "))

            if product_id == 0:
                break

            product = next((p for p in self.products if p.product_id == product_id), None)

            if not product:
                print(f"Товар с ID {product_id} не найден.")
                continue

            quantity = int(input(f"Введите количество товара '{product.name}': "))

            if order.add_product(product, quantity):
                print(f"Добавлено {quantity}x '{product.name}' в заказ.")
            else:
                print(f"Недостаточно товара '{product.name}' на складе.")

        self.orders.append(order)
        print(f"Заказ ID {order.order_id} создан для клиента {customer.name}.")

        # Сохранение чека в текстовый файл
        order.save_receipt()

    def save_to_file(self, filename):
        data = {
            'products': [product.to_dict() for product in self.products],
            'customers': [customer.to_dict() for customer in self.customers],
            'orders': [order.to_dict() for order in self.orders]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for product_data in data['products']:
                self.add_product(product_data['name'], product_data['price'], product_data['stock'])

            for customer_data in data['customers']:
                self.add_customer(customer_data['name'], customer_data['email'])

            for order_data in data['orders']:
                customer = next(c for c in self.customers if c.customer_id == order_data['customer']['customer_id'])
                order = Order(order_data['order_id'], customer)

                for product_info in order_data['products']:
                    product = next(p for p in self.products if p.product_id == product_info[0])
                    order.add_product(product, product_info[1])

                self.orders.append(order)

    def display_products(self):
        print("\nСписок товаров:")
        for product in self.products:
            print(f"{product.product_id}. {product.name} - {product.price} руб., Остаток: {product.stock}")

    def display_customers(self):
        print("\nСписок клиентов:")
        for customer in self.customers:
            print(f"{customer.customer_id}. {customer.name} - {customer.email}")

    def display_orders(self):
        # Логика просмотра заказов по ID
        if not self.orders:
            print("Нет созданных заказов.")
            return

        for order in self.orders:
            products_list = ', '.join([f"{quantity}x {product.name}" for product, quantity in order.products])
            total_price = order.total_price()
            print(
                f"Заказ ID {order.order_id}: Клиент - {order.customer.name}, Товары - [{products_list}], Общая сумма - {total_price} руб.")

