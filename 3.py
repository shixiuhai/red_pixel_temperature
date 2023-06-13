import cv2
import numpy as np

# 读取热成像RGB图
img = cv2.imread('238271504e0b4edda5873fb88b86a316.png')

# 将图像转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 计算灰度图的梯度
grad_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0)
grad_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1)

# 计算梯度的幅值和方向
grad_mag, grad_dir = cv2.cartToPolar(grad_x, grad_y)

# 找到最高温度的区域
max_mag = np.max(grad_mag)
max_mag_idx = np.where(grad_mag == max_mag)

# 圈出最高温度的区域
x, y = max_mag_idx[1][0], max_mag_idx[0][0]
cv2.circle(img, (x, y), 10, (0, 0, 255), 2)

# 打印最高温度
print('最高温度：', gray[y, x])

# 显示结果图像
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
