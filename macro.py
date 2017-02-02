from pynput import keyboard
from pynput.keyboard import Controller


def on_press(key):
    """
    when a key is pressed this method is called
    :param key: The key currently pressed
    :return:
    """

    try:
        # declare global var so we can use it again

        global lastPressed
        global combination
        global toWrite

        # print the currently pressed key
        print('alphanumeric key {0} pressed'.format(key.char))

        # setting the text to write when the macro is being triggerd
        toWrite = "hello"

        # add the currently pressed key
        lastPressed += '{0}'.format(key.char)

        # the combination to be pressed in order to trigger the macro
        # this specific one is ctrl+k+b
        combination = "Key.ctrlkb"

        # writingFile.write(str('{0}'.format(key.char)))
        # if the combination is pressed
        if lastPressed[len(lastPressed) - len(combination):] == combination:
            # write the predefined macro text
            write(toWrite)

            # reset the lastPressed string
            lastPressed = ""

    except AttributeError:
        # print the currently pressed key
        print('special key {0} pressed'.format(
            key))
        # add the currently pressed key
        lastPressed += '{0}'.format(key)


def on_release(key):
    # print the currently pressed key
    print('{0} released'.format(
        key))
    # if the currently pressed kry is esc then stop
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def write(toType):
    writer = Controller()
    writer.type(toType)


toWrite = ""
combination = ""
lastPressed = ""

# listen to pressed keys
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
