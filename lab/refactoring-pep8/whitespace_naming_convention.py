# by Kami Bigdely
# PEP8 - whitespaces and variable names.
# This is a guess game. Guess what number the computer has chosen!
class Pizza:
    def __init__ (obj, mybread_type, CHEESE_TYPE, meat_type, pizza_toppings, size):
        obj.bread_type= mybread_type
        obj.cheese_type = CHEESE_TYPE
        obj.meat_type= meat_type
        obj.toppings = pizza_toppings
        obj.size = size
    @classmethod
    def create_chicago_pizza (class_type, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meatType= 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 'chunky tomato sauce', 'onion']
        return class_type(bread, cheese, meatType, toppings, size)
    @classmethod
    def create_california_pizza(class_type, meat_type, size):
        BREAD = 'thin crust'
        CHEESE = 'feta cheese'
        TOPPINGS = ['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper']
        return class_type(BREAD, CHEESE, meat_type, TOPPINGS, size)
    def printInfo(obj):
        print('bread type is: ', obj.bread_type)
        print('cheese type is: ', obj.cheese_type)
        print('meat type is: ', obj.meatType)
        print('Toppings are: ', end='')
        print(', '.join(map(str, obj.toppings)))

myPizza = pizza.create_california_pizza('chicken', 'large')
myPizza.printInfo()