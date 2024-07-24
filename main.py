import pyautogui
import cv2
import numpy as np
import time


def detect_blue_square():
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 定义蓝色阈值范围
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # 在 HSV 颜色空间中寻找蓝色区域
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 寻找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # 找到最大的轮廓
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        # 返回蓝色方块的中心坐标
        return (x + w // 2, y + h // 2)
    else:
        return None


def click_blue_square():
    end_time = time.time() + 69
    while time.time() < end_time:
        blue_square_pos = detect_blue_square()
        if blue_square_pos:
            pyautogui.click(blue_square_pos)
            # 延迟
            time.sleep(0.002)


if __name__ == "__main__":
    click_blue_square()
