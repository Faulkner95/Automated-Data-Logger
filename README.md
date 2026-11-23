ESP32 Temperature Data Logger

Project Overview

This project uses an ESP32 to generate simulated temperature readings and transmits them to a PC over USB serial. This is caught by a Python script which receives the readings and converts them to usable floats with timestamps and node telemetry data written to a CSV file.

Requirements:

Python 3.x

ESP32 flashed with MicroPython & PySerial installed within your enviorment (pip install pyserial)

Configuration:"

Update the COM_PORT variable in logger.py to match your ESP32's serial port.

COM_PORT = "/your/path/to/ESP32_COMM"
BAUD_RATE = 115200


To run the logger, connect the ESP32 to your computer and make sure the ESP32 temperature program is running.

IMPORTANT!

Close any other applications using the serial port.

Run the logger:

python logger.py

Press Ctrl+C to stop data collection.

GH repo:

https://github.com/Faulkner95/Automated-Data-Logger