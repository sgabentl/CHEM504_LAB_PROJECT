from colour_detect_red import ColourDetection as REDColour
from colour_detection import ColourDetection as BLUEColour
from test_position import PositionMove
# from stirrer import IKADriver
from graph import Graph

arm = PositionMove()
arm.robot_conn()
arm.load_sample_1()

# Next week ask what the always allow chmod 666 code is
# stirrer = IKADriver(serial_port="")
# stirrer.setStir(1000)
# stirrer.startStir()

# colour_detection_red = REDColour()
# colour_detection_red.capture()
# colour_detection_red.plot_graph()

# colour_detection = BLUEColour()
# colour_detection.capture()
# colour_detection.plot_graph()

graph = Graph()
graph.get_rgb()

# stirrer.stopStir()
arm.unload_sample_1()
arm.load_sample_2()

graph.get_rgb()

arm.unload_sample_2()
