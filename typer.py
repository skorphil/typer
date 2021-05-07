from random import randrange
from pynput import keyboard
from timer import Timer
import time
import os
from datetime import datetime
from pandas import DataFrame
import sqlite3


t = Timer()

letters_1 = ["в", "а", "о", "л"]


def generate_letter(letters_list):
    """Return random letter from list"""
    random_letter = letters_list[randrange(len(letters_list))]
    return random_letter


def check_result(letter_to_compare):
    """Take letter and compare to user input. Returns True/False and -1"""

    with keyboard.Events() as events:
        # Block for as much as possible
        event = events.get(3)

        if event is None:
            print("You did not press a key within one second")
            return False
        if event.key == keyboard.KeyCode.from_char(letter_to_compare):
            return True
        if event.key == keyboard.Key.esc:
            return -1
        else:
            return False


def repetition(letters_list):
    """Choose random letter from letter_list and check results.
    Return results or -1"""
    letter = generate_letter(letters_list)
    os.system("clear")
    print(letter)
    t.start()
    result = check_result(letter)

    if result != -1:
        repetition_result = [letter, result, t.stop(), datetime.now()]
        return repetition_result
    else:
        t.stop()
        return -1


def exersize(letters_list):
    repetitions_result = []
    exersize_time = datetime.now()
    repetitions_count = 0

    while True:
        result = repetition(letters_list)
        if result == -1:
            os.system("clear")
            print("ESC is pressed")
            break
        time.sleep(0.7)
        repetitions_result.append(result)

    exersize_result = DataFrame(
        repetitions_result, columns=["Letter", "Success", "Time", "Date"]
    )

    exersize_result["Exersise_date"] = exersize_time
    print("your results:")
    print(exersize_result["Success"].value_counts(normalize=True) * 100)
    return exersize_result


def write_to_db(results_df):

    conn = sqlite3.connect("typer.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Letters_stat (
            Letter TEXT, 
            Success INTEGER, 
            Time REAL, 
            Date TIMESTAMP,
            Exersise_date TIMESTAMP
            )"""
    )
    conn.commit()
    results_df.to_sql("Letters_stat", conn, if_exists="append", index=False)
    c.close()  # and your cursor when you're done!
    conn.close()  # always a good habit to close your connections

    # print(exersize_result)
    # exersize_result.info()


write_to_db(exersize(letters_1))

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