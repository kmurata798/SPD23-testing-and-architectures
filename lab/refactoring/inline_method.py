# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18
class Person:
    def __init__(self, my_age):
        self.age = my_age

def enter_night_club(individual):
    if individual.age > LEGAL_DRINKING_AGE:
        print("allowed to enter")
        return True
    print("Entrance of minors is denited")
    return False

person = Person(17.9)
enter_night_club(person)
        
