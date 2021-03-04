import pytest
import extract_position_4 as ext_pos

@pytest.fixture
def input_average():
    return "|update| the positron location \
        in the particle accelerator is x:21.432"
        

@pytest.fixture
def input_null():
    """When the device is not inputting any value."""
    return None


@pytest.fixture
def input_error():
    """When the machine has an error: the log reports an error."""
    return "|error| An error has occured!"

def test_extract_position_null_case(input_null):
    """Runs with an input that is None"""
    # when the function is given a NoneType Input
    assert ext_pos.extract_position(input_null) == None

def test_extract_position_average_case(input_average):
    """Runs with a proper input from the device, and returns
    the location of the positron."""
    # Expected Input - input includes 'x:' for average inputs
    assert ext_pos.extract_position(input_average) == "21.432"

def test_extract_position_null_case(input_error):
    """Reads in a log when the machine is broken"""
    # Error Input - when the input is either 'error' or 'debug' 
    assert ext_pos.extract_position(input_error) == None