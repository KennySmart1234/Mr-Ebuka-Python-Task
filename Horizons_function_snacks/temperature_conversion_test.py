    

from unittest import TestCase
from temperature_conversion import temperature_conversion


class TestTemperatureConversion(TestCase):

    def test_that_temperature_below_to_threshold_return_cold_advisory(self):
        self.assertEqual(temperature_conversion(4, 50, "c"), "Cold advisory")

    def test_that_temperature_equal_to_threshold_return_heat_alert(self):
        self.assertEqual(temperature_conversion(45, 5, "f"), "Heat alert")

    def test_that_temperature_above_to_threshold_return_heat_alert(self):
        self.assertEqual(temperature_conversion(55, 6, "c"), "Heat alert")         
    def test_that_temperature_above_to_threshold_return_heat_alert(self):
        self.assertEqual(temperature_conversion(58, 6, "f"), "Heat alert")        





        
        
                      
           










