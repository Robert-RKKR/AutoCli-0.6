# Collect template from Yaml file:
from inventory.yaml_reader import yaml_read
TEMPLATES_PATH = 'inventory/connections/templates'
DEVICE_TYPES_TEMPLATE = yaml_read(f'{TEMPLATES_PATH}/device_types.yml')['output']

# Device type model variables:
DEVICE_TYPE = (
    (0, ('Autodetect')),
    (1, (DEVICE_TYPES_TEMPLATE[1]['representation'])),
    (2, (DEVICE_TYPES_TEMPLATE[2]['representation'])),
    (3, (DEVICE_TYPES_TEMPLATE[3]['representation'])),
    (4, (DEVICE_TYPES_TEMPLATE[4]['representation'])),
    (5, (DEVICE_TYPES_TEMPLATE[5]['representation'])),
    (6, (DEVICE_TYPES_TEMPLATE[6]['representation'])),
    (7, (DEVICE_TYPES_TEMPLATE[7]['representation'])),
    (99, ('Unsupported')),
)

def collect_device_type_commands_from_id(device_type_id: int):

    return DEVICE_TYPES_TEMPLATE.get(device_type_id, {}).get('textfsm', False)

# Device name translation functions:
def collect_device_type_name_from_id(device_type_id: int, netmiko: bool = False, napalm: bool = False):
    
    # Check version of device type name:
    if netmiko:
        return DEVICE_TYPES_TEMPLATE.get(device_type_id, {}).get('netmiko', False)
    elif napalm:
        return DEVICE_TYPES_TEMPLATE.get(device_type_id, {}).get('napalm', False)
    else:
        pass

def collect_device_type_id_from_name(device_type_name: str, netmiko: bool = False, napalm: bool = False):

    def search_loop(version):
        for id in DEVICE_TYPES_TEMPLATE:
            current_device_type = DEVICE_TYPES_TEMPLATE[id]
            current_device_type_name = current_device_type.get(version, False)
            if current_device_type_name == device_type_name:
                return id
    
    # Check version of device type name:
    if netmiko:
        return search_loop('netmiko')
    elif napalm:
        return search_loop('napalm')
    else:
        pass
