d = {
    "5A57A1": ["remote_1_button_1", "ON", "false"],
    "5A57A8": ["remote_1_button_2", "ON", "false"],
    "DF3E94": ["office_remote_b1", "ON", "false"],
    "DF3E98": ["office_remote_b2", "ON", "false"],
    "DF3E91": ["office_remote_b3", "ON", "false"],
    "DF3E92": ["office_remote_b4", "ON", "false"],
    "727D06": ["living_room_remote_on", "ON", "false"],
    "91F40E": ["office_door", "OFF", "false"],
    "91F40A": ["office_door", "ON", "false"],
    "97720E": ["office_window", "OFF", "false"],
    "97720A": ["office_window", "ON", "false"],
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
