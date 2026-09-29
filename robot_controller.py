import time

from config import (GRIPPER_COIL_ADDRESS, GRAB, RELEASE, HOME_POSITION, DETECTED_ITEM_INPUT)

def move_robot(client, position):
    position = [int(position[0]), int(position[1]), int(position[2])]
    print(f"robot move -> {position}")
    client.write_registers(address=0, values=position)
    time.sleep(1.35)

def grab(client):
    print("GRAB")
    result = client.read_discrete_inputs(address=DETECTED_ITEM_INPUT, count=1)
    if result.bits[0]:
        client.write_coil(address=GRIPPER_COIL_ADDRESS, value=GRAB)
        time.sleep(0.5)
    else:
        client.write_coil(address=GRIPPER_COIL_ADDRESS, value=RELEASE)
        go_home(client)
def release(client):
    print("RELEASE")
    client.write_coil(address=GRIPPER_COIL_ADDRESS, value=RELEASE)

def go_home(client):
    print("RETURN TO HOME")
    move_robot(client, HOME_POSITION)
