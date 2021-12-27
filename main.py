import sys

from pynput import keyboard
import threading

buffer = []
__version__ = "0.2.0-alpha"


# TODO:thread para iterar a frase na lista e colorir a palavra com a syntax python


def on_release(key):
    print('{0} released'.format(
        key))
    if key == ".":
        _arq = (L for L in buffer)
        for L in _arq:
            file.write(L + "\n")
        return False


# listener = keyboard.Listener(on_release=on_release)
if 1 < len(sys.argv) < 3:
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        file = open(sys.argv[1], "w")
    else:
        file = open(sys.argv[1], "a")
    line = 0
    empty = 0
    # listener.start()
    # listener.join(1)
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
    print("main.py <FILE>")
