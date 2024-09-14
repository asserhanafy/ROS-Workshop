import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/asserhanafy/ROS-Workshop/ros1_ws/install/my_py_pkg'
