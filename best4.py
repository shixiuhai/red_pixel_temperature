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
fps = cap.get(cv2.CAP_PROP_FPS)
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 初始化变量以查找最大温度及其位置
max_temp = 0
max_temp_loc = (0, 0)
square_size = 30
# 循环遍历所有帧并提取温度数据
for i in range(num_frames):
    # 读取下一帧
    ret, frame = cap.read()
    # 从帧中提取温度数据
    temp_array = frame[:, :, 0]
    # 查找最大温度及其位置
    if np.max(temp_array) > max_temp:
        max_temp = np.max(temp_array)
        max_temp_loc = np.where(temp_array == max_temp)
        # 检查视频是否结束或用户是否中断
        if not ret or cv2.waitKey(1) == ord('q'):
            break
    avg_temp = np.mean(temp_array[max_temp_loc[0][0]-square_size//2:max_temp_loc[0][0]+square_size//2+1, max_temp_loc[1][0]-square_size//2:max_temp_loc[1][0]+square_size//2+1])
    frame = cv2.rectangle(frame, (max_temp_loc[1][0]-square_size//2, max_temp_loc[0][0]-square_size//2), (max_temp_loc[1][0]+square_size//2+1, max_temp_loc[0][0]+square_size//2+1), (0, 0, 255), 2)
    cv2.putText(frame, 'Max Temp: {:.2f}'.format(max_temp), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, 'Avg Temp: {:.2f}'.format(avg_temp), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Frame', frame)
