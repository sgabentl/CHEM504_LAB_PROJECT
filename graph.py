import cv2
import numpy as np
import matplotlib.pyplot as plt

# Initialize the video capture (0 for the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened correctly
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Create a figure for plotting (to keep it updated in real-time)
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(10, 6))

# Set up initial empty bars
bars = ax.bar(['Red', 'Green', 'Blue'], [0, 0, 0], color=['red', 'green', 'blue'])

# Set plot labels and title
ax.set_title('Average RGB Intensity from Video Stream')
ax.set_xlabel('Color Channel')
ax.set_ylabel('Average Intensity (0 to 255)')
ax.grid(True)

# Loop to capture frames from the video stream
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Exit if the frame was not captured properly
    if not ret:
        print("Failed to capture frame")
        break

    # Convert the frame from BGR to RGB (OpenCV uses BGR by default)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Extract the RGB components
    red = frame_rgb[:, :, 0]  # Red channel
    green = frame_rgb[:, :, 1]  # Green channel
    blue = frame_rgb[:, :, 2]  # Blue channel

    # Compute the average intensity for each channel
    avg_red = np.mean(red)
    avg_green = np.mean(green)
    avg_blue = np.mean(blue)

    # Update the bar heights with the new intensity values
    bars[0].set_height(avg_red)
    bars[1].set_height(avg_green)
    bars[2].set_height(avg_blue)

    # Draw the updated plot
    plt.draw()
    plt.pause(0.1)  # Pause to update the plot

    # Show the video feed in a window (optional)
    cv2.imshow('Video Feed', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Close the plot when the loop ends
plt.ioff()  # Turn off interactive mode
plt.show()
