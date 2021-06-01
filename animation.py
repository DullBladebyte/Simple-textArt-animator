import time
from art import *
import os
os.system('cls')


text = ""
frame = ""
print("Type in the text you want to be animated")

while True:
    text = input()
    
    break

os.system('cls')
while True:
    for i in text:
        wait = open("wait.txt", "r")
        wait = wait.read()
        frame += i
        if not i == " ":
            print("".join(text2art(frame)))
            time.sleep(int(wait)/1000)
            os.system('cls')
    frame = ""
    time.sleep(int(wait)/1000)

        
