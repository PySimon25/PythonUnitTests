import unittest
from esercizi_python import PasswordValidator, PasswordTooShortError, PasswordMissingUppercaseError, \
    PasswordMissingLowercaseError, PasswordMissingDigitError

class TestPasswordValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.password_validator = PasswordValidator()

    def test_password_too_short_exception(self) -> None:
        with self.assertRaises(PasswordTooShortError) as context:
            self.password_validator.validate("patate")
        self.assertEqual(str(context.exception), "La password deve contenere almeno 8 caratteri.")

    def test_password_missing_uppercase_exception(self) -> None:
        with self.assertRaises(PasswordMissingUppercaseError) as context:
            self.password_validator.validate("patateintecia")
        self.assertEqual(str(context.exception), "La password deve contenere almeno una lettera maiuscola.")

    def test_password_missing_lowercase_exception(self) -> None:
        with self.assertRaises(PasswordMissingLowercaseError) as context:
            self.password_validator.validate("PATATEINTECIA")
        self.assertEqual(str(context.exception), "La password deve contenere almeno una lettera minuscola.")

    def test_password_missing_digit_exception(self) -> None:
        with self.assertRaises(PasswordMissingDigitError) as context:
            self.password_validator.validate("PaTaTeInTeCiA")
        self.assertEqual(str(context.exception), "La password deve contenere almeno un numero.")

    def test_valid_operation_no_exceptions(self) -> None:
        try:
            self.password_validator.validate("2PatateInTecia")
        except Exception as e:
            self.fail(f"Unexpected exception raised: {e}")

