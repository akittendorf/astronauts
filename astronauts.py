from csv import DictReader
from random import choice

class Astronaut(object):
    def __init__(self, name, status, flight_hours):
        self.__name = name
        self.__status = status
        self.__flight_hours = flight_hours   
        
    @property
    def name(self):
        return self.__name
    
    @property
    def status(self):
        return self.__status
    
    @property
    def flight_hours(self):
        return self.__flight_hours
    
    def __repr__(self):
        return 'Astronaut({}, {}, {})'.format(self.name, self.status, self.flight_hours)
        
    # create constructor object
    def __new__(cls, name, status, flight_hours):
        flight_hours = int(flight_hours)
        if type(name) == str and type(status) == str and type(flight_hours) == int:
            return object.__new__(cls)
        else:
            print("Invalid parameter data types (name: str, status: str, flight_hours: int)")
            return None
    
    # create gt, ge, eq magic methods based on flight hours
    def __gt__(self, other):
        return self.flight_hours > other.flight_hours
    
    def __ge__(self, other):
        return self.flight_hours >= other.flight_hours
    
    def __eq__(self, other):
        return self.flight_hours == other.flight_hours
    
    # create str magic method to print name, status
    def __str__(self):
        return "{}, {}".format(self.name, self.status)

# read in astronauts.csv and store each row as an Astronaut
def astronauts(file): # takes a file, returns a list
    astronauts = []
    with open(file) as infile:
        reader = DictReader(infile)
        for row in reader:
            astronauts.append(Astronaut(row['Name'], row['Status'], row['Space Flight (hr)']))
    return astronauts

astronauts = astronauts('astronauts.csv')

# list all mutable attributes from the first Astronaut object
print(astronauts[0].__dict__.keys())

# pick two random Astronauts and compare them 
def compare(lst): # takes a list, returns none
    ast1 = choice(lst)
    duplicate = True
    while duplicate == True:
        ast2 = choice(lst)
        if ast1 == ast2:
            continue
        else: 
            duplicate = False
    print('Astronaut {} ({}) has equal flight hours to Astronaut {} ({}): {}'.format(ast1.name, ast1.flight_hours, ast2.name, ast2.flight_hours, ast1.__eq__(ast2)))
    print('Astronaut {} ({}) has more flight hours than Astronaut {} ({}): {}'.format(ast1.name, ast1.flight_hours, ast2.name, ast2.flight_hours, ast1.__gt__(ast2)))
    return 

compare(astronauts)

# print out all astronauts from the astronauts list. assume you cannot access any attributes.
for astronaut in astronauts:
    print(astronaut)
        
    

    
        


