
import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('238271504e0b4edda5873fb88b86a316.png')
input_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp_range = (10, 40) # 温度范围
temperature = np.random.uniform(temp_range[0], temp_range[1], size=input_image.shape) # 模拟温度分布
print(temperature)
infrared_image = temperature + input_image

kernel_size = 5 # 区域核大小
n_regions = 5 # 设置要分成的区域数量
binsize = 2 # 设置区域尺寸
max_regions = np.zeros(n_regions, dtype=int)
min_regions = np.zeros(n_regions, dtype=int)
mean_regions = np.zeros(n_regions)

for i in range(n_regions):
    mask = cv2.inRange(infrared_image, temp_range[0], temp_range[1])
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    mask = cv2.dilate(mask, kernel)
    regions_temp = np.zeros(infrared_image.shape)
    regions_temp[mask == 255] = i+1
    max_regions[i] = np.max(regions_temp)
    min_regions[i] = np.min(regions_temp)
    mean_regions[i] = np.mean(regions_temp)


max_temp_region = np.argmax(max_regions)
print("最高温度区域为第{}个区域，温度为{}度".format(max_temp_region+1, temperature[max_temp_region][max_regions[max_temp_region]]))
plt.figure(figsize=(10,8))
plt.imshow(infrared_image)
plt.title('Infrared Image')
plt.colorbar()
plt.hist(max_regions, bins=10, alpha=0.5, edgecolor='black')
plt.plot(min_regions, label='min_regions')
plt.plot(mean_regions, label='mean_regions')
plt.legend()
if np.where(max_regions == max_temp_region)[0].size == 0:
    print("找不到最高温度区域！")
else:
    plt.scatter(np.where(max_regions == max_temp_region)[0], np.where(max_regions == max_temp_region)[1], s=100, facecolors='none', edgecolors='r')
plt.scatter(np.where(max_regions == max_temp_region)[0], np.where(max_regions == max_temp_region)[1], s=100, facecolors='none', edgecolors='r')
plt.show()
