import requests
import datetime
import bluetooth
HARD_CODED_MAPPING = {
    "Bose SLIII": "wow"
}

def update_location(location,update_time):
    # api-endpoint
    URL = "http://maps.googleapis.com/maps/api/geocode/json" #insert flask endpoint

    # defining a params dict for the parameters to be sent to the API
    DATA = {
        "location": location,
        "updated": update_time
    }
    # sending get request and saving the response as response object
    r = requests.post(url=URL, params=DATA)

def poll_for_devices():
    #if device found update location and send timestamp
    devices = bluetooth.find_service(name='Location Hub', uuid=None, address=None)
    #nearby_devices = bluetooth.discover_devices(lookup_names=True, flush_cache=True, duration=20)
    #print"found %d devices" % len(nearby_devices)
    poll_time = datetime.datetime.now()
    for name in devices.description:
        location = HARD_CODED_MAPPING.get(name)
        if location is not None:
            update_location(location,poll_time)
        print("%s - %s" % (name, poll_time))

    return poll_time

