# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:
    """
    Get the onboard temperature in celsius
    """
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        pass
    def read_voltage(self):        
        return 2.7
    def get_temperature(self):
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]

  
class CarbonMonoxideSensor:
    """
    Sensor capable of getting carbon monoxide level and converting voltage to carbon monoxide level.
    """
    VOLTAGE_TO_CO_FACTOR = 0.048
    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()
    def get_carbon_monoxide_level(self):
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide
    def read_sensor_voltage(self):
        # In real life, it should read from hardware.        
        return 2.3
    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature

    
class DisplayUnit:
    """
    Show the units 
    """
    def __init__(self):
        self.string = ''
    def display(self,msg):
        print(msg)


class CarbonMonoxideDevice:
    """
    Show the carbon Monoxide level.
    """
    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit       
    def Display(self):
        msg = 'Carbon Monoxide Level is : ' +  str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
    