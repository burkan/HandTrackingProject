

# Move the cursor
# click buttons
# hold buttons
# Scroll

import pyautogui

print (pyautogui.position())
print (pyautogui.size())
print (pyautogui.onScreen(2000,10))
x_carpeta = 1533
y_carpeta = 224

x_fichero = 950
y_fichero = 250

pyautogui.moveTo(x_fichero,y_fichero,duration=2)
#pyautogui.click()
pyautogui.dragTo(x_carpeta,y_carpeta,duration=2)
#pyautogui.moveTo(x_carpeta,y_carpeta,duration=2)

#pyautogui.rightClick()
#pyautogui.moveRel(500,500,duration=2)