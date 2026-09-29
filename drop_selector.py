from config import (METAL_BASE, METAL_LID, METAL_BASE_AREA, METAL_LID_AREA)

def get_drop_position(vision_code):
    if vision_code == METAL_BASE:
        print("DROP BOX->LEFT")
        return METAL_BASE_AREA
    elif vision_code == METAL_LID:
        print("DROP BOX->RIGHT")
        return METAL_LID_AREA
    print(f"ERROR: Unknown material code = {vision_code}")
    return None
