import sys
from pynput import keyboard

buffer = []
__version__ = "0.3.0-alpha"

# TODO:thread para iterar a frase na lista e colorir a palavra com a syntax python


# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == ".":
#         return False
#
#
# with keyboard.Listener(on_release=on_release) as listener:
#     listener.join()

try:
    open(sys.argv[1])
except FileNotFoundError:
    file = open(sys.argv[1], "w")
else:
    file = open(sys.argv[1], "a")

try:
    if 1 < len(sys.argv) < 3:
        line = 0
        empty = 0
        while True:
            if empty == 2:
                break
            _in = input(f"[{line}]: ")
            buffer.insert(line, _in)
            if _in == "":
                empty += 1
                buffer.insert(-1, "")
            else:
                empty = 0
            line += 1
    else:
        print("crid.py <FILE>")
except KeyboardInterrupt:
    _arq = (L for L in buffer)
    for L in _arq:
        file.write(L + "\n")
finally:
    file.close()
