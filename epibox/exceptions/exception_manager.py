# built-in
import subprocess
import time
from datetime import datetime

# local
from epibox.common.disconnect_system import disconnect_system
from epibox.common.write_file import write_summary_file


def error_kill(client, devices, msg, mqtt_msg='ERROR', a_file=None, files_open=True, devices_connected=True):

    print(msg)
    client.publish('rpi', str([mqtt_msg]))
    client.loop_stop()

    # Disconnect the system
    disconnect_system(devices, a_file, files_open, devices_connected)
    

    pid = subprocess.run(['sudo', 'pgrep', 'python'], capture_output=True, text=True).stdout.split('\n')[:-1]
    for p in pid:
        subprocess.run(['kill', '-9', p])


def error_disconnect(client, devices, msg, a_file=None, files_open=True):

    print('The system has stopped running because ' + str(msg))
    client.publish('rpi', str(['RECONNECTING']))

    # Disconnect the system
    write_summary_file(a_file.name)
    disconnect_system(devices, a_file, files_open)
    
    devices = []
    system_started = False

    return devices, system_started


def client_kill(client, devices, msg, a_file=None, files_open=True):

    print(msg)
    client.publish('rpi', str(['STOPPED']))
    client.loop_stop()

    # Disconnect the system
    disconnect_system(devices, a_file, files_open)

    time.sleep(3)
    pid = subprocess.run(['sudo', 'pgrep', 'python'], capture_output=True, text=True).stdout.split('\n')[:-1]
    for p in pid:
        subprocess.run(['kill', '-9', p])