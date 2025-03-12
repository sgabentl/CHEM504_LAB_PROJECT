import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd

class ColourDetection:
    # Define color ranges in HSV color space
    # LOWER_BLUE = np.array([90, 50, 50])
    # UPPER_BLUE = np.array([130, 255, 255])
    LOWER_BLUE = np.array([100, 150, 50])
    UPPER_BLUE = np.array([140, 255, 255])
    
    # LOWER_COLORLESS = np.array([0, 0, 200])  
    # UPPER_COLORLESS = np.array([180, 50, 255])
    LOWER_COLOURLESS_GB = np.array([35, 50, 50])
    UPPER_COLOURLESS_GB = np.array([85, 255, 255])
    
    # Set the size of the detection region (ROI)
    ROI_SIZE = 100  # 100x100 pixels
    
    def __init__(self):
        self.v_values = []
        self.time_list = []
        self.cap = cv2.VideoCapture(0)
        self.time_list = []
        self.blue_ratio_list = []
        self.colourless_ratio_list = []
    
    def get_hsv(self):
        self.hsv = cv2.cvtColor(self.roi, cv2.COLOR_BGR2HSV)
        
        my_list = []
        for lists in self.hsv:
            for tuple in lists:
                my_list.append(int(tuple[-1]))
        
        av_value = sum(my_list) / (len(my_list))
        return av_value
        
        
    
    def capture(self):

        start_time = time.time()
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to capture frame")
                break
        
            # Get image dimensions
            h, w, _ = frame.shape
            # Calculate center coordinates of the image
            x_center, y_center = w // 2, h // 2
            x1, y1 = x_center - self.ROI_SIZE // 2, y_center - self.ROI_SIZE // 2
            x2, y2 = x_center + self.ROI_SIZE // 2, y_center + self.ROI_SIZE // 2
        
            # Extract the center region (ROI)
            self.roi = frame[y1:y2, x1:x2]
        
            # Convert ROI to HSV color space
            value = self.get_hsv()
            self.v_values.append(value)
            
        
            # Perform color detection (Blue & Colorless)
            blue_mask = cv2.inRange(self.hsv, self.LOWER_BLUE, self.UPPER_BLUE)
            colourless_mask = cv2.inRange(self.hsv, self.LOWER_COLOURLESS_GB, self.UPPER_COLOURLESS_GB)
        
            # Compute the proportion of detected colors in the ROI
            blue_ratio = np.sum(blue_mask > 0) / blue_mask.size
            colorless_ratio = np.sum(colourless_mask > 0) / colourless_mask.size

            # Record elapsed time and color ratios
            elapsed_time = time.time() - start_time
            self.time_list.append(elapsed_time)
            self.blue_ratio_list.append(blue_ratio)
            self.colourless_ratio_list.append(colorless_ratio)
            
            self.time_list.append(elapsed_time)
        
            # Determine the color status
            if blue_ratio > 0.05:
                colour_status = "Blue (Oxidized)"
            elif colorless_ratio > 0.05:
                colour_status = "Colorless (Reduced)"
            else:
                colour_status = "Transitioning"
        
            # Draw a green rectangle to indicate the detection area on the original frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Status: {colour_status}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # Display the detection results
            cv2.imshow("Color Detection", frame)
            cv2.imshow("ROI", self.roi)  # Show the analyzed region
        
            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                df = pd.DataFrame(self.v_values)
                df.to_csv("hsv_values.csv", index=False)
                break
            # elif elapsed_time > 30:
            #     break
        
        self.cap.release()
        cv2.destroyAllWindows()
    
    def plot_graph(self):
        # Plot colour change graph
        plt.figure(figsize=(8, 5))
        plt.plot(self.time_list, self.blue_ratio_list, label="Blue Ratio", color="blue")
        plt.plot(self.time_list, self.colourless_ratio_list, label="Colourless Ratio", color="gray")
        plt.xlabel("Time (s)")
        plt.ylabel("Colour Ratio")
        plt.title("Colour Change Over Time")
        plt.legend()
        plt.grid(True)
        plt.savefig("Figure")
        plt.show()


colour_detection = ColourDetection()
colour_detection.capture()
