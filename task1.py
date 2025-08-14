Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> message = input("HELLO WORLD")
HELLO WORLD
>>> shift = int(input("3"))
3
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    shift = int(input("3"))
ValueError: invalid literal for int() with base 10: ''
>>> encrypted = "PRATHAM RAJPUT"
>>> for char in message:
...     if char.isalpha():
...         base = ord('A') if char.isupper() else ord('a')
...         encrypted += chr((ord(char) - base + shift) % 26 + base)
...         else:
...             encrypted + char
>>> print("Encrypted:", encrypted)
Encrypted: PRATHAM RAJPUT
>>> decrypted = "HELLO WORLD"
>>> for char in encrypted:
...     if char.isalpha():
...         base = ord('A') if char.isupper() else ord('a')
...         decrypted += chr((ord(char) - base - shift) % 26 + base)
...         else:
...             decrypted += char
>>> print("Decrypted:",decrypted)
Decrypted: HELLO WORLD