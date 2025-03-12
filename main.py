from wed12 import ColourDetection
from test_position import PositionMove

arm = PositionMove()
arm.move_to_stirrer()

colour_detection = ColourDetection()
colour_detection.capture()
colour_detection.plot_graph()
