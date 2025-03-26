import matplotlib.pyplot as plt
import numpy as np

# Create an array of intensities from 0 to 255
intensity = np.arange(0, 256)

# Define RGB intensities (example values, these can be changed)
red = intensity  # Red intensity varies from 0 to 255
green = 255 - intensity  # Green intensity decreases as red increases (for demonstration)
blue = np.abs(128 - intensity)  # Blue intensity forms a symmetric pattern around 128

# Create a plot
plt.figure(figsize=(10, 6))

# Plot the intensity of each color
plt.plot(intensity, red, color='red', label='Red')
plt.plot(intensity, green, color='green', label='Green')
plt.plot(intensity, blue, color='blue', label='Blue')

# Add labels and title
plt.title('RGB Intensity vs. Color Component')
plt.xlabel('Intensity (0 to 255)')
plt.ylabel('Component Value')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
