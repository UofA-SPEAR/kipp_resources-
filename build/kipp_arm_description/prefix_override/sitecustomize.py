import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/prjadmin/Desktop/kipp_resources/install/kipp_arm_description'
