import sys
from os.path import isfile, exists
from pynput import keyboard

buffer = []
__version__ = "0.3.0"


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

def save():
    if input("Save buffer? [y/n]: ").lower().strip() == "y":
        _arq = (L for L in buffer)
        for L in _arq:
            file.write(L + "\n")


try:
    if 1 < len(sys.argv) < 3:
        if len(sys.argv) == 1:
            file_name = "foo.txt"
        else:
            file_name = sys.argv[1]
        if isfile(file_name) and exists(file_name):
            file = open(file_name)
        else:
            file = open(file_name, "w+")
        line = 0
        empty = 0
        while True:
            if empty == 1:
                save()
                break
            _in = input(f"[{line}]: ")
            buffer.insert(line, _in)
            if _in == "":
                empty += 1
            else:
                empty = 0
            line += 1
    else:
        print("crid.py <FILE>")
except KeyboardInterrupt:
    save()
finally:
    file.close()
