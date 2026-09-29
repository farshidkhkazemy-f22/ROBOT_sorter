# =====================================
#           SYSTEM
# =====================================
FACTORY_IO_IP = '192.168.1.181'
MODBUS_PORT = 502
LOOP_CYCLE_TIME = 0.05

# =====================================
#        START - STOP
# =====================================
START_INPUT_ADDRESS = 6
STOP_INPUT_ADDRESS = 7
HOME_INPUT_ADDRESS = 9

# =====================================
#           VISION
# =====================================
VISION_REGISTER_ADDRESS = 3

METAL_BASE = 8
METAL_LID = 9

# =====================================
#         DROPPING AREA
# =====================================
METAL_BASE_AREA = [
    0,     # X
    550,   # Y
    330    # Z
]
METAL_LID_AREA = [
    1000,  # X
    550,   # Y
    330   # Z
]

# ======================================
#              ROBOT
# ======================================

HOME_POSITION = [
    0,   # X
    0,   # Y
    0    # Z
]

# =====================================
#           GRIPPER
# ====================================
GRIPPER_COIL_ADDRESS = 0
GRAB = True
RELEASE = False
DETECTED_ITEM_INPUT = 8
