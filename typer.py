from random import randrange
from pynput import keyboard
from timer import Timer
import time
import os
from datetime import datetime


t = Timer()

letters_1 = ["в", "а", "о", "л"]


def generate_letter(letters_list):
    """Return random letter from list"""
    random_letter = letters_list[randrange(len(letters_list))]
    return random_letter


def check_result(letter_to_compare):
    with keyboard.Events() as events:
        # Block for as much as possible
        event = events.get(20)

        if event.key == keyboard.KeyCode.from_char(letter_to_compare):
            return True
        if event.key == keyboard.Key.esc:
            return -1
        else:
            return False


def repetition(letters_list):
    """Ask for letter from letter_list and check results.
    Return results"""
    letter = generate_letter(letters_list)
    print(letter)
    t.start()
    result = check_result(letter)
    os.system("clear")
    if result != -1:
        repetition_result = [letter, result, t.stop()]
        return repetition_result
    else:
        t.stop()
        return -1


def exersize(letters_list):
    exersize_result = []
    repetitions_result = []
    exersize_time = datetime.now()

    while True:
        result = repetition(letters_list)
        if result == -1:
            os.system("clear")
            print("ESC is pressed")
            break
        time.sleep(1)
        repetitions_result.append(result)

    for l in repetitions_result:
        l.append(exersize_time)
    print("your results:")
    print(repetitions_result)


exersize(letters_1)

# print(generator(letters_1))

# --- RESOURCES ----
# -- Using classes to access values of functions OOP
# https://stackoverflow.com/questions/10139866/calling-variable-defined-inside-one-function-from-another-function

# --- pynput ---
# -- error with libffi
# brew install libffi
# cp /usr/local/opt/libffi/lib/libffi.7.dylib /Users/Philipp/opt/anaconda3/envs/playground/lib/

# -- error with pyobj c API (expected 20)
# conda install pyobjc-core==6.2

# -- timer
# https://realpython.com/python-timer/