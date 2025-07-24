class PasswordTooShortError(Exception):
    """Raised when the password is shorter than the required minimum length."""
    pass

class PasswordMissingUppercaseError(Exception):
    """Raised when the password does not contain an uppercase letter."""
    pass

class PasswordMissingLowercaseError(Exception):
    """Raised when the password does not contain a lowercase letter."""
    pass

class PasswordMissingDigitError(Exception):
    """Raised when the password does not contain a digit."""
    pass

class PasswordValidator:
    """
    Validates passwords against a set of security rules.

    Rules:
        - Minimum length of 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit

    Raises:
        PasswordTooShortError: If the password is too short.
        PasswordMissingUppercaseError: If the password lacks uppercase letters.
        PasswordMissingLowercaseError: If the password lacks lowercase letters.
        PasswordMissingDigitError: If the password lacks digits.
    """
 
    def validate(self, password: str) -> None:
        """
        Validates the given password based on defined rules.

        Args:
            password (str): The password to validate.

        Raises:
            PasswordTooShortError: If the password has fewer than 8 characters.
            PasswordMissingUppercaseError: If no uppercase letters are present.
            PasswordMissingLowercaseError: If no lowercase letters are present.
            PasswordMissingDigitError: If no digits are present.
        """
        if not self._is_min_length(password):
            raise PasswordTooShortError("La password deve contenere almeno 8 caratteri.")
        
        if not self._contains_uppercase_characters(password):
            raise PasswordMissingUppercaseError("La password deve contenere almeno una lettera maiuscola.")
        
        if not self._contains_lowercase_characters(password):
            raise PasswordMissingLowercaseError("La password deve contenere almeno una lettera minuscola.")
        
        if not self._contains_digits(password):
            raise PasswordMissingDigitError("La password deve contenere almeno un numero.")

    def _is_min_length(self, password: str) -> bool:
        return len(password) >= 8

    def _contains_uppercase_characters(self, password: str) -> bool:
        return any(char.isupper() for char in password)

    def _contains_lowercase_characters(self, password: str) -> bool:
        return any(char.islower() for char in password)
    
    def _contains_digits(self, password: str) -> bool:
        return any(char.isdigit() for char in password)
