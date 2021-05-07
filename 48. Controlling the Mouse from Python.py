import pyautogui
print(pyautogui.size())
width, height = pyautogui.size()
print (width)
print (height)
print (pyautogui.position())

pyautogui.moveTo(10,10)
pyautogui.moveTo(10,10, duration=1.5)
pyautogui.moveRel(200,0)
pyautogui.moveRel(200,0, duration=2)
pyautogui.moveRel(0, -100, duration=1)

print (pyautogui.position())
pyautogui.click(410,0)
pyautogui.click()

