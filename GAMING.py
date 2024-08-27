from pynput.keyboard import Controller, Key, Listener
import time

# Define a global variable to control the loop
keep_running = True

# Define the function to stop the script when the escape key is pressed
def on_press(key):
    global keep_running
    if key == Key.esc:  # Set the escape key as the failsafe
        keep_running = False
    #honestly, i suck at programming so you have to wait for the end of the loop

# Start a listener to detect the escape key press
listener = Listener(on_press=on_press)
listener.start()

# Initialize the keyboard controller
keyboard = Controller()

# Wait to switch to Citra
time.sleep(2)
print("Started sequence")

while keep_running:

    # Inputs for Silque
    keyboard.press(Key.left)
    time.sleep(0.05)
    keyboard.release(Key.left)
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)

    # Wait for Silque's animation
    time.sleep(2.25)

    # Inputs for Faye
    keyboard.press(Key.left)
    time.sleep(0.05)
    keyboard.release(Key.left)
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)

    # Wait for Faye's animation
    time.sleep(2.25)

    # Inputs to end the turn
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)
    keyboard.press(Key.up)
    time.sleep(0.05)
    keyboard.release(Key.up)
    time.sleep(0.05)
    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    time.sleep(0.05)

    #wait for screen transition animation
    time.sleep(2)

print("Script stopped successfully.")
listener.stop()  # Stop the listener
