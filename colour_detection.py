import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import datetime

class ColourDetection:
    LOWER_BLUE = np.array([100, 150, 50])
    UPPER_BLUE = np.array([140, 255, 255])
    

   
    ROI_SIZE = 100  # 100x100 pixels
   
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.time_list = []
        self.blue_ratio_list = []

    def get_timestamp(self):
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    def compute_weighted_blue_ratio(self, hsv):
        mask = cv2.inRange(hsv, self.LOWER_BLUE, self.UPPER_BLUE)
        
        # get H, S, V values
        H, S, V = cv2.split(hsv)
        
        # the values mainly changed are S and V
        S_blue = S[mask > 0]  
        V_blue = V[mask > 0]  
        
        if len(S_blue) == 0:  
            return 0

        # calculate the weighted blue ratio
        blue_ratio = np.sum(S_blue * V_blue) / (np.sum(S) * np.sum(V))  
        return blue_ratio
        

    def capture(self):
        start_time = time.time()

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to capture frame")
                break

            h, w, _ = frame.shape
            x_center, y_center = w // 2, h // 2
            x1, y1 = x_center - self.ROI_SIZE // 2, y_center - self.ROI_SIZE // 2
            x2, y2 = x_center + self.ROI_SIZE // 2, y_center + self.ROI_SIZE // 2

            roi = frame[y1:y2, x1:x2]
            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            # calculate the weighted blue ratio
            weighted_blue_ratio = self.compute_weighted_blue_ratio(hsv)

            elapsed_time = time.time() - start_time
            self.time_list.append(elapsed_time)
            self.blue_ratio_list.append(weighted_blue_ratio)

            colour_status = "Blue (Oxidized)" if weighted_blue_ratio > 0 else "Transitioning"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Status: {colour_status}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Color Detection", frame)
            cv2.imshow("ROI", roi)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif elapsed_time > 30:
                break

        self.cap.release()
        cv2.destroyAllWindows()
        self.save_to_csv()

    def save_to_csv(self):
        timestamp = self.get_timestamp()
        file_path = f"colour_detection_values/color_detection_{timestamp}.csv"

        data = {
            "Time (s)": self.time_list,
            "Weighted Blue Ratio": self.blue_ratio_list
        }
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)

        print(f"Data saved to {file_path}")

    def plot_graph(self):
        timestamp = self.get_timestamp()
        image_path = f"colour_detection_graph/Figure_{timestamp}.png"

        plt.figure(figsize=(8, 5))
        plt.plot(self.time_list, self.blue_ratio_list, label="Weighted Blue Ratio", color="blue")
        plt.xlabel("Time (s)")
        plt.ylabel("Weighted Blue Ratio")
        plt.title("Colour Change Over Time")
        plt.legend()
        plt.grid(True)
        plt.savefig(image_path)
        plt.show(block=False)
        time.sleep(10)
        plt.close()

        print(f"Graph saved to {image_path}")
