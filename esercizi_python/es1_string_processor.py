class StringProcessor:
    """
    A utility class for performing common string operations such as reversing strings,
    converting to uppercase, and counting vowels.
    """

    def reverse_string(self, string_to_reverse: str) -> str:
        """
        Reverses the given string.

        Args:
            string_to_reverse (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        # Slice & Step Backwards: https://www.w3schools.com/Python/python_howto_reverse_string.asp
        return string_to_reverse[::-1]

    def capitalize_words(self, string_to_capitalize: str) -> str:
        """
        Converts all characters in the string to uppercase.

        Args:
            string_to_capitalize (str): The string to convert.

        Returns:
            str: The string in uppercase.
        """
        return string_to_capitalize.upper()

    def count_vowels(self, string_to_count: str) -> int:
        """
        Counts the number of vowels in the given string.

        Args:
            string_to_count (str): The string in which to count vowels.

        Returns:
            int: The number of vowels found in the string.
        """
        # https://www.geeksforgeeks.org/python/python-program-count-number-vowels-using-sets-given-string/
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = sum(1 for character in string_to_count if character in vowels)
        return count
