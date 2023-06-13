import cv2
import numpy as np
import os

# 导入Flir Lepton红外相机的API
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
import PySpin

# 初始化相机
system = PySpin.System_GetInstance()
cam_list = system.GetCameras()
cam = cam_list.GetByIndex(0)
cam.Init()

# 设置相机参数
cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_Continuous)
cam.PixelFormat.SetValue(PySpin.PixelFormat_Mono16)
cam.ExposureAuto.SetValue(PySpin.ExposureAuto_Continuous)
cam.GainAuto.SetValue(PySpin.GainAuto_Continuous)

# 获取相机图像
cam.BeginAcquisition()
frame = cam.GetNextImage()
data = frame.GetData()
frame.Release()
cam.EndAcquisition()

# 将图像转换为numpy数组
img = np.frombuffer(data, dtype=np.uint16)
img = img.reshape((frame.GetHeight(), frame.GetWidth()))

# 将图像转换为温度值
img = (img - 27315) / 100.0

# 获取感兴趣区域的温度值
roi = img[100:200, 100:200]
mean_temp = np.mean(roi)

# 显示图像和温度值
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('Mean temperature:', mean_temp)