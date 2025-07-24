from datetime import datetime

class TemperatureConverter:
    """
    A utility class for converting temperatures between Celsius and Fahrenheit.

    This class provides methods to convert temperatures in both directions and 
    maintains a history of all conversions performed.
    """

    def __init__(self) -> None:
        self._conversions = []
    
    def celsius_to_fahrenheit(self, celsius_temp: float) -> float:
        """
        Converts a temperature from Celsius to Fahrenheit.

        Args:
            celsius_temp (float): Temperature in degrees Celsius.

        Returns:
            float: Converted temperature in degrees Fahrenheit, rounded to 2 decimals.
        """
        fahrenheit_temp = round((celsius_temp * 9/5) + 32, 2)
        self._log_conversion("Celsius", celsius_temp, "Fahrenheit", fahrenheit_temp)
        return fahrenheit_temp
    
    def fahrenheit_to_celsius(self, fahrenheit_temp: float) -> float:
        """
        Converts a temperature from Fahrenheit to Celsius.

        Args:
            fahrenheit_temp (float): Temperature in degrees Fahrenheit.

        Returns:
            float: Converted temperature in degrees Celsius, rounded to 2 decimals.
        """
        celsius_temp = round((fahrenheit_temp - 32) / 1.8, 2)
        self._log_conversion("Fahrenheit", fahrenheit_temp, "Celsius", celsius_temp)
        return celsius_temp

    def _log_conversion(self, from_unit: str, from_value: float,
                        to_unit: str, to_value: float) -> None:
        """
        Logs a temperature conversion with timestamp and details.

        Args:
            from_unit (str): The unit of the original temperature (e.g., 'Celsius').
            from_value (float): The original temperature value.
            to_unit (str): The unit of the converted temperature (e.g., 'Fahrenheit').
            to_value (float): The converted temperature value.
        """
        timestamp = datetime.now().isoformat()
        self._conversions.append({
            "timestamp": timestamp,
            "from": {"unit": from_unit, "value": from_value},
            "to": {"unit": to_unit, "value": to_value}
        })
    
    def get_conversion_history(self) -> list[dict]:
        """
        Returns the list of all recorded temperature conversions.

        Returns:
            list[dict]: A list of dictionaries representing each conversion entry.
        """
        return self._conversions
    
    def clear_conversion_history(self) -> None:
        """
        Clears all recorded temperature conversions.
        """
        self._conversions.clear()
