print(''.join(list(map(lambda c: chr(120042 + ord(c) - ord('a')) if 97 <= ord(c) <= 122 else c, [c for c in input('Enter text to be converted: ')]))))
