from pynput import keyboard
from pynput.keyboard import Key
import sys

# file = open("teste.txt", "w")
buffer = [[]]

# TODO:criar uma thread para separar as palavras na lista e colori-las com a syntaxe python



def on_press(key):
    try:
        if key == Key.up:
            print("seta pra cima")
        elif key == Key.down:
            print("seta pra baixo")
        elif key == "\x1b[B":
            print("diferente")

    except AttributeError:
        # print('special key pressed: {0}'.format(key))
        if key == Key.ctrl or key == Key.shift:
            print("parado")
        pass


listener = keyboard.Listener(on_press=on_press)
if len(sys.argv) == 1:
    line = 0
    empty = 0
    listener.start()
    while True:
        if empty == 2:
            break
        _in = input(f"[{line}]: ")
        buffer[line].append(_in)
        if _in == "":
            empty += 1
        else:
            empty = 0
        buffer.append([])
        line += 1
        print(buffer)

buffer.pop()
buffer.pop()
listener.stop()
_arq = (L for L in buffer)
for L in _arq:
    # L.append("\n")
    # file.writelines(L)
    print(L)

# listener.stop()
