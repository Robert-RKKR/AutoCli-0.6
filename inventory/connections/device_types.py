# Collect template from Yaml file:
from inventory.yaml_reader import yaml_read
TEMPLATES_PATH = 'inventory/connections/templates'
DEVICE_TYPES_TEMPLATE = yaml_read(f'{TEMPLATES_PATH}/device_types.yml')['output']
