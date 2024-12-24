#!/usr/bin/env python3

from playsound import playsound
from sshkeyboard import listen_keyboard
import random
import os

def quack(_):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    if random.random() > 0.1999:
        playsound(f"{current_directory}/../sound/quack.mp3")

def dev_null(_):
    pass

listen_keyboard(
    on_press=quack,
    on_release=dev_null,
)
