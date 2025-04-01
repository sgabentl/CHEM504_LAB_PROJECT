from colour_detect_red import ColourDetection as REDColour
from colour_detection import ColourDetection as BLUEColour
from test_position import PositionMove
# from stirrer import IKADriver
from graph import Graph

def run_program():
    """Loads 2 samples to stirrer plate and """
    arm = PositionMove()
    arm.robot_conn()
    arm.load_sample_1()

    # Next week ask what the always allow chmod 666 code is
    # Unlock with sumo python3 file_path
    # stirrer = IKADriver(serial_port="/dev/ttyACM0")
    # stirrer.setStir(1000)
    # stirrer.startStir()

    # colour_detection_red = REDColour()
    # colour_detection_red.capture()
    # colour_detection_red.plot_graph()

    # colour_detection = BLUEColour()
    # colour_detection.capture()
    # colour_detection.plot_graph()

    # Add a sleep for the graph destroy window
    graph1 = Graph()
    graph1.get_rgb()

    # stirrer.stopStir()
    arm.unload_sample_1()
    arm.load_sample_2()
    # stirrer.setStir(1000)
    # stirrer.startStir()

    graph2 = Graph()
    graph2.get_rgb()
    # stirrer.stopStir()

    arm.unload_sample_2()


run_program()
