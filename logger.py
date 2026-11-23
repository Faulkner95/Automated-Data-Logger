import serial
import csv
import os
from datetime import datetime

# Configuration
COM_PORT = "/dev/ttyUSB1"
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

try:
    while True:

        # Read incoming serial data
        raw_data = ser.readline().decode(
            "utf-8",
            errors="ignore"
        ).strip()

        if not raw_data:
            continue

        # Validate temperature reading
        try:
            temperature = float(raw_data)

        except ValueError:
            print(f"Ignored: {raw_data}")
            continue

        # Display received temperature
        print(f"Received: {temperature:.2f} F")

# ==========================================
# ERROR HANDLING
# ==========================================

except KeyboardInterrupt:
    print("\nData collection stopped.")

finally:
    ser.close()
    print("Serial connection closed.")