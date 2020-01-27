d = {
    "5A57A1": ["remote_1_button_1", "ON", "false"],
    "5A57A8": ["remote_1_button_2", "ON", "false"],
    "DF3E94": ["office_remote_b1", "ON", "false"],
    "DF3E98": ["office_remote_b2", "ON", "false"],
    "DF3E91": ["office_remote_b3", "ON", "false"],
    "DF3E92": ["office_remote_b4", "ON", "false"],
    "91F40E": ["office_door", "OFF", "true"],
    "91F40A": ["office_door", "ON", "true"],
    "97720E": ["office_window", "OFF", "true"],
    "97720A": ["office_window", "ON", "true"],
    "940E0E": ["my_closet", "OFF", "true"],
    "940E0A": ["my_closet", "ON", "true"],
    "92E70E": ["crystal_closet", "OFF", "true"],
    "92E70A": ["crystal_closet", "ON", "true"],
    "FF1901": ["living_room_remote", "ON", "false"],
    "950D0E": ["laundry_door", "OFF", "true"],
    "950D0A": ["laundry_door", "ON", "true"],
    "94830E": ["storage_door", "OFF", "true"],
    "94830A": ["storage_door", "ON", "true"],
}

p = data.get("payload")

if p is not None:
    if p in d.keys():
        service_data = {
            "topic": "home/{}".format(d[p][0]),
            "payload": "{}".format(d[p][1]),
            "qos": 0,
            "retain": "{}".format(d[p][2]),
        }
    else:
        service_data = {
            "topic": "home/unknown",
            "payload": "{}".format(p),
            "qos": 0,
            "retain": "false",
        }
        logger.warning("<rfbridge_demux> Received unknown RF command: {}".format(p))
    hass.services.call("mqtt", "publish", service_data, False)
