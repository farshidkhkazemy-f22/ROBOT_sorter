import time
START_INPUT = 6
STOP_INPUT = 7
ROBOT_FREEZE_INPUT = 9
STOP_IS_NC = False


class Interrupted(Exception):
    pass
stop_latch = False
def read_start_stop(client):
    result = client.read_discrete_inputs(address=START_INPUT, count=4)
    start_signal = bool(result.bits[0])
    stop_signal = bool(result.bits[1])
    robot_freeze_signal = bool(result.bits[3])

    return start_signal, stop_signal, robot_freeze_signal

