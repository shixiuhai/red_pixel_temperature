import cv2
import numpy as np

# 读取视频文件
cap = cv2.VideoCapture('istockphoto-1225043479-640_adpp_is.mp4')

# 获取视频帧的宽度和高度
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建一个空的温度数组
temp_array = np.zeros((height, width))

# 循环遍历视频帧
while cap.isOpened():
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break
    
    # 获取温度数据
    temp_data = frame[:, :, 0]
    
    # 将温度数据添加到温度数组中
    temp_array += temp_data
    
    # 显示视频帧
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 计算感兴趣区域的平均温度
roi_temp = np.mean(temp_array[100:200, 100:200])

# 输出结果
print('ROI temperature:', roi_temp)

# 释放资源
cap.release()
cv2.destroyAllWindows()
