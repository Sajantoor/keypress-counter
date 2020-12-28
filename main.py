import keyboard
import time # for wait

key: str = "" # key we are tracking
breakKey = 'esc' # Counting stops if this key is pressed

def getKey(): 
    global key
    global breakKey
    key = input("Input the key you want to count then press enter: ")
    if key == breakKey: 
        breakKey = "`"
        print("To stop, press '`'")
    try: 
        keyboard.is_pressed(key)
    except: 
        print("Not a valid key, try again!")
        getKey()

getKey()
count = 0 # Counter 
# opens file in writing mode
file = open('keypress.txt', 'w')
file.write("0")
file.seek(0)

while True: 
    if keyboard.is_pressed(key):
        count += 1
        print(count)
        isPressed = True
        # update text
        file.write(str(count))
        file.seek(0)
        # avoid repeated keypress by holding down
        time.sleep(0.1)

    elif keyboard.is_pressed(breakKey):
        print("Broke")
        break

file.close()