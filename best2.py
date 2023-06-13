import cv2
import numpy as np

# Load video file
cap = cv2.VideoCapture('istockphoto-1225043479-640_adpp_is.mp4')
convert_rgb = cap.get(cv2.CAP_PROP_CONVERT_RGB)
if convert_rgb == 1:
    channel_count = 3
    print(3)
else:
    channel_count = 1
    print(1)

# Set pixel format to temperature linear
# cap.set(cv2.CAP_PROP_CONVERT_RGB, 0.0)
cap.set(cv2.CAP_PROP_FORMAT, cv2.CV_32F)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop through all frames and extract temperature data
for i in range(num_frames):
    # Read next frame
    ret, frame = cap.read()

    # Extract temperature data from frame
    temp_array = frame[:, :, 0]

    # Find maximum temperature and its location
    max_temp = np.max(temp_array)
    max_temp_loc = np.where(temp_array == max_temp)

    # Print maximum temperature and its location
    print('Frame', i+1, ': Maximum temperature is', max_temp, 'at location', max_temp_loc)

    # Draw circle around maximum temperature location
    frame = cv2.circle(frame, (max_temp_loc[1][0], max_temp_loc[0][0]), 10, (0, 0, 255), 2)

    # Display frame
    cv2.imshow('Frame', frame)

    # Check for end of video or user interrupt
    if not ret or cv2.waitKey(1) == ord('q'):
        break

# Release video file and close window
cap.release()
cv2.destroyAllWindows()
