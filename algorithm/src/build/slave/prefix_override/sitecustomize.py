import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/thaoton1910/swarm_robot/algorithm/src/install/slave'
