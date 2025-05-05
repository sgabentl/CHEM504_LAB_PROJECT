from test_position import PositionMove
from stirrer import IKADriver
from graph import Graph

PORT = "serial_port"
def run_program():
    """Loads 2 samples to stirrer plate and """
    arm = PositionMove()
    arm.robot_conn()
    arm.load_sample_1()

    graph1 = Graph()
    graph1.get_rgb()

    arm.unload_sample_1()
    arm.load_sample_2()

    graph2 = Graph()
    graph2.get_rgb()

    arm.unload_sample_2()

def run_program_with_auto_stirrer():
    """Loads 2 samples to stirrer plate and """
    arm = PositionMove()
    arm.robot_conn()
    arm.load_sample_1()

    stirrer = IKADriver(serial_port=PORT)
    stirrer.setStir(1000)
    stirrer.startStir()

    # Add a sleep for the graph destroy window
    graph1 = Graph()
    graph1.get_rgb()

    stirrer.stopStir()
    arm.unload_sample_1()
    arm.load_sample_2()
    stirrer.setStir(1000)
    stirrer.startStir()

    graph2 = Graph()
    graph2.get_rgb()
    stirrer.stopStir()

    arm.unload_sample_2()

run_program()

