# Django Import:
from django.utils.translation import gettext_lazy as _

# Constance values:
DEVICE_PATH = 'static/ico/model/devices/'
FOLDER_PATH = 'static/ico/model/folders/'
USER_PATH = 'static/ico/model/users/'

DEVICE_ICONS = (
    (0, (f'{DEVICE_PATH}switch.svg')),
    (1, (f'{DEVICE_PATH}border_router.svg')),
    (2, (f'{DEVICE_PATH}chassis.svg')),
    (3, (f'{DEVICE_PATH}console.svg')),
    (4, (f'{DEVICE_PATH}firewall.svg')),
    (5, (f'{DEVICE_PATH}router.svg')),
    (6, (f'{DEVICE_PATH}router_firewall.svg')),
    (7, (f'{DEVICE_PATH}router_wifi_1.svg')),
    (8, (f'{DEVICE_PATH}router_wifi_2.svg')),
    (9, (f'{DEVICE_PATH}stack.svg')),
    (10, (f'{DEVICE_PATH}stack_firewall_1.svg')),
    (11, (f'{DEVICE_PATH}stack_firewall_2.svg')),
    (12, (f'{DEVICE_PATH}switch.svg')),
    (13, (f'{DEVICE_PATH}wifi-connection.svg')),
    (14, (f'{DEVICE_PATH}wireless-router.svg')),
)

USER_ICONS = (
    (0, (f'{USER_PATH}manager-1.svg')),
    (1, (f'{USER_PATH}afro-hair-dark.svg')),
    (2, (f'{USER_PATH}afro-hair.svg')),
    (3, (f'{USER_PATH}bald.svg')),
    (4, (f'{USER_PATH}beard.svg')),
    (5, (f'{USER_PATH}business-man.svg')),
    (6, (f'{USER_PATH}business-woman.svg')),
    (7, (f'{USER_PATH}businessman-2.svg')),
    (8, (f'{USER_PATH}businessman.svg')),
    (9, (f'{USER_PATH}goth.svg')),
    (10, (f'{USER_PATH}grandmother.svg')),
    (11, (f'{USER_PATH}grandpa.svg')),
    (12, (f'{USER_PATH}hair-bun.svg')),
    (13, (f'{USER_PATH}japanese.svg')),
    (14, (f'{USER_PATH}long-haired.svg')),
    (15, (f'{USER_PATH}man-1.svg')),
    (16, (f'{USER_PATH}man-2.svg')),
    (17, (f'{USER_PATH}man.svg')),
    (18, (f'{USER_PATH}manager-2.svg')),
    (19, (f'{USER_PATH}nerd.svg')),
    (20, (f'{USER_PATH}nurse-2.svg')),
    (21, (f'{USER_PATH}nurse.svg')),
    (22, (f'{USER_PATH}punk-2.svg')),
    (23, (f'{USER_PATH}punk.svg')),
    (24, (f'{USER_PATH}short-hair.svg')),
    (25, (f'{USER_PATH}skater-2.svg')),
    (26, (f'{USER_PATH}skater.svg')),
    (27, (f'{USER_PATH}turtleneck-2.svg')),
    (28, (f'{USER_PATH}turtleneck.svg')),
    (29, (f'{USER_PATH}woman-2.svg')),
    (30, (f'{USER_PATH}woman-3.svg')),
    (31, (f'{USER_PATH}woman-4.svg')),
    (32, (f'{USER_PATH}woman.svg')),
)

FOLDER_ICONS = (
    (0, (f'{FOLDER_PATH}folder-1.svg')),
    (1, (f'{FOLDER_PATH}folder-2.svg')),
    (2, (f'{FOLDER_PATH}folder-3.svg')),
    (3, (f'{FOLDER_PATH}folder-4.svg')),
    (4, (f'{FOLDER_PATH}folder-5.svg')),
    (5, (f'{FOLDER_PATH}folder-6.svg')),
    (6, (f'{FOLDER_PATH}folder-7.svg')),
    (7, (f'{FOLDER_PATH}folder-8.svg')),
    (8, (f'{FOLDER_PATH}folder-9.svg')),
    (9, (f'{FOLDER_PATH}folder-10.svg')),
    (10, (f'{FOLDER_PATH}folder-11.svg')),
    (11, (f'{FOLDER_PATH}folder-12.svg')),
    (12, (f'{FOLDER_PATH}folder-13.svg')),
    (13, (f'{FOLDER_PATH}folder-14.svg')),
    (14, (f'{FOLDER_PATH}folder-15.svg')),
    (15, (f'{FOLDER_PATH}folder-16.svg')),
    (16, (f'{FOLDER_PATH}folder-17.svg')),
    (17, (f'{FOLDER_PATH}folder-18.svg')),
    (18, (f'{FOLDER_PATH}folder-18.svg')),
)

DEVICETYPES = (
    (0, _('Undefinded')),
    (1, _('Autodetect')),
    (2, _('Cisco IOS')),
    (3, _('Cisco XR')),
    (4, _('Cisco XE')),
    (5, _('Cisco NXOS')),
    (6, _('Cisco ASA')),
)
