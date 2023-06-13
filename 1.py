import numpy as np
import cv2
import matplotlib.pyplot as plt

# 读取热成像图像
img = cv2.imread('PT151104000028oUrX.jpg')

# 对数据进行预处理
# 噪声去除、背景去除、光强校正等
input_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 进行温度分布模拟
# 使用半导体材料的热导率或物理计算机模拟等方法，模拟物体内部的热力学过程，从而确定物体内部的温度分布
temperature = np.random.uniform(10, 30, size=input_image.shape) # 模拟温度分布

# 重建温度信息
infrared_image = temperature + input_image

# 进行区域核模拟
n_regions = 5 # 设置要分成的区域数量
binsize = 2 # 设置区域尺寸

# 在温度最高区域进行处理
max_regions = np.zeros(n_regions, dtype=int)
min_regions = np.zeros(n_regions, dtype=int)
mean_regions = np.zeros(n_regions)

for i in range(n_regions):
    mask = cv2.inRange(infrared_image, 20, 30)
    regions_temp = np.zeros(infrared_image.shape)
    regions_temp[mask == 255] = i+1
    max_regions[i] = np.max(regions_temp)
    min_regions[i] = np.min(regions_temp)
    mean_regions[i] = np.mean(regions_temp)



# 显示结果
plt.figure(figsize=(10,8))
plt.imshow(infrared_image)
plt.title('Infrared Image')
plt.colorbar()
plt.hist(max_regions, bins=10, alpha=0.5, edgecolor='black')
# plt.plot(min_regions, label='min_regions')
# plt.plot(mean_regions, label='mean_regions')
plt.legend()
plt.show()                                            
                                        