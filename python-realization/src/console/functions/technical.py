import os
import sys
import time


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


def restart(text):
    print(text)
    time.sleep(4)
    clear = lambda: os.system('cls')
    clear()
    os.execv(sys.executable, [os.path.basename(sys.executable)] + sys.argv)
