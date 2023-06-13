import cv2
import numpy as np

# 读取红外图像
img = cv2.imread('238271504e0b4edda5873fb88b86a316.png', 0)

# 定义温度范围和颜色映射
min_temp = 30
max_temp = 40
color_map = cv2.COLORMAP_JET

# 将灰度图像转换为伪彩色图像
img_color = cv2.applyColorMap(img, color_map)

# 根据温度范围提取感兴趣区域
mask = cv2.inRange(img_color, min_temp, max_temp)
img_roi = cv2.bitwise_and(img_color, img_color, mask=mask)

# 找到最大轮廓并圈出温度最高区域
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if len(contours) > 0:
    max_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(max_contour)
    cv2.rectangle(img_roi, (x, y), (x + w, y + h), (0, 0, 255), 2)
    (cx, cy), radius = cv2.minEnclosingCircle(max_contour)
    radius = int(radius * 0.8) # 将半径缩小为原来的80%
    center = (int(cx), int(cy))
    radius = int(radius)
    cv2.circle(img_roi, center, radius, (0, 255, 0), 2)

# 打印出最大区域的温度值
max_temp_roi = img[y:y+h, x:x+w]
max_temp_value = np.max(max_temp_roi)
print('Max temperature in ROI:', max_temp_value)

# 显示结果
cv2.imshow('Infrared Image', img_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
