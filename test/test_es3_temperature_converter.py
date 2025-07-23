import unittest
from datetime import datetime
from esercizi_python import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Crea un unico TemperatureConverter per tutti i test
        cls.temperature_converter = TemperatureConverter()

    def setUp(self) -> None:
        # Verifica che la histpry sia vuota
        self.assertEqual(self.temperature_converter.get_conversion_history(), [])

    def test_celsius_to_fahrenheit(self) -> None:
        # Conversioni varie da celsius a Fahrenheit
        self.assertEqual(self.temperature_converter.celsius_to_fahrenheit(-17.78), 0)
        self.assertEqual(self.temperature_converter.celsius_to_fahrenheit(0), 32)
        self.assertEqual(self.temperature_converter.celsius_to_fahrenheit(40), 104)
        self.assertEqual(self.temperature_converter.celsius_to_fahrenheit(-17), 1.4)

    def test_fahrenheit_to_celsius(self) -> None:
        # Conversioni varie da Fahrenheit a Celsius
        self.assertEqual(self.temperature_converter.fahrenheit_to_celsius(0), -17.78)
        self.assertEqual(self.temperature_converter.fahrenheit_to_celsius(68), 20)

    def test_celsius_to_fahrenheit_logging(self) -> None:
        # Verifica che i log °C -> °F vengano creati correttamente
        result = self.temperature_converter.celsius_to_fahrenheit(100)
        self.assertEqual(result, 212.0)

        # Recupera la history dal convertitore
        history = self.temperature_converter.get_conversion_history()
        self.assertEqual(len(history), 1)

        log = history[0]

        # assertIn verifica che "timestamp" esista nel dizionario log
        self.assertIn("timestamp", log)
        # Verifica il timestamp
        self.assertTrue(self._is_valid_isoformat(log["timestamp"]))

        # Verifica sezione "from"
        self.assertEqual(log["from"]["unit"], "Celsius")
        self.assertEqual(log["from"]["value"], 100)

        # Verifica sezione "to"
        self.assertEqual(log["to"]["unit"], "Fahrenheit")
        self.assertEqual(log["to"]["value"], 212.0)

    def test_fahrenheit_to_celsius_logging(self) -> None:
        # Verifica che i log °F -> °C vengano creati correttamente
        result = self.temperature_converter.fahrenheit_to_celsius(32)
        self.assertEqual(result, 0.0)

        # Recupera la history dal convertitore
        history = self.temperature_converter.get_conversion_history()
        self.assertEqual(len(history), 1)

        log = history[0]

        # assertIn verifica che "timestamp" esista nel dizionario log
        self.assertIn("timestamp", log)
        # Verifica il timestamp
        self.assertTrue(self._is_valid_isoformat(log["timestamp"]))

        # Verifica sezione "from"
        self.assertEqual(log["from"]["unit"], "Fahrenheit")
        self.assertEqual(log["from"]["value"], 32)

        # Verifica sezione "to"
        self.assertEqual(log["to"]["unit"], "Celsius")
        self.assertEqual(log["to"]["value"], 0.0)

    def _is_valid_isoformat(self, timestamp: str) -> bool:
        try:
            datetime.fromisoformat(timestamp)
            return True
        except ValueError:
            return False

    def tearDown(self) -> None:
        # Pulisce la history e verifica che sia vuota
        self.temperature_converter.clear_conversion_history()
        self.assertEqual(self.temperature_converter.get_conversion_history(), [])

if __name__ == '__main__':
    unittest.main()
