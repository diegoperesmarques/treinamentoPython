import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1


pyautogui.hotkey('alt','tab')
pyautogui.hotkey('ctrl','t')
#link = 'https://google.com'
#pyperclip.copy(link)
#pyautogui.hotkey('ctrl','v')

pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')
time.sleep(10)
#pyautogui.position() - descobrir a posição do mouse

#Abrindo a pasta
pyautogui.click(x=462, y=715, clicks=2)
time.sleep(5)

#clique no arquivo
pyautogui.click(x=379, y=312)

#clique nos três (03) pontos
pyautogui.click(x=824, y=221)

#clique na opção "download"
pyautogui.click(x=630, y=597)
time.sleep(5)

#baixar o arquivo
pyautogui.press('enter')
pyautogui.press('enter')


