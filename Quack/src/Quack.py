from pynput import keyboard
import pygame
import random
import os

current_directory = os.path.dirname(os.path.realpath(__file__))


def handle_key():
    if random.random() > 0.9999:
        quack()
   

def quack():
    pygame.mixer.init()
    pygame.mixer.music.load(f"{current_directory}/../sound/quack.mp3")
    pygame.mixer.music.play()


def on_press(key):
    try:
        handle_key()
    except AttributeError as e:
        print(e)


def on_release(key):
    pass


quack()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
