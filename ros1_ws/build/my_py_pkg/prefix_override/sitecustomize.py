import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/asserhanafy/linux-tasks/ros1_ws/install/my_py_pkg'
