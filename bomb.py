import pyautogui #pip install pyautogui
import time
time.sleep(2)

for i in range (250):	#250 is the number of messages you will send
	pyautogui.hotkey('ctrl','v')
	pyautogui.press('enter')
#copy message from here 
#and go to the message box