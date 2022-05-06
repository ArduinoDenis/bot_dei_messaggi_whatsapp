import pyautogui as spam
import time

limit = input("inserire il numero di messaggi da inviare")
msg = input("Messaggio che vuoi inviare")

i = 0

time.sleep(5)

while i<int(limit):

    spam.typewrite(msg)
    spam.press('Enter')

i+=1
