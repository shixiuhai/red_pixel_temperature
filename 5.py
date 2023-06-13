import cv2
import numpy as np

# 读取红外图像
img = cv2.imread('3.png', cv2.IMREAD_GRAYSCALE)

# 定义温度范围和颜色映射
temp_min = 20
temp_max = 100
color_map = cv2.applyColorMap(cv2.convertScaleAbs(img, alpha=(255/(temp_max-temp_min))), cv2.COLORMAP_JET)

# 定义区域核模拟核
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# 找到温度最高的区域并圈出该区域
img_threshold = cv2.threshold(img, 35, 255, cv2.THRESH_BINARY)[1]
img_threshold = cv2.morphologyEx(img_threshold, cv2.MORPH_CLOSE, kernel)
contours, hierarchy = cv2.findContours(img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_contour = max(contours, key=cv2.contourArea)
(x, y), radius = cv2.minEnclosingCircle(max_contour)
center = (int(x), int(y))
radius = int(radius)
if radius > 50: # 如果圆的半径太大，则缩小圆的半径
    radius = 50
cv2.circle(color_map, center, radius, (0, 0, 255), 2)

# 打印出温度最高区域的温度
max_temp = np.max(img[int(y-radius):int(y+radius), int(x-radius):int(x+radius)])
if max_temp > temp_max: # 如果最高温度超过了温度范围，则将其设为温度范围的最大值
    max_temp = temp_max
print('The highest temperature in the region is:', max_temp)




cv2.circle(img, center, radius, (0, 0, 255), 2)
cv2.imshow('Result', img)
# 显示结果图像
# cv2.imshow('Result', color_map)
cv2.waitKey(0)
cv2.destroyAllWindows()
