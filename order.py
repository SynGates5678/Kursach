class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []

    def add_product(self, product, quantity):
        if product.sell(quantity):
            self.products.append((product, quantity))
            return True
        return False

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.products)

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'customer': {'customer_id': self.customer.customer_id},
            'products': [(product.product_id, quantity) for product, quantity in self.products]
        }

    def save_receipt(self):
        receipt_filename = f"receipt_{self.order_id}.txt"
        with open(receipt_filename, 'w', encoding='utf-8') as f:
            f.write(f"Чек для заказа ID: {self.order_id}\n")
            f.write(f"Клиент: {self.customer.name}\n")
            f.write(f"Электронная почта: {self.customer.email}\n")
            f.write("Товары:\n")
            for product, quantity in self.products:
                f.write(f"- {product.name}: {quantity} шт. по {product.price} руб.\n")
            f.write(f"Общая сумма: {self.total_price()} руб.\n")

        print(f"Чек сохранен в файл: {receipt_filename}")