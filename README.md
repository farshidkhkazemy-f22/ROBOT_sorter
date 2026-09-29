# Factory I/O Robotic Sorting System

A Python-based robotic sorting system for Factory I/O, using Modbus TCP for real-time communication with the simulated PLC. Uses a Binary Search Tree (BST) to map binary sensor codes to material types and pick/drop positions, with computer-vision-based material detection and start/stop/home control logic.

## Demo
![Factory I/O Scene](<Factory IO 9_29_2026 6_59_12 PM.png>)

## Features
- Modbus TCP communication with Factory I/O
- Binary sensor code to material type mapping (BST-based)
- Automated pick-and-place robotic arm control
- Start / Stop / Home control logic with signal debouncing
- Configurable Factory I/O IP address at runtime

## Project Structure
- main.py — main control loop
- config.py — configuration constants (addresses, positions, etc.)
- robot_controller.py — robot movement, grab/release logic
- robot_positions.py — BST of pick/drop positions
- binary_processor.py — binary sensor code to decimal conversion
- sorting.py — sorting cycle logic
- vision.py — material detection logic
- drop_selector.py — drop position selection
- start_stop.py — start/stop/home signal handling

## Requirements
'''
pip install -r requirements.txt
'''

## How to Run
1. Open Factory I/O and load the sorting scene.
2. Enable the Modbus TCP/IP Server driver and click Connect.
3. Run the scene (Play).
4. Run main.py and enter the Factory I/O server IP when prompted.

## Modbus Address Map
| Address | Type            | Description          |
|---------|-----------------|----------------------|
| 0–5     | Discrete Input  | Material sensors     |
| 6       | Discrete Input  | Start button         |
| 7       | Discrete Input  | Stop button          |
| 8       | Discrete Input  | Detected Sensor      |
| 9       | Discrete Input  | Home/Freeze switch   |
| 0-2     | Holding Register| Robot X/Y/Z position |
| 0       | Coil            | Gripper control      |
| 3       | Input Register  | Vision Sensor1       |
| 4       | Input Register  | Vision Sensor2       |
