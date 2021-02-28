# by Kami Bigdely
# Extract class
class Meat:
    def __init__(self, time, temp, pressure, desired_state):
        self.time = time
        self.temp = temp
        self.pressure = pressure
        self.desired_state = desired_state
        self.WELL_DONE = 3000
        self.MEDIUM = 2500
        self.COOKED_CONSTANT = 0.05


    def is_cookeding_criteria_satisfied(self):
        return self.is_well_done() or \
            self.is_medium()


    def is_well_done(self):    
        return self.desired_state == 'well-done' and  \
            self.get_cooking_progress() >= self.WELL_DONE


    def is_medium(self):
        return self.desired_state == 'medium' and  \
            self.get_cooking_progress() >= self.MEDIUM

    def get_cooking_progress(self):
        return self.time * self.temp * self.pressure * self.COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'
# Instantiate a Meat class object passing in the variables above
current_meat = Meat(time, temp, pressure, desired_state)

if current_meat.is_cookeding_criteria_satisfied():
    print('cooking is done.')
else:
    print('ongoing cooking.')