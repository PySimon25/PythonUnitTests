from datetime import datetime

class TemperatureConverter:

    def __init__(self) -> None:
        self._conversions = []
    
    def celsius_to_fahrenheit(self, celsius_temp: float) -> float:
        fahrenheit_temp = round((celsius_temp * 9/5) + 32, 2)
        self._log_conversion("Celsius", celsius_temp, "Fahrenheit", fahrenheit_temp)
        return fahrenheit_temp
    
    def fahrenheit_to_celsius(self, fahrenheit_temp: float) -> float:
        celsius_temp = round((fahrenheit_temp - 32) / 1.8, 2)
        self._log_conversion("Fahrenheit", fahrenheit_temp, "Celsius", celsius_temp)
        return celsius_temp

    def _log_conversion(self, from_unit: str, from_value: float, to_unit: str, to_value: float):
        timestamp = datetime.now().isoformat()
        self._conversions.append({
            "timestamp": timestamp,
            "from": {"unit": from_unit, "value": from_value},
            "to": {"unit": to_unit, "value": to_value}
        })
    
    def get_conversion_history(self) -> list[dict]:
        return self._conversions
    
    def clear_conversion_history(self) -> None:
        self._conversions.clear()
