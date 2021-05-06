from pynput import keyboard

# The event listener will be running in this block
with keyboard.Events() as events:
    # Block at most one second
    event = events.get(1.0)
    if event is None:
        print("You did not press a key within one second")
    else:
        print("Received event {}".format(event))
