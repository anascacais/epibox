# built-in
import json

def get_battery(client, devices, service):

    if service != 'Mini':
        battery = {}
        for device in devices:
            state = device.state()
            if state['battery'] > 63:
                battery_volts = 2 * ((state['battery']*3.3) / (2**10-1))
            else:
                battery_volts = 2 * ((state['battery']*3.3) / (2**6-1))

            battery[device.macAddress] = battery_volts

        battery_json = json.dumps(['BATTERY', battery])
        client.publish('rpi', battery_json)