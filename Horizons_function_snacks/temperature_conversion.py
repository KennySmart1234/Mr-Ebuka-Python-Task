    
        
            
def temperature_conversion(temperature, threshold, unit='F'):

    unit = unit.upper()

    if unit == "C":
        converted_temperature = (temperature * 9/5) + 32

    elif unit == "F":
        converted_temperature = (temperature - 32) * 5/9

    else:
        return "Invalid unit"


    if converted_temperature < threshold:
        return "Cold advisory"

    elif converted_temperature >= threshold:
        return "Heat alert"
            
     





