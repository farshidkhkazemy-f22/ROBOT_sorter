import time
from pymodbus.client import ModbusTcpClient

# --- Portfolio Architecture Imports ---
from binary_processor import convert_binary_to_decimal
from robot_positions import initialize_coordinate_tree, search_bst
from start_stop import read_start_stop, Interrupted
from vision import classify_material
from drop_selector import get_drop_position
from robot_controller import go_home, release
from sorting import execute_sorting


# --- Configuration Constants ---
FACTORY_IO_IP = input("Please Enter your IP Address: ").strip()
if not FACTORY_IO_IP:
    FACTORY_IO_IP = "127.0.0.1"
MODBUS_PORT = 502
LOOP_CYCLE_TIME = 0.05  # Fixed execution cadence as requested
SENSOR_START_ADDRESS = 0
SENSOR_COUNT = 6
START_INPUT_ADDRESS = 6
STOP_INPUT_ADDRESS = 7
VISION_1_REGISTER = 3
VISION_2_REGISTER = 4
METAL_BASE_CODE = 8
METAL_LID_CODE = 9
ROBOT_POSITION_REGISTER = 0
GRIPPER_COIL_ADDRESS = 0
GRAB = True
RELEASE = False
HOME_POSITION = [0, 0, 0]
METAL_BASE_AREA = [0, 550, 350]
METAL_LID_AREA = [1000, 550, 350]

# Initialize client and compile the BST position map
client = ModbusTcpClient(FACTORY_IO_IP, port=MODBUS_PORT)
position_tree_root = initialize_coordinate_tree()
if not client.connect():
    print("ERROR: Could not connect to Factory I/O")
    raise SystemExit(1)
print("Connected to Factory I/O")
# SYSTEM STATE
system_active = False
cycle_running = False
robot_freeze_mode = False
prev_start = False

# MAIN LOOP
while True:
    try:
        # START-STOP
        start_signal, stop_signal, robot_freeze_signal = read_start_stop(client)
        # NOTE: STOP is only checked at the start of each loop iteration,
        # so it takes effect after the current pick-and-place cycle finishes,
        # not immediately mid-motion.
        if not stop_signal:
            if system_active:
                print("===SYSTEM STOP===")
                system_active = False
                release(client)
                go_home(client)
            prev_start = stop_signal
            time.sleep(LOOP_CYCLE_TIME)
            continue

        if not robot_freeze_signal:
            if robot_freeze_mode:
                print("===HOME MODE===")
                robot_freeze_mode = True
                go_home(client)
            prev_start = robot_freeze_signal
            time.sleep(LOOP_CYCLE_TIME)
            continue
        robot_freeze_mode = False

        # IMPORTANT NOTE: Press the START button first to activate the robot.
        # The system stays idle and the robot will not move until START is pressed.
        if start_signal and not prev_start and not system_active:
            print("===SYSTEM START===")
            system_active = True
            go_home(client)
        prev_start = start_signal

        if not system_active:
            time.sleep(LOOP_CYCLE_TIME)
            continue

        # READING 6 SENSORS AS BINARY VALUE
        result = client.read_discrete_inputs(address=0, count=6)
        bit_list = [1 if state else 0 for state in result.bits[:6]]
        result2 = client.read_discrete_inputs(address=0, count=6)
        if bit_list != [1 if state else 0 for state in result2.bits[:6]]:
            continue

        # MATERIAL ID
        material_id = convert_binary_to_decimal(bit_list)

        if material_id is None:
            time.sleep(LOOP_CYCLE_TIME)
            continue

        # BST SEARCH
        matched_node = search_bst(position_tree_root, material_id)
        if matched_node is None:
            time.sleep(LOOP_CYCLE_TIME)
            continue
        print(f"SENSOR={bit_list}, MATERIAL ID={material_id}")

        # PICK POSITION
        target_xyz = matched_node.coordinates
        print(f"PICK POSITION={target_xyz}")

        # VISION
        vision_code = classify_material(client)
        if vision_code is None:
            print("vision is not identified")
            time.sleep(LOOP_CYCLE_TIME)
            continue

        # DROP BOX
        drop_position = get_drop_position(vision_code)
        if drop_position is None:
            continue

        # SORT
        cycle_running = True
        execute_sorting(client, pick_position=target_xyz, drop_position=drop_position)

        cycle_running = False

        # time.sleep(LOOP_CYCLE_TIME)
    except Interrupted:
        print("===INTERRUPTED===")
        cycle_running = False
        release(client)
        go_home(client)

    except Exception as e:
        print(f"MAIN LOOP ERROR:{e}")
        cycle_running = False
        go_home(client)
        time.sleep(1)
    except KeyboardInterrupt:

        print("Program stopped by user")
        break
go_home(client)
client.close()
print("Factory I/O connection closed")
