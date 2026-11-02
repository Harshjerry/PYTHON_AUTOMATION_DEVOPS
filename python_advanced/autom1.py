import os
width = os.get_terminal_size().columns

name="Harsh"
print(name.center(width))
print(name.ljust(width))
print(name.rjust(width))
