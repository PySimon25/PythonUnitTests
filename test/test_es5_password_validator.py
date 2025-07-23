import unittest
from esercizi_python import PasswordValidator, PasswordTooShortError, PasswordMissingUppercaseError, \
    PasswordMissingLowercaseError, PasswordMissingDigitError

class TestPasswordValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.password_validator = PasswordValidator()

    def test_password_too_short_exception(self) -> None:
        with self.assertRaises(PasswordTooShortError):
            self.password_validator.validate("patate")

    def test_password_missing_uppercase_exception(self) -> None:
        with self.assertRaises(PasswordMissingUppercaseError):
            self.password_validator.validate("patateintecia")

    def test_password_missing_lowercase_exception(self) -> None:
        with self.assertRaises(PasswordMissingLowercaseError):
            self.password_validator.validate("PATATEINTECIA")

    def test_password_missing_digit_exception(self) -> None:
        with self.assertRaises(PasswordMissingDigitError):
            self.password_validator.validate("PaTaTeInTeCiA")

    def test_valid_operation_no_exceptions(self) -> None:
        try:
            self.password_validator.validate("2PatateInTecia")
        except Exception as e:
            self.fail(f"Unexpected exception raised: {e}")

