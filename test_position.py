from PIL import ImageTk, Image
import numpy as np
import math
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'robotiq'))
from utils.UR_Functions import URfunctions as URControl
from robotiq.robotiq_gripper import RobotiqGripper
from test_gripper import Gripper

class PositionHandler: 
     def __init__(self, robot: URControl, ):
          self.robot = robot
          self.gripper = RobotiqGripper()
          self.init = self.init()
     
     def init(self):
          self.gripper.connect("192.168.0.2", 63352)
     
     def move_to_position(self, position: list[float]):
          self.robot.move_joint_list(position, 0.25, 0.5, 0.02)

     
class PositionMove:         
     RED_POSITION1 = [1.7446362972259521, -1.4385647040656586, 2.3446999231921595, -0.7653154295733948, 1.5420920848846436, 3.153193950653076]
     RED_POSITION2 = [1.730034589767456, -1.0733220440200348, 2.283058468495504, -1.201580212717392, 1.542656660079956, 3.153193950653076]
     GREEN_POSITION1 = [1.7241122722625732, -1.6038876972594203, 2.0562947432147425, -0.45576222360644536, 1.5195368528366089, 3.1572272777557373]
     GREEN_POSITION2 = [1.1704504489898682, -2.112025877038473, 2.47654635110964, -0.3685503763011475, 1.168399691581726, 3.1618423461914062]
     GREEN_POSITION3 = [1.169089436531067, -1.8085299930968226, 2.695914093648092, -0.8905757826617737, 1.1692121028900146, 3.1597652435302734]
     #GREEN_POSITION2 = [1.174616813659668, -2.16580929378652, 2.3327489534961146, -0.15603549898181157, 1.1721503734588623, 3.1608855724334717]
     #GREEN_POSITION3 = [1.1731359958648682, -1.8137570820250453, 2.6901567617999476, -0.8645797532847901, 1.1737935543060303, 3.1583807468414307]
     RED_POSITION3 = [1.7239357233047485, -1.5127788682333012, 2.154865090047018, -0.6454361242106934, 1.5201416015625, 3.1564512252807617]
     RED_POSITION4 = [1.7227802276611328, -1.0755092662623902, 2.2902348677264612, -1.2178798180869599, 1.5208289623260498, 3.153461456298828]
     
     def __init__(self):
          self.gripper = Gripper()
          self.gripper.connect()
          
     def robot_conn(self):
          self.robot = URControl(ip="192.168.0.2", port=30003)
          self.positionHandler = PositionHandler(self.robot)

     def move_to_stirrer(self):
          self.positionHandler.move_to_position(self.RED_POSITION3)
          self.positionHandler.move_to_position(self.RED_POSITION4)
          self.gripper.close_grip()
          self.positionHandler.move_to_position(self.RED_POSITION3)
          self.positionHandler.move_to_position(self.GREEN_POSITION1)
          self.positionHandler.move_to_position(self.GREEN_POSITION2)
          self.positionHandler.move_to_position(self.GREEN_POSITION3)
          self.gripper.open_grip()
          self.positionHandler.move_to_position(self.GREEN_POSITION2)
          
     def remove_from_stirrer(self):
          self.positionHandler.move_to_position(self.GREEN_POSITION3)
          self.gripper.close_grip()
          self.positionHandler.move_to_position(self.GREEN_POSITION2)
          self.positionHandler.move_to_position(self.GREEN_POSITION1)
          self.positionHandler.move_to_position(self.RED_POSITION3)
          self.positionHandler.move_to_position(self.RED_POSITION4)
          self.gripper.open_grip()
          self.positionHandler.move_to_position(self.RED_POSITION1)
