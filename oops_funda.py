

# Object Oriented Programming

class car:

    def __init__(self, name,topspeed,price,transmission):
        self.name = name
        self.topspeed = topspeed
        self.price = price
        self.transmission = transmission

    def getter(self):
        print("Name: ",self.name)
        print("Top Speed: ",self.topspeed)
        print("Price: ",self.price)
        print("Transmission: ",self.transmission)

    def setter(self,n,t,p,tr):
        self.name = n
        self.topspeed = t
        self.price = p
        self.transmission = tr

    # def __del__(self):
    #     print("Destructor called, car deleted")

    def is_sports_car(self):
        if self.topspeed>200:
            print("The car is a sports car")

    def is_worth(self):
        if self.topspeed/self.price>0.0001:
            print("The car is worth buying")

honda = car("Honda", 200, 100000, "Automatic")
honda.getter()
honda.setter("Honda_The_power_of_dreams", 300, 100000, "Automatic")
honda.getter()
honda.is_sports_car()



