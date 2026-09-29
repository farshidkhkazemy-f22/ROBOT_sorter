from robot_controller import (move_robot, grab, release)

def execute_sorting(client, pick_position, drop_position):
    # PICK
    print(f"PICK POSITION={pick_position}")
    move_robot(client, pick_position)
    # GRAB
    grab(client)
    # DROP
    print(f"DROP POSITION={drop_position}")
    move_robot(client, drop_position)
    # RELEASE
    release(client)

