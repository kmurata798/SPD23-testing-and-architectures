# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cooked_criteria_satisfied(time, temperature, pressure, desired_state):
    is_well_done = time * temperature * pressure * COOKED_CONSTANT >= WELL_DONE
    return desired_state == 'well-done' and is_medium_rare:
    is_medium_rare = time * temperature * pressure * COOKED_CONSTANT >= MEDIUM
    return desired_state == 'medium' and is_medium_rare: