import pyperclip
import random

def main():
    prevClipboard = ""
    while True:
        clipboard = pyperclip.waitForNewPaste()
        print(clipboard)
        r = random.random()
        print(r)
        if r > 0.999999:
            pyperclip.copy(prevClipboard)
        prevClipboard = clipboard

if __name__ == "__main__":
    main()
