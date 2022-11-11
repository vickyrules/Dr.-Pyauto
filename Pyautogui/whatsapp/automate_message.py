#please maximize your browsers window before running the program.
#Do not close the browser in-between
#Do not move cursor untill the program is running

########## Use it justfor fun, not to bother someone#############
#              '''Happpy Coding'''            #


#install the following modules first
# use the following terminal command

# pip install pyautogui
# pip install time
# pip install sys
from pyautogui import *
from time import sleep
import sys
# import webbrowser as wb

#add contacts names
contacts = ["name"]

#type your message here
message = "hey Bro"

#how many times you want to send
sendCnt = 10

# method to find the search bar location
def click_search_name(name):
    x1, y1 = [211,250]
    moveTo(x1, y1)
    click()
    typewrite(name, interval=0.2)
    sleep(2)
    press('enter')

# method to find and send message
def click_send_message(msg):
    x3, y3 = [950,750]
    moveTo(x3, y3)
    click()
    sleep(2)
    typewrite(msg)
    press('enter')

#iterating through the contact list

for name in contacts:
    try:
        click_search_name(name)
    except:
        print("Unable to locate search bar or name")
    try:
        for send in range(sendCnt):
            click_send_message(str(i)+". "+message)
    except:
        print("Unable to locate message bar")
    
