class PasswordTooShortError(Exception):
    pass

class PasswordMissingUppercaseError(Exception):
    pass

class PasswordMissingLowercaseError(Exception):
    pass

class PasswordMissingDigitError(Exception):
    pass

class PasswordValidator:
 
    def validate(self, password: str) -> None:
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
