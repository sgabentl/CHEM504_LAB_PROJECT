import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import pandas as pd

class Graph:
    ROI_SIZE = 50  # 100x100 pixels
    image0 = False
    image30 = False
    image60 = False

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
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
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

            # Create window with colour status and ROI
            colour_status = "Blue (Oxidized)" if self.rgb_dict["red"] < 50 else "Transitioning"
            colour_status = "Red" if self.rgb["blue"] < 50 else "Transitioning"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Status: {colour_status}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow("Color Detection", frame)
            cv2.imshow("ROI", self.roi)
            
            if elapsed_time > 0 and self.image0 == False:
                image_filename = f"images/image_0_{self.timestamp}.jpg"
                cv2.imwrite(image_filename, frame)
                self.image0 = True
            if elapsed_time >= 30 and self.image30 == False:
                image_filename = f"images/image_30_{self.timestamp}.jpg"
                cv2.imwrite(image_filename, frame)
                self.image30 = True
            if elapsed_time >= 59 and self.image60 == False:
                image_filename = f"images/image_60_{self.timestamp}.jpg"
                cv2.imwrite(image_filename, frame)
                self.image60 = True
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif elapsed_time > 60:
                break

        self.cap.release()
        cv2.destroyAllWindows()
        
        self.create_graph()
    
