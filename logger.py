import serial
import csv
import os
from datetime import datetime

# Configuration
COM_PORT = "/dev/ttyUSB0"
BAUD_RATE = 115200
CSV_FILENAME = "sensor_data.csv"
DEVICE_ID = "ESP32_Node_1"

# Serial Connection
print(f"Connecting to ESP32 on {COM_PORT}...")

ser = serial.Serial(
    port=COM_PORT,
    baudrate=BAUD_RATE,
    timeout=1
)

print("Serial connection established!")
