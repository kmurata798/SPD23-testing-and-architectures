# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cooked_criteria_satisfied(time, temperature, pressure, desired_state):
    well_done_calculation = time * temperature * pressure * COOKED_CONSTANT >= WELL_DONE
    medium_calculation = time * temperature * pressure * COOKED_CONSTANT >= MEDIUM
    if desired_state == 'well-done' and well_done_calculation: 
        return True
    if desired_state == 'medium' and medium_calculation:
        return True
    return False