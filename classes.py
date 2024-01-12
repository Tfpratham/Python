class Vehicle:
      #self mandatory hota hai
      #self is referring to its self
      def __init__(self, make,model):
            self.make= make
            self.model= model      
      def moves(self):
            print('Moves along....') 
      def get_make_model(self):
            print(f"I'm a {self.make} {self.model}")
#creating object of the upper class            
my_car = Vehicle('Volksvagan', 'GTI')
#calling method of the class 
print(my_car.make)
print(my_car.model)
my_car.moves()
my_car.get_make_model()

your_car=Vehicle("GTR", "R35")
your_car.get_make_model()
your_car.moves()

there_car=Vehicle("Skyline","R34")
there_car.get_make_model()

our_car=Vehicle("BMW","s class")
our_car.get_make_model()

their_car=Vehicle("G wagon","g63")
their_car.get_make_model()
my_car.moves()

class Airplane(Vehicle):
      def moves(self):
          print('flies along')

class Truck(Vehicle):
      def moves(self):
            print('rumbles along')

class trollie(Vehicle):
      pass

Hasegawa =Airplane('Hasegawa', 'A-4E/F') 
Hasegawa.get_make_model()
Hasegawa.moves()
Toyota =Truck('Toyota', '42n') 
Toyota.get_make_model()
Toyota.moves()
Dmart =trollie('Dmart', '4wheel') 
Dmart.get_make_model()
Dmart.moves()