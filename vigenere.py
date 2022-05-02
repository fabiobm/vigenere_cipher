from string import ascii_lowercase


class Vigenere:
    """
    Encrypts and decrypts text using the [Vigenère cipher](https://en.wikipedia.org/wiki/Vigenère_cipher).

    The alphabet is by default the lowercase Latin alphabet, but can be any
    list of (unique) characters or strings.
    """

    def __init__(self, alphabet=list(ascii_lowercase)):
        if not isinstance(alphabet, list):
            raise ValueError("Alphabet must be a list of characters or strings")
        if len(set(alphabet)) != len(alphabet):
            raise ValueError("Alphabet must not have duplicated symbols")

        self.alphabet = alphabet
        self.words = any(len(symbol) > 1 for symbol in alphabet)

    def _transform(self, text, key, decrypting=False):
        if key == "" or key == []:
            raise ValueError("Key must not be empty")

        if not isinstance(key, str) and not isinstance(key, list):
            raise ValueError("Key must be a string or a list of strings")

        if not isinstance(text, str) and not isinstance(text, list):
            raise ValueError("Text must be a string or a list of strings")

        transformed = []
        for i, symbol in enumerate(text):
            try:
                symbol_idx = self.alphabet.index(symbol)
            except ValueError:
                raise ValueError("Symbols in text must be in the alphabet")

            try:
                key_symbol_idx = self.alphabet.index(key[i % len(key)])
            except ValueError:
                raise ValueError("Symbols in key must be in the alphabet")

            idx = (
                symbol_idx + (key_symbol_idx if not decrypting else -key_symbol_idx)
            ) % len(self.alphabet)

            transformed.append(self.alphabet[idx])

        return transformed if self.words else "".join(transformed)

    def encrypt(self, text, key):
        """
        Encrypts the message `text` using a Vigenère cipher with key `key`.

        Both `text` and `key` must be either strings or lists of words (and both
        must be the same type). The symbols (characters or words) in `text` and `key`
        must all be present in the alphabet supplied when creating the instance. The
        `key` must not be empty.
        """

        return self._transform(text, key)

    def decrypt(self, text, key):
        """
        Decrypts the message `text` using a Vigenère cipher with key `key`.

        Both `text` and `key` must be either strings or lists of words (and both
        must be the same type). The symbols (characters or words) in `text` and `key`
        must all be present in the alphabet supplied when creating the instance. The
        `key` must not be empty.
        """

        return self._transform(text, key, decrypting=True)
