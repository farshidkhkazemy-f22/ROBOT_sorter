from config import (VISION_REGISTER_ADDRESS, METAL_BASE, METAL_LID)

VISION_1_ADDRESS = VISION_REGISTER_ADDRESS
VISION_2_ADDRESS = VISION_REGISTER_ADDRESS + 1

def read_vision(client):
    result = client.read_input_registers(address=VISION_1_ADDRESS, count=2)
    vision_1 = result.registers[0]
    vision_2 = result.registers[1]
    print(f"VISION 1 = {vision_1}, VISION 2 = {vision_2}")
    return vision_1, vision_2

def classify_material(client):
    vision_1, vision_2 = read_vision(client)

    if vision_1 == METAL_BASE or vision_2 == METAL_BASE:
        print("VISION RESULT->METAL BASE")
        return METAL_BASE
    elif vision_1 == METAL_LID or vision_2 == METAL_LID:
        print("VISION RESULT->METAL LID")
        return METAL_LID
    print(f"UNKNOWN VISION RESULT:{vision_1}, {vision_2}")
    return None
