from pynput import keyboard

def _start():
     print("HelloWorld")
def apertando(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    else:
        _start()

# Collect events until released
with keyboard.Listener(on_press=apertando) as listener:
    listener.join()