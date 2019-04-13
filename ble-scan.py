#%% 
import pygatt
import sys
import time 
#    this app runs the equivalent of  `gatttool -b <device_id> --char-read <service_uuid>`

## TODO: scan for devices matching pattern (e.g. manufacturer id or device name)
DEVICE_1 = # device MAC address goes here
DEVICE_2 = # device MAC address goes here

# The BGAPI backend will attempt to auto-discover the serial device name of the
# attached BGAPI-compatible USB adapter.
# adapter = pygatt.BGAPIBackend()


def scan_device(device_id, read_services):
    try:
        adapter = pygatt.GATTToolBackend()
        adapter.start()
        device = adapter.connect(address=device_id, 
                                 timeout=10, 
                                 auto_reconnect=True)  
        return read_services(device)
    except:
        err = sys.exc_info()
        print(err)
    finally:
        adapter.stop()

def scan_jinou_temperature_sensor(device_id):
    def read_jinou_services(device):
        # these services use formatting specific to the Jinou JO-0628 temperature/humidity sensor

        # Documented services on Jinou JO-0628 temperature/humidity sensor
        BATTERY_SERVICE = "0x2a19"
        NAME_SERVICE    = "0x2a00"
        ENV_SERVICE     = "0xaa21"
        SAMPLING_ON     = "0xaa22"  #sampling enabled
        SAMPLING_RATE   = "0x0023"  #sample rate in 100ths of a second

        result = {}
        result['name'] = device.char_read(NAME_SERVICE)
        result['name'] = result['name'].decode("ascii")
        print(f"NAME: {result['name']}")
        
        result['battery'] = device.char_read(BATTERY_SERVICE) 
        result['battery'] = int(result['battery'].hex(), 16)
        print(f"BATTERY: {result['battery']}%")

        env = device.char_read(ENV_SERVICE) 
        result['temperature'] = int(env.hex()[2:4 ], 16) + int(env.hex()[ 4:6 ], 16)/10
        result['humidity']    = int(env.hex()[8:10], 16) + int(env.hex()[10:12], 16)/10
        print(f"TEMPERATURE: {result['temperature']}°C, HUMIDITY: {result['humidity']}%" )
        return result

    return scan_device(device_id, read_jinou_services)


results = []
# TODO: implement some logging system to track the data (maybe push to logstash and set up a kibana dashoard?)
#       probably push to logging service between each device

results.append(scan_jinou_temperature_sensor(DEVICE_1))
results.append(scan_jinou_temperature_sensor(DEVICE_2))

import json
json_data = json.dumps(results)
print(json_data)



#%%
