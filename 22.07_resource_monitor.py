import os
import psutil
import time


def monitor(pid):
    return f"PID:{pid}, CPU: {psutil.cpu_percent()}, RAM: {psutil.virtual_memory()[2]}"


while True:
    print(monitor(os.getpid()))
    time.sleep(0.5)


data_store = {
    "PID": ["", ""],
    "PID": ["", ""],
    "PID": ["", ""],
    "PID": ["", ""],
}
