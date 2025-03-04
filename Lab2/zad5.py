def transposition_cypher(text: str, key: int):
    if key > len(text): return text

    result = ''

    for char in text:
        ascii_char = ord(char)
        ascii_char += key
        result += chr(ascii_char)

    return result

text = 'abc'
key = 1

print(transposition_cypher(text, key))