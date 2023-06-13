import cv2
import numpy as np
cap = cv2.VideoCapture('istockphoto-1225043479-640_adpp_is.mp4')
convert_rgb = cap.get(cv2.CAP_PROP_CONVERT_RGB)
if convert_rgb == 1:
    channel_count = 3
    print(3)
else:
    channel_count = 1
    print(1)
cap.set(cv2.CAP_PROP_FORMAT, cv2.CV_32F)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)
fps = cap.get(cv2.CAP_PROP_FPS)
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 初始化变量以查找最大温度及其位置
square_size = 10 # 区域尺寸
# num_squares = 30 # 正方形遍历次数
num_squares=int(max(width, height) / square_size)
print(num_squares)
print("-------------")

# 物体反射率默认是0.95
def reflectance_correction(gray, reflectance=0.1):
    
    # temp_array = np.exp(temp_array / 255 * 5) - 1 
    temperature = (gray - reflectance) / (1 - reflectance) * 100
    return temperature * np.exp(gray / 255 * 5) - 1

# 循环遍历所有帧并提取温度数据
for i in range(num_frames):
    # 读取下一帧
    ret, frame = cap.read()
    # 从帧中提取温度数据
    # 从帧中提取温度数据
    temp_array = frame[:, :, 0]
    # 这个方法可以校准的温度范围是从-20℃到2000℃左右
    # temp_array = np.exp(temp_array / 255 * 5) - 1 
    # 映射温度按照-20到500
    temp_array = np.exp(temp_array * np.log(2)) ** 0.02 - 1
    
    # temp_array = reflectance_correction(temp_array)
    
    max_temp = 0
    max_temp_loc = (0, 0)  # 正方形中心坐标

    for k in range(num_squares):
        y1 = int(k * (height / num_squares))
        y2 = int((k + 1) * (height / num_squares))
        for j in range(num_squares):
            # Calculate square coordinates
            x1 = int(j * (width / num_squares))
            x2 = int((j + 1) * (width / num_squares))

            # Extract square temperature data and calculate average temperature
            square_temp = temp_array[y1:y2, x1:x2]
            avg_temp = np.mean(square_temp)

            # Check if average temperature is higher than current maximum temperature
            if avg_temp > max_temp:
                max_temp = avg_temp
                max_temp_loc = (int((x1 + x2) / 2), int((y1 + y2) / 2))

    # Print maximum temperature and its location
    # print('Frame', i + 1, ': Maximum temperature is', (max_temp-32)/1.8, 'at location', max_temp_loc)
    print('Frame', i + 1, ': Maximum temperature is',max_temp, 'at location', max_temp_loc)

    # Draw square around maximum temperature location
    square_size_half = int(square_size / 2)
    frame = cv2.rectangle(frame, (max_temp_loc[0] - square_size_half, max_temp_loc[1] - square_size_half),
                        (max_temp_loc[0] + square_size_half, max_temp_loc[1] + square_size_half), (0, 0, 255), 2)

    # Display frame
    cv2.imshow('Frame', frame)

    # Check for end of video or user interrupt
    if not ret or cv2.waitKey(1) == ord('q'):
        break