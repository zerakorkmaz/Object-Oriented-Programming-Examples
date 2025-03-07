#Polymorphism (Çok Biçimlilik), farklı sınıfların aynı metodu farklı şekillerde
# uygulayabilmesini sağlar.

#Bir çok akıllı cihazın bulunduğu bir akıllı ev sistemi oluşturalım.

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        print(input("Select the light color:(yellow, white, red, blue)"))
        print(input("Select the light brightness:(low, medium, high)"))
        print("Light turned on")
    def turn_off(self):
        print("Light turned off")

class AirConditioner(SmartDevice):
    def turn_on(self):
        print("Air conditioner turned on")
        print(input("Enter temperature: "))
        print("Warming, please wait...")

    def turn_off(self):
        print("Air conditioner turned off")

class SecurityCamera(SmartDevice):
    def turn_on(self):
        print("Security camera turned on,registration has started..! ")
    def turn_off(self):
        print("Security camera turned off, registration has stopped..! ")

devices=[Light(),AirConditioner(),SecurityCamera()]
for device in devices:
    device.turn_on()

#burada turn on ve turn off fonksiyonları her sınıfta farklı bir şekilde uygulanıyor.