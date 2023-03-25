fiat = 1.5
ford = 1.25
honda = 1.25
toyota = 1
bmw = 0.80
mercedes = 0.75

brands = {'fiat': 1.5, 'ford': 1.25, 'honda': 1.25, 'toyota': 1, 'bmw': 0.8, 'mercedes': 0.75}


class Vehicle():
    def __init__(self, weight=0, fuelLevelMax=0, fuelLevelCurrent=0, fuelRatio=0, wheel=0, distance=0, brand=0,
                 engineTorque=0, engineVolume=0, speed=0, remains=0, time=0):
        self.weight = weight
        self.fuelLevelMax = fuelLevelMax
        self.fuelLevelCurrent = fuelLevelCurrent
        self.fuelRatio = fuelRatio
        self.wheel = wheel
        self.distance = distance
        self.brand = brand
        self.engineTorque = engineTorque
        self.engineVolume = engineVolume
        self.speed = speed
        self.remains = remains
        self.time = time

    def calcweight(self):
        self.weight = self.brand * ((self.wheel * 100) + self.fuelLevelCurrent)
        return

    def calcremains(self):
        self.remains = (self.fuelLevelCurrent * 15)
        return

    def calcfuelratio(self):
        self.fuelRatio = (self.fuelLevelCurrent / self.fuelLevelMax) * 100
        return

    def calcengine(self):
        self.speed = (self.engineVolume / 75) * (self.engineTorque / 75) - (self.wheel + (self.weight / 100))
        return

    def travel(self):
        self.distance = self.speed * self.time
        return

    def fuelconsumption(self):
        self.fuelLevelCurrent = self.fuelLevelCurrent - (self.distance / 15)
        return


class Car(Vehicle):
    def __init__(self, weight, fuelLevelMax, fuelLevelCurrent, fuelRatio, distance, brand, engineTorque, engineVolume,
                 speed, remains, time, wheel=4, seats=0, window=0, door=0):
        super().__init__(weight, fuelLevelMax, fuelLevelCurrent, fuelRatio, wheel, distance, brand, engineTorque,
                         engineVolume, speed, remains, time)
        self.seats = seats
        self.window = window
        self.door = door

    def calcweight(self):
        self.weight = self.brand * ((self.wheel * 100) + (self.seats * 120) + (self.door * 150) + self.fuelLevelCurrent)
        return


class Motorcycle(Vehicle):
    def __init__(self, weight, fuelLevelMax, fuelLevelCurrent, fuelRatio, distance, brand, engineTorque, engineVolume,
                 speed, remains, time, wheel=2):
        super().__init__(weight, fuelLevelMax, fuelLevelCurrent, fuelRatio, wheel, distance, brand, engineTorque,
                         engineVolume, speed, remains, time)


arac1 = Car(weight=0, fuelLevelMax=1200, fuelLevelCurrent=400, fuelRatio=0, distance=0, brand=ford, engineTorque=700,
            engineVolume=1800, speed=0, remains=0, time=2, wheel=4,
            seats=5, window=6, door=5)

arac1.calcweight()

arac1.calcremains()

arac1.calcengine()

arac1.calcfuelratio()

arac1.travel()

print('Arabanin Agirligi(kg):', arac1.weight, 'kg')
print('Benzin:', '%', arac1.fuelRatio)
print('Guncel Benzinle Kac Metre Gidilir:', arac1.remains, 'm')
print('Yol:', arac1.distance, 'm')
print('Aracin Hizi:', arac1.speed, 'm/s')


arac1.fuelconsumption()
arac1.calcfuelratio()
arac1.calcremains()

print('Yol Sonrasi Kalan Benzin:', '%', arac1.fuelRatio)
print('Kalan Benzinle Kac Metre Gidilir:', arac1.remains, 'm')
