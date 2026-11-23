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

# Initialize CSV file
write_header = (
    not os.path.exists(CSV_FILENAME)
    or os.path.getsize(CSV_FILENAME) == 0
)

if write_header:
    with open(
        CSV_FILENAME,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:

        csv_writer = csv.writer(file)

        csv_writer.writerow([
            "Timestamp",
            "Device_ID",
            "Temperature_F"
        ])

try:
    while True:

        # Read incoming serial data
        raw_data = ser.readline().decode(
            "utf-8",
            errors="ignore"
        ).strip()

        if not raw_data:
            continue

        # Validate and convert the received data to float
        try:
            temperature = float(raw_data)

        except ValueError:
            print(f"Ignored: {raw_data}")
            continue

        # Display received temperature
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{current_time}] Received: {temperature:.2f} F")


# ERROR HANDLING


except KeyboardInterrupt:
    print("\nData collection stopped.")

finally:
    ser.close()
    print("Serial connection closed.")