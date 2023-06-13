import cv2
import numpy as np

# Planck公式：根据物体的辐射能量和温度之间的关系，使用Planck公式计算像素的温度值。
def planck(gray, wavelength, temperature):
    h = 6.62607004e-34  # Planck constant
    c = 299792458  # speed of light
    k = 1.38064852e-23  # Boltzmann constant
    a = 2 * h * c ** 2 / wavelength ** 5
    b = h * c / (wavelength * k * temperature)
    intensity = a / (np.exp(b) - 1)
    return intensity * np.exp(gray / 255 * 5) - 1

# 基于灰度值的线性拟合：根据红外图像的灰度值和已知的温度值之间的关系，使用线性拟合方法计算像素的温度值。
def linear_fit(gray, a, b):
    temperature = a * gray + b
    return temperature * np.exp(gray / 255 * 5) - 1

# 基于反射率的校正：考虑物体表面的反射率对温度测量的影响，使用反射率校正方法对像素的温度值进行校正。
# 物体反射率默认是0.95
def reflectance_correction(gray, reflectance):
    temperature = (gray - reflectance) / (1 - reflectance) * 100
    return temperature * np.exp(gray / 255 * 5) - 1


# 读取视频文件
cap = cv2.VideoCapture('320722224-1-192.mp4')

# 循环读取每一帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # 计算每个像素的温度值
    # wavelength = 10.6e-6  # 红外相机的波长
    # temperature = planck(gray, wavelength, 25)  # 使用Planck公式计算温度值
    # # 或者
    # a = 0.04  # 线性拟合参数a
    # b = -273  # 线性拟合参数b
    # temperature = linear_fit(gray, a, b)  # 使用线性拟合方法计算温度值
    # # 或者
    # reflectance = 0.1  # 物体表面的反射率
    # temperature = reflectance_correction(gray, reflectance)  # 使用反射率校正方法计算温度值

    # 计算每个像素的温度值
    temperature = np.exp(gray / 255 * 5) - 1

    # 找到温度最高的像素坐标
    max_temp = np.max(temperature)
    max_temp_pos = np.where(temperature == max_temp)

    # 在图像上圈出温度最高的区域
    x, y = max_temp_pos[::-1]
    # cv2.circle(frame, (x, y), 10, (0, 0, 255), 2)

    # 打印出温度
    print('Max temperature:', max_temp)

    # 显示处理后的图像
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# import cv2

# # 读取红外图片
# img = cv2.imread('infrared_image.jpg', cv2.IMREAD_GRAYSCALE)

# # 获取图片宽度和高度
# height, width = img.shape[:2]

# # 遍历每个像素，获取温度值
# for y in range(height):
#     for x in range(width):
#         temperature = img[y][x]
#         print('Pixel at ({}, {}) has temperature: {}'.format(x, y, temperature))
