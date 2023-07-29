import pyautogui as pgui
import time
import json


def load_config(file_path):
    with open(file_path, 'r') as file:
        config_data = json.load(file)
    return config_data


def spammer():
    while True:
        chat = pgui.locateOnScreen('chatbar.png', confidence=0.9)
        frequent = pgui.locateOnScreen('Untitled2.png', confidence=0.9)
        if chat != None:
            pgui.click(chat)
            if len(one) != 0:
                pgui.write(one)
            else:
                print("you need at least one sentence")
        else:
            print('cannot find chat')
        send = pgui.locateOnScreen('Untitled1.png', confidence=0.9)
        if send != None:
            pgui.click(send)
        else:
            print("cannot find send")
        frequent = pgui.locateOnScreen('Untitled2.png', confidence=0.9)
        if frequent != None:
            time.sleep(30)


        chat = pgui.locateOnScreen('chatbar.png', confidence=0.9)
        if chat != None:
            pgui.click(chat)
            pgui.write(two)
        else:
            print('cannot find chat')

        send = pgui.locateOnScreen('Untitled1.png', confidence=0.9)
        if send != None:
            pgui.click(send)
        else:
            print("cannot find send")
        frequent = pgui.locateOnScreen('Untitled2.png', confidence=0.9)
        if frequent != None:
            time.sleep(30)


        chat = pgui.locateOnScreen('chatbar.png', confidence=0.9)
        if chat != None:
            pgui.click(chat)
            pgui.write(three)
        else:
            print('cannot find chat')
        send = pgui.locateOnScreen('Untitled1.png', confidence=0.9)
        if send != None:
            pgui.click(send)
        else:
            print("cannot find send")
        frequent = pgui.locateOnScreen('Untitled2.png', confidence=0.9)
        if frequent != None:
            time.sleep(30)

        chat = pgui.locateOnScreen('chatbar.png', confidence=0.9)
        if chat != None:
            pgui.click(chat)
            pgui.write(four)
        else:
            print('cannot find chat')
        send = pgui.locateOnScreen('Untitled1.png', confidence=0.9)
        if send != None:
            pgui.click(send)
        else:
            print("cannot find send")
        frequent = pgui.locateOnScreen('Untitled2.png', confidence=0.9)
        if frequent != None:
            time.sleep(30)

        chat = pgui.locateOnScreen('chatbar.png', confidence=0.9)
        if chat != None:
            pgui.click(chat)
            pgui.write(five)
        else:
            print('cannot find chat')
        send = pgui.locateOnScreen('Untitled1.png', confidence=0.9)
        if send != None:
            pgui.click(send)
        else:
            print("cannot find send")
        frequent = pgui.locateOnScreen('Untitled2.png', confidence=0.9)
        if frequent != None:
            time.sleep(30)

        chat = pgui.locateOnScreen('chatbar.png', confidence=0.9)
        if chat != None:
            pgui.click(chat)
            pgui.write(six)
        else:
            print('cannot find chat')
        send = pgui.locateOnScreen('Untitled1.png', confidence=0.9)
        if send != None:
            pgui.click(send)
        else:
            print("cannot find send")
        frequent = pgui.locateOnScreen('Untitled2.png', confidence=0.9)
        if frequent != None:
            time.sleep(30)

config = load_config('config.json')
pgui.FAILSAFE = config['failsafe']
delay = config['delay']
timeout = config['timeout']
run = config['run']

if run == False:
    print(f"Please open the config file and change 'run' to true, while you are there, try setting some other options too!")
    exit(1)

print(f"Failsafe: {pgui.FAILSAFE}")
print(f"Delay: {delay} Seconds")
print(f"Timeout: {timeout} Seconds")
print(f"====Oxydium 2023====")

one = config['message_one']
if one != "null":
    print("message one loaded from config")
else:
    print("there needs to be at least one message, look at README.TXT")
    exit(1)

two = config['message_two']
if two != "null":
    print("message two loaded from config")
else:
    print("read NULL from config, continuing")
    spammer()

three = config['message_three']
if three != "null":
    print("message three loaded from config")
else:
    print("read NULL from config, continuing")
    spammer()

four = config['message_four']
if four != "null":
    print("message four loaded from config")
else:
    print("read NULL from config, continuing")
    spammer()

five = config['message_five']
if five != "null":
    print("message five loaded from config")
else:
    print("read NULL from config, continuing")
    spammer()

six = config['message_six']
if six != "null":
    print("message six loaded from config")
else:
    print("read NULL from config, continuing")
    spammer()

spammer()