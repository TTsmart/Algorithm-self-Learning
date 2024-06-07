import pyautogui
import time


# 等待一段时间，确保你有时间将焦点移回到桌面
time.sleep(5)
# pyautogui.press('win')
# time.sleep(1)
# pyautogui.write('aTrust')
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(5)
# pyautogui.press('enter')
# time.sleep(10)
# pyautogui.write('lizhenting')
# pyautogui.press('tab')
# pyautogui.write('Lzt000225!')
# pyautogui.press('enter')


# 模拟按下Windows+R键打开“运行”对话框
pyautogui.hotkey('win', 'r')

# 等待运行对话框出现
time.sleep(1)

# 输入'mstsc'打开远程桌面连接
pyautogui.write('mstsc')

# 按下回车键执行
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('y')
# 等待远程桌面连接窗口打开（可能需要根据你的计算机速度调整等待时间）
time.sleep(2)