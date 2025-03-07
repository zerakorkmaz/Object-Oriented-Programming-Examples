#Method Overriding, bir üst sınıfta tanımlanan bir metodu, alt sınıfta yeniden tanımlamak ve farklı bir şekilde
# çalışmasını sağlamak demektir.Polymorphism ile benzerdir.

#sipariş sistemi oluşturalım, "prepare" metodu sipariş türlerinde farklı çalışsın.
class Order:
    menu={"Fast Food":{"Hamburger":150,"Pizza":200},
          "Gourmet": {"Salad":80, "Steak":300},
          "Vegan":{"Vegan Burger": 120, "Vegan Pizza": 180}
    }

    def __init__(self,dish_name,dish_type):
        self.dish_name=dish_name
        self.dish_type=dish_type
        self.price=self.menu[dish_type].get(dish_name,0)
        print(f"{self.dish_name} is added to the order.")

    def prepare(self):
        return print(f"{self.dish_name} is preparing...")

    def get_price(self):
        return self.price

class FastFood(Order):
    def prepare(self):
        return print(f"{self.dish_name} is preparing...")

class GourmeOrder(Order):
    def prepare(self):
        return print(f"{self.dish_name} is preparing...")

class VeganOrder(Order):
    def prepare(self):
        return print(f"{self.dish_name} is preparing...")

#kullanıcının sipariş oluşturacağı bir fonksiyon da ekleyelim.
def create_order():
    print("\n---Menü---")
    for dish_type, dishes in Order.menu.items():
        print(f'{dish_type} :{", ".join(dishes.keys())}')

    print('Please choose a dish type..!')
    print('1-Fast Food')
    print('2-Gourmet')
    print('3-Vegan')

    dish_type=int(input('Enter your choice: (1/2/3) '))

    if dish_type==1:
        dish_type='Fast Food'
    elif dish_type==2:
        dish_type='Gourmet'
    elif dish_type==3:
        dish_type='Vegan'
    else:
        print('Invalid choice!')
        return craete_order()

    print('f\n{dish_type} Menu:')
    for dish,price in Order.menu[dish_type].items():
        print(f'{dish} : {price}TL')

    dish_name=input('Please choose a dish..!')


    if dish_type=='Fast Food':
        return FastFood(dish_name,dish_type)
    elif dish_type=='Gourmet':
        return GourmeOrder(dish_name,dish_type)
    elif dish_type=='Vegan':
        return VeganOrder(dish_name,dish_type)

def process():
    print('\n---New Order---')
    order_number=int(input('How many pieces would you like to order?'))
    orders=[]
    total_price=0

    for i in range(order_number):
        order = create_order()
        orders.append(order)
        total_price+=order.get_price()

        print(f'Total price: {total_price}')
        print(f'Your order is completed!.')

process()

#Açıklamak gerekirse burada FastFood, GourmetOrder, VeganOrder sınıfları, Order sınıfından türetilmiş alt sınıflardır.
# Bu sınıflar, prepare metodunu override eder