import numpy as np

# 定义指数函数的底数和指数值
base = 2
exp = 0.02

# 读取灰度值矩阵
gray_array = np.load('gray_array.npy')

# 将灰度值映射到0到0.64的范围内
temp_array = gray_array / 255 * 0.64

# 将0到0.64的范围内的值转换为对应的温度值
temp_array = np.exp(temp_array * np.log(2)) ** 0.02 - 1

# 将温度值矩阵保存为文件
np.save('temp_array.npy', temp_array)