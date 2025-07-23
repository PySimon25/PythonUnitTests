class StringProcessor:

    def reverse_string(self, string_to_reverse: str) -> str:
        # Slice & Step Backwards: https://www.w3schools.com/Python/python_howto_reverse_string.asp
        return string_to_reverse[::-1]

    def capitalize_words(self, string_to_capitalize: str) -> str:
        return string_to_capitalize.upper()

    def count_vowels(self, string_to_count: str) -> int:
        # https://www.geeksforgeeks.org/python/python-program-count-number-vowels-using-sets-given-string/
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = sum(1 for character in string_to_count if character in vowels)
        return count
