import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import pandas as pd

class Graph:
    ROI_SIZE = 50  # 100x100 pixels

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.time_list = []
        self.rgb_dict = {"red": [], "green": [], "blue": [], "time": []}
        
    def save_to_csv(self):
        file_path = f"rgb_csv/rgb_{self.timestamp}.csv"

        df = pd.DataFrame(self.rgb_dict)
        df.to_csv(file_path, index=False)

        print(f"Data saved to {file_path}")
        
    def create_graph(self):
        """Creates an rgb graph"""
        self.time = self.rgb_dict["time"]
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        plt.plot(self.time, self.rgb_dict["red"], color="red", label="Red")
        plt.plot(self.time, self.rgb_dict["green"], color="green", label="Green")
        plt.plot(self.time, self.rgb_dict["blue"], color="blue", label="Blue")
        plt.xlabel("Time (s)")
        plt.ylabel("Intensity (a.u.)")
        plt.title("Intensity vs Time")
        plt.legend()
        plt.grid(True)
        plt.show(block=False)
        plt.savefig(f"graphs/graph_{self.timestamp}")
        plt.close()
        self.save_to_csv()

    def get_rgb(self):
        """Uses camera to get rgb values"""
        start_time = time.time()
            # Loop to capture frames from the video stream
        while True:
            # Read a frame from the camera
            ret, frame = self.cap.read()

            # Exit if the frame was not captured properly
            if not ret:
                print("Failed to capture frame")
                break
            
            h, w, _ = frame.shape
            x_center, y_center = w // 2, h // 2
            x1, y1 = x_center - self.ROI_SIZE // 2, y_center - self.ROI_SIZE // 2
            x2, y2 = x_center + self.ROI_SIZE // 2, y_center + self.ROI_SIZE // 2

            self.roi = frame[y1:y2, x1:x2]

            # Convert the frame from BGR to RGB (OpenCV uses BGR by default)
            roi_rgb = cv2.cvtColor(self.roi, cv2.COLOR_BGR2RGB)
            
            self.pixel_red = 0
            self.pixel_green = 0
            self.pixel_blue = 0
            count = 0
            for row in roi_rgb:
                for pixel in row:
                    self.pixel_red += float(pixel[0])
                    self.pixel_green += float(pixel[1])
                    self.pixel_blue += float(pixel[2])
                    count += 1
                    
            red = self.pixel_red / count
            green = self.pixel_green / count
            blue = self.pixel_blue / count
                    
            self.rgb_dict["red"].append(red)
            self.rgb_dict["green"].append(green)
            self.rgb_dict["blue"].append(blue)
            elapsed_time = time.time() - start_time
            self.rgb_dict["time"].append(elapsed_time)
            
            cv2.imshow("Color Detection", frame)
            cv2.imshow("ROI", self.roi)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif elapsed_time > 30:
                break

        self.cap.release()
        cv2.destroyAllWindows()
        
        self.create_graph()
