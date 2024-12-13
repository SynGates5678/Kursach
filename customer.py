class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
         return {
             'customer_id': self.customer_id,
             'name': self.name,
             'email': self.email
         }