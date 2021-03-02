# Get average
import math
def get_average(li):
    if not li:
        return float('NaN')
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average_empty_list():
    assert math.isnan(get_average([]))