**ESP32 Temperature Data Logger**

**Project Overview**

This project uses an ESP32 to generate simulated temperature readings and transmits them to a PC over USB serial. This is caught by a Python script which receives the readings and converts them to usable floats with timestamps and node telemetry data written to a CSV file. To run the logger, connect the ESP32 to your computer and make sure the ESP32 temperature program is running.

**Requirements:**

-Python 3.x

-ESP32 flashed with MicroPython & PySerial installed within your enviorment (pip install pyserial)

**Configuration:**

_Update the COM_PORT variable in logger.py to match your ESP32's serial port._

COM_PORT = "_/your/path/to/ESP32_COMM_"

BAUD_RATE = 115200




**IMPORTANT!**

Close any other applications using the serial port before running the logger.

Press Ctrl+C to stop data collection.

_GH repo:
https://github.com/Faulkner95/Automated-Data-Logger_
