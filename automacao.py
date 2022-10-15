import pyautogui
import time
pyautogui.PAUSE = 1
#entrar no google drive
pyautogui.press("win")
pyautogui.write("chrom")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press("enter")
#entrar na area de trabalho
pyautogui.hotkey("win", "d")
time.sleep(1)
#pegar e arrastar o arquivo
pyautogui.moveTo(x=44, y=354)
pyautogui.mouseDown()
pyautogui.moveTo(x=1127, y=461)
#abrir o google drive e colocar e soltar o arquivo
pyautogui.hotkey("alt","tab")
pyautogui.mouseUp()