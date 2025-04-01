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
     # Automated stirrer might be a different height      
     STIRRER_1 = [1.7241122722625732, -1.6038876972594203, 2.0562947432147425, -0.45576222360644536, 1.5195368528366089, 3.1572272777557373]
     STIRRER_2 = [1.1704504489898682, -2.112025877038473, 2.47654635110964, -0.3685503763011475, 1.168399691581726, 3.1618423461914062]
     STIRRER_3 = [1.169089436531067, -1.8085299930968226, 2.695914093648092, -0.8905757826617737, 1.1692121028900146, 3.1597652435302734]
     STIRRER_4 = [1.3753674030303955, -2.014369627038473, 2.465492550526754, -0.4437050384334107, 1.511202335357666, 3.1767196655273438]
     STIRRER_5 = [1.3743326663970947, -1.7633243999876917, 2.636611525212423, -0.8658105891994019, 1.5119651556015015, 3.1751298904418945]
     
     LOAD_1 = [1.7239357233047485, -1.5127788682333012, 2.154865090047018, -0.6454361242106934, 1.5201416015625, 3.1564512252807617]
     LOAD_2 = [1.7227802276611328, -1.0755092662623902, 2.2902348677264612, -1.2178798180869599, 1.5208289623260498, 3.153461456298828]
     LOAD_3 = [1.8120537996292114, -1.0047091406634827, 2.096247975026266, -1.1023701292327424, 1.784925103187561, 3.175017833709717]
     LOAD_4 = [1.8128043413162231, -1.3205546897700806, 2.006113354359762, -0.6958256524852295, 1.784356713294983, 3.1772873401641846]
     
     UNLOAD_1 = [1.1704657077789307, -2.1179315052428187, 2.4668949286090296, -0.35293133676562505, 1.168339729309082, 3.1618471145629883]
     UNLOAD_2 = [0.7566418647766113, -1.636881013909811, 2.2505953947650355, -0.6343515676311036, 0.9606629610061646, 3.1384644508361816]
     UNLOAD_3 = [0.7554967999458313, -1.2361930173686524, 2.4058011213885706, -1.1882760983756562, 0.9613173007965088, 3.1351099014282227]
     UNLOAD_4 = [0.7551684379577637, -1.1130998891643067, 2.4130519072162073, -1.3181210321239014, 0.9611937999725342, 3.1341538429260254]
     UNLOAD_5 = [0.8142712116241455, -1.6682263813414515, 2.2509000937091272, -0.5373445314219971, 0.9473036527633667, 3.1304078102111816]
     UNLOAD_6 = [0.813372790813446, -1.3423428249410172, 2.407254759465353, -1.0180101555636902, 0.9482195377349854, 3.1276650428771973]
     UNLOAD_7 = [0.8128491640090942, -1.1640876692584534, 2.428725067769186, -1.2169773441604157, 0.9481956958770752, 3.1262495517730713]
     
     
     def __init__(self):
          self.gripper = Gripper()
          self.gripper.connect()
          
     def robot_conn(self):
          self.robot = URControl(ip="192.168.0.2", port=30003)
          self.positionHandler = PositionHandler(self.robot)

     def load_sample_1(self):
          self.positionHandler.move_to_position(self.LOAD_1)
          self.positionHandler.move_to_position(self.LOAD_2)
          self.gripper.close_grip()
          self.positionHandler.move_to_position(self.LOAD_1)
          # self.positionHandler.move_to_position(self.STIRRER_1)
          self.positionHandler.move_to_position(self.STIRRER_2)
          self.positionHandler.move_to_position(self.STIRRER_3)
          self.gripper.open_grip()
          self.positionHandler.move_to_position(self.STIRRER_2)
          
     def unload_sample_1(self):
          self.positionHandler.move_to_position(self.STIRRER_3)
          self.gripper.close_grip()
          self.positionHandler.move_to_position(self.UNLOAD_1)
          self.positionHandler.move_to_position(self.UNLOAD_2)
          self.positionHandler.move_to_position(self.UNLOAD_3)
          self.positionHandler.move_to_position(self.UNLOAD_4)
          self.gripper.open_grip()
          self.positionHandler.move_to_position(self.UNLOAD_2)

     
     def load_sample_2(self):
          self.positionHandler.move_to_position(self.STIRRER_2)
          self.positionHandler.move_to_position(self.LOAD_1)
          self.positionHandler.move_to_position(self.LOAD_3)
          self.gripper.close_grip()
          self.positionHandler.move_to_position(self.LOAD_4)
          self.positionHandler.move_to_position(self.STIRRER_4)
          self.positionHandler.move_to_position(self.STIRRER_5)
          self.gripper.open_grip()
          self.positionHandler.move_to_position(self.STIRRER_2)
          
     def unload_sample_2(self):
          self.positionHandler.move_to_position(self.STIRRER_3)
          self.gripper.close_grip()
          self.positionHandler.move_to_position(self.UNLOAD_1)
          self.positionHandler.move_to_position(self.UNLOAD_5)
          self.positionHandler.move_to_position(self.UNLOAD_6)
          self.positionHandler.move_to_position(self.UNLOAD_7)
          self.gripper.open_grip_60()
          self.positionHandler.move_to_position(self.UNLOAD_5)
