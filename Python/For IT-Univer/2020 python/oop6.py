class Car():
    # attributes of your class
    name = 'x3'
    make = 'BMW'
    model = 2013
    car_count = 0
    
    #methods of your class
    def start(self, name, make, model):
        print('start  a  car')
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1 # it is for all objects in your class 
        
    def stop(self):
        print('stop car')
    #static methods
    @staticmethod
    def car_details(a, b):
        print("it's a class Car")
        return a * a, b ** 3


#creating an object of class Car
car_a = Car()
car_b = Car()

print(car_a.car_details(3, 3))

print(Car.car_details(2, 2))

'''print(type(car_b))

car_a.start()

print(car_a.make)

print(dir(car_a))

car_a.start('8','BMW', 2015 )

print(car_a.name)
car_b.start('3','Gyguli', 2003 )

print(car_b.make)

print(car_a.car_count)
'''
