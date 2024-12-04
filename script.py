from robodk import robolink, robomath
RDK = robolink.Robolink()


from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
# Link to RoboDK
# RDK = Robolink()

frame = RDK.Item('RefSuctionCup')

RDK = robolink.Robolink()
robot = RDK.Item('Dobot MG400', robolink.ITEM_TYPE_ROBOT)
pick = RDK.Item('Pick 1')
'''
pick.Copy()
approach_pick = frame.Paste()
approach_pick.setName('Approach 1')
approach_pick.setPose(approach_pick.Pose()*robomath.transl(tz=80))
'''

num_tiles= 3
pick.Copy()
for i in range(2, num_tiles+1):
    approach_pick = frame.Paste()
    approach_pick.setName('Pick ' + str(i))
    approach_pick.setPose(approach_pick.Pose()*robomath.transl(ty=-30*(i-1)))
    
place = RDK.Item('Place in box')
for j in range(1, num_tiles+1):
    approach_pick = frame.Paste()
    approach_pick.setName('Approach ' + str(j))
    approach_pick.setPose(approach_pick.Pose()*robomath.transl(tz=80))
    approach_pick.setPose(approach_pick.Pose()*robomath.transl(ty=-30*(i-1)))



#movements
for k in range(1, 4):
    robot.MoveJ(RDK.Item('Approach '+ str(k)))
    robot.MoveL(RDK.Item('Pick ' + str(k)))
    robot.setDO('1', 1)
    robot.Pause(200) #milisecond
    robot.MoveL(approach_pick)
    robot.MoveJ(RDK.Item('place'))
    robot.setDO('1', 0) #suction off
    robot.setDO('2', 1) #air pressure on
    robot.Pause(200)
    robot.setDO('2', 0) #air pressure off




'''
# Program example:
item = RDK.Item('base')
if item.Valid():
    print('Item selected: ' + item.Name())
    print('Item posistion: ' + repr(item.Pose()))

print('Items in the station:')
itemlist = RDK.ItemList()
print(itemlist)
'''
