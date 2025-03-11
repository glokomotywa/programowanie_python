def szyfruj(tekst, klucz):
    zaszyfrowany = ""
    for char in tekst:
        zaszyfrowany += chr((ord(char) + klucz - 65) % 26 + 65) if char.isupper() else chr((ord(char) + klucz - 97) % 26 + 97)
    return zaszyfrowany
