import cv2
import numpy as np

# 读取红外RGB图像
img = cv2.imread('3.png')

# 将RGB图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 定义温度范围和对应的颜色
colors = np.array([[0, 0, 255], [0, 255, 255], [0, 255, 0], [255, 255, 0], [255, 0, 0]])
temps = np.array([20, 25, 30, 35, 40])

# 调整颜色映射表的大小为256
# colors = cv2.resize(colors, (256, 1))

# 将灰度图像转换为伪彩色图像
heatmap = cv2.applyColorMap(gray, colors)

# 将伪彩色图像转换为真实温度图像
temp_map = np.zeros_like(gray, dtype=np.float32)
for i in range(len(temps)):
    temp_map[gray == i] = temps[i]
temp_map = cv2.convertScaleAbs(temp_map)

# 显示结果
cv2.imshow('Infrared RGB Image', img)
cv2.imshow('Heatmap', heatmap)
cv2.imshow('Temperature Map', temp_map)
cv2.waitKey(0)
cv2.destroyAllWindows()
