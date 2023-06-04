import time
import subprocess
import os
import threading
import argparse
import logging

parser = argparse.ArgumentParser(description='Script Runner')
parser.add_argument('-s', '--script', default=r"C:\trayCamera\cam.py", required=True,
                    help='Path to the script to be executed')
parser.add_argument('-i', '--interval', type=int, default=30, help='Time interval between script executions in seconds')
parser.add_argument('-l', '--log', default='args.log', help='Path to the log file')
args = parser.parse_args()

shooter_script = args.script
activation_interval = args.interval

if not os.path.isfile(shooter_script):
    print(f"Error: Invalid script path: {shooter_script}")
    exit(1)

logging.basicConfig(filename='args.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def run_script():
    try:
        subprocess.Popen(['pythonw', shooter_script])
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Script executed successfully at {current_time}")
    except Exception as e:
        logging.error(f"Error executing script: {e}")


def execute_script_with_interval():
    while True:
        run_script()
        time.sleep(activation_interval)


timer_thread = threading.Timer(0, execute_script_with_interval)
timer_thread.start()
