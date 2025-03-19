from colour_detection import ColourDetection
from test_position import PositionMove
# from stirrer import IKADriver
import time

arm = PositionMove()
arm.robot_conn()
arm.move_to_stirrer()

# stirrer = IKADriver(serial_port="/dev/ttyACM0")
# stirrer.setStir(1000)
# stirrer.startStir()

colour_detection = ColourDetection()
colour_detection.capture()
colour_detection.plot_graph()

# stirrer.stopStir()
arm.remove_from_stirrer()
