student_1 = {
    'first_name': "John", 'last_name': "Wick",
    'age': 45
}
student_2 = {
    'first_name': "Jack", 'last_name': "Sparrow",
    'age': 50
}
student_3 = {
    'first_name': "Mary", 'last_name': "Lee",
    'age': 37
}


# - Class = template or Bleuprint to create new objects

# - Objects =  are instances of class


#!  Example class :  Human

#!   Objects :  Putin Trump

class Human:
    # Constructor
    def __init__(self, name, age, country):
        # AtTributes -- Values
        self.first_name = name
        self.his_age = age
        self.his_country = country

    def increase_age(self):
        self.his_age += 1
        return self
        # Methods

    def print_info(self):
        print("President is "+self.first_name+" his Age "+str(self.his_age) +
              " and his Country " + self.his_country)

        return self


Putin = Human("Putin", 78, "Russia")
Putin.print_info().increase_age().print_info().increase_age().print_info()
