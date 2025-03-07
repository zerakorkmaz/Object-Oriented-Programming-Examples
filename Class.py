#Sınıf (Class), nesnelerin özelliklerini ve davranışlarını tanımlayan bir şablondur.

class BackPack:
    pass

#İnstance Attributes yani nesne niteliklerini "__init__" fonksiyonu ile sınıflar içerisine tanımlarız.

class BackPack:
    def __init__(self, color, size):
        self.color = color
        self.size = size

backpack1=BackPack("red", 10)
backpack2=BackPack("blue", 20)

print(f'first backpack is {backpack1.color} and size is {backpack1.size}'
      f'\nsecond backpack is {backpack2.color} and size is {backpack2.size}')

# Bir fast food restoranı için sistem tasarımı oluşturalım
# -> İlgili sınıflar: Pizza, Müşteri, Çalışan,
# Sipariş Özellikleri: Pizzanın boyutu, fiyatı, müşteri adı, sipariş numarası

class Pizza:
    def __init__(self, size,ingredients, price):
        self.size = size
        self.ingredients = ingredients
        self.price = price

    def show_info(self):
        return print(f"{self.size} pizza ({', '.join(self.ingredients)}): {self.price} TL")

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_info(self):
        return print(f"Customer: {self.name} - {self.phone}")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_info(self):
        return print(f"Employee: {self.name} - {self.position}")

class Order:
    order_counter=1
    def __init__(self, customer, employee, pizza):
        self.order_id =Order.order_counter
        Order.order_counter+=1
        self.customer = customer
        self.employee = employee
        self.pizza = pizza
        self.total_price = self.pizza.price

    def show_info(self):
        return print(f"Order #{self.order_id} - {self.customer.name} ({self.customer.phone}) ordered a {self.pizza.size} "
                     f"pizza with {self.pizza.ingredients} ingredients and the total price is {self.total_price} TL.")


customer1=Customer("Ali","05321234567")
pizza1=Pizza("Large","cheese,sausage","100")
pizza2=Pizza("Small","pepperoni","150")
employee= Employee("Mehmet","cashier")
order1 = Order(customer1, employee, pizza1)
order2 = Order(customer1, employee, pizza2)

print(order1.show_info())
print(order2.show_info())


