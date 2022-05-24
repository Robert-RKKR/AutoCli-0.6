# Generated by Django 3.2.13 on 2022-05-24 18:57

import autocli.basemodel.validators
from django.db import migrations, models
import django.db.models.deletion
import inventory.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Model with root option cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Model name.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Model description.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(choices=[(0, 'static/ico/model/colors/color0.svg'), (1, 'static/ico/model/colors/color1.svg'), (2, 'static/ico/model/colors/color2.svg'), (3, 'static/ico/model/colors/color3.svg'), (4, 'static/ico/model/colors/color4.svg'), (5, 'static/ico/model/colors/color5.svg'), (6, 'static/ico/model/colors/color6.svg'), (7, 'static/ico/model/colors/color7.svg'), (8, 'static/ico/model/colors/color8.svg'), (9, 'static/ico/model/colors/color9.svg'), (10, 'static/ico/model/colors/color10.svg'), (11, 'static/ico/model/colors/color11.svg'), (12, 'static/ico/model/colors/color12.svg'), (13, 'static/ico/model/colors/color13.svg')], default=0, help_text='Color graphical representation.', verbose_name='Color icon')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Model with root option cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Model name.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Model description.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('username', models.CharField(error_messages={'blank': 'Username field is mandatory.', 'invalid': 'Enter the correct username value.', 'null': 'Username field is mandatory.'}, help_text='Local / remote user name.', max_length=64, verbose_name='Username')),
                ('password', models.CharField(blank=True, help_text='Local / remote user password.', max_length=64, null=True, verbose_name='Password')),
                ('ico', models.IntegerField(choices=[(0, 'static/ico/model/users/manager-1.svg'), (1, 'static/ico/model/users/afro-hair-dark.svg'), (2, 'static/ico/model/users/afro-hair.svg'), (3, 'static/ico/model/users/bald.svg'), (4, 'static/ico/model/users/beard.svg'), (5, 'static/ico/model/users/business-man.svg'), (6, 'static/ico/model/users/business-woman.svg'), (7, 'static/ico/model/users/businessman-2.svg'), (8, 'static/ico/model/users/businessman.svg'), (9, 'static/ico/model/users/goth.svg'), (10, 'static/ico/model/users/grandmother.svg'), (11, 'static/ico/model/users/grandpa.svg'), (12, 'static/ico/model/users/hair-bun.svg'), (13, 'static/ico/model/users/japanese.svg'), (14, 'static/ico/model/users/long-haired.svg'), (15, 'static/ico/model/users/man-1.svg'), (16, 'static/ico/model/users/man-2.svg'), (17, 'static/ico/model/users/man.svg'), (18, 'static/ico/model/users/manager-2.svg'), (19, 'static/ico/model/users/nerd.svg'), (20, 'static/ico/model/users/nurse-2.svg'), (21, 'static/ico/model/users/nurse.svg'), (22, 'static/ico/model/users/punk-2.svg'), (23, 'static/ico/model/users/punk.svg'), (24, 'static/ico/model/users/short-hair.svg'), (25, 'static/ico/model/users/skater-2.svg'), (26, 'static/ico/model/users/skater.svg'), (27, 'static/ico/model/users/turtleneck-2.svg'), (28, 'static/ico/model/users/turtleneck.svg'), (29, 'static/ico/model/users/woman-2.svg'), (30, 'static/ico/model/users/woman-3.svg'), (31, 'static/ico/model/users/woman-4.svg'), (32, 'static/ico/model/users/woman.svg')], default=0, help_text='Credential graphical representation.', verbose_name='Credential icon')),
                ('color', models.ForeignKey(blank=True, help_text='Corelated color.', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.color', verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Credential',
                'verbose_name_plural': 'Credentials',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Model with root option cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Model name.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Model description.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('hostname', models.CharField(error_messages={'blank': 'IP / DNS name field is mandatory.', 'invalid': 'Enter a valid IP address or DNS resolvable hostname. It must contain 4 to 32 digits, letters and special characters -, _, . or spaces.', 'null': 'IP / DNS name field is mandatory.', 'unique': 'Device with this hostname already exists.'}, help_text='Valid IP address or domain name.', max_length=32, unique=True, validators=[inventory.validators.HostnameValueValidator()], verbose_name='Hostname')),
                ('ico', models.IntegerField(choices=[(0, 'static/ico/model/devices/switch.svg'), (1, 'static/ico/model/devices/border_router.svg'), (2, 'static/ico/model/devices/chassis.svg'), (3, 'static/ico/model/devices/console.svg'), (4, 'static/ico/model/devices/firewall.svg'), (5, 'static/ico/model/devices/router.svg'), (6, 'static/ico/model/devices/router_firewall.svg'), (7, 'static/ico/model/devices/router_wifi_1.svg'), (8, 'static/ico/model/devices/router_wifi_2.svg'), (9, 'static/ico/model/devices/stack.svg'), (10, 'static/ico/model/devices/stack_firewall_1.svg'), (11, 'static/ico/model/devices/stack_firewall_2.svg'), (12, 'static/ico/model/devices/switch.svg'), (13, 'static/ico/model/devices/wifi-connection.svg'), (14, 'static/ico/model/devices/wireless-router.svg')], default=0, help_text='Network device graphic representation.', verbose_name='Device icon')),
                ('ssh_port', models.IntegerField(default=22, help_text='SSH protocol port number.', verbose_name='SSH port')),
                ('https_port', models.IntegerField(default=443, help_text='HTTPS protocol port number.', verbose_name='HTTPS port')),
                ('ssh_status', models.BooleanField(default=False, help_text='Status of SSH connection to the device.', verbose_name='SSH status')),
                ('https_status', models.BooleanField(default=False, help_text='Status of HTTPS connection to the device.', verbose_name='HTTPS status')),
                ('secret', models.CharField(blank=True, help_text='Network device secret password.', max_length=64, null=True, verbose_name='Secret')),
                ('token', models.CharField(blank=True, help_text='Network device API key.', max_length=128, null=True, verbose_name='API token')),
                ('certificate', models.BooleanField(default=False, help_text='Check network device certificate during HTTPS connection.', verbose_name='Certificate')),
                ('color', models.ForeignKey(blank=True, help_text='Corelated color.', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.color', verbose_name='Color')),
                ('credential', models.ForeignKey(blank=True, help_text='Credential needed to establish SSH / HTTPS connection.', null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.credential', verbose_name='Credential')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Model with root option cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Model name.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Model description.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('netmiko_name', models.CharField(blank=True, help_text='Netmiko name.', max_length=32, null=True, verbose_name='Netmiko name')),
                ('napalm_name', models.CharField(blank=True, help_text='Napalm name.', max_length=32, null=True, verbose_name='Napalm name')),
                ('ico', models.IntegerField(choices=[(0, 'static/ico/model/devices/switch.svg'), (1, 'static/ico/model/devices/border_router.svg'), (2, 'static/ico/model/devices/chassis.svg'), (3, 'static/ico/model/devices/console.svg'), (4, 'static/ico/model/devices/firewall.svg'), (5, 'static/ico/model/devices/router.svg'), (6, 'static/ico/model/devices/router_firewall.svg'), (7, 'static/ico/model/devices/router_wifi_1.svg'), (8, 'static/ico/model/devices/router_wifi_2.svg'), (9, 'static/ico/model/devices/stack.svg'), (10, 'static/ico/model/devices/stack_firewall_1.svg'), (11, 'static/ico/model/devices/stack_firewall_2.svg'), (12, 'static/ico/model/devices/switch.svg'), (13, 'static/ico/model/devices/wifi-connection.svg'), (14, 'static/ico/model/devices/wireless-router.svg')], default=0, help_text='Device type graphical representation.', verbose_name='Device type icon')),
            ],
            options={
                'verbose_name': 'Device type',
                'verbose_name_plural': 'Device types',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Model with root option cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Model name.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Model description.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(choices=[(0, 'static/ico/model/folders/folder-1.svg'), (1, 'static/ico/model/folders/folder-2.svg'), (2, 'static/ico/model/folders/folder-3.svg'), (3, 'static/ico/model/folders/folder-4.svg'), (4, 'static/ico/model/folders/folder-5.svg'), (5, 'static/ico/model/folders/folder-6.svg'), (6, 'static/ico/model/folders/folder-7.svg'), (7, 'static/ico/model/folders/folder-8.svg'), (8, 'static/ico/model/folders/folder-9.svg'), (9, 'static/ico/model/folders/folder-10.svg'), (10, 'static/ico/model/folders/folder-11.svg'), (11, 'static/ico/model/folders/folder-12.svg'), (12, 'static/ico/model/folders/folder-13.svg'), (13, 'static/ico/model/folders/folder-14.svg'), (14, 'static/ico/model/folders/folder-15.svg'), (15, 'static/ico/model/folders/folder-16.svg'), (16, 'static/ico/model/folders/folder-17.svg'), (17, 'static/ico/model/folders/folder-18.svg'), (18, 'static/ico/model/folders/folder-18.svg')], default=0, help_text='Folder graphic representation.', verbose_name='Folder icon')),
                ('color', models.ForeignKey(blank=True, help_text='Corelated color.', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.color', verbose_name='Color')),
                ('credential', models.ForeignKey(blank=True, help_text='Folder default credential needed to establish SSH / HTTPS connection.', null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.credential', verbose_name='Default credential')),
                ('devices', models.ManyToManyField(blank=True, help_text='All devices that belongs to current folder.', to='inventory.Device', verbose_name='Devices')),
                ('root_folder', models.ForeignKey(blank=True, help_text='The parent folder to witch the current folder belongs.', null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.folder', verbose_name='Root folder')),
            ],
            options={
                'verbose_name': 'Folder',
                'verbose_name_plural': 'Folders',
            },
        ),
        migrations.CreateModel(
            name='DeviceCollectedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('result_status', models.BooleanField(default=False, help_text='A positive result means that the command output was successfully received and processed.', verbose_name='Result status')),
                ('raw_data_status', models.BooleanField(default=False, help_text='A positive result means that the raw data collection process has been successfully completed.', verbose_name='Raw data status')),
                ('processed_data_status', models.BooleanField(default=False, help_text='A positive result means that the process of processing the data was completed successfully.', verbose_name='Processed data status')),
                ('command_name', models.CharField(help_text='CLI command name.', max_length=64, verbose_name='Command name')),
                ('command_raw_data', models.TextField(blank=True, help_text='CLI command raw data output.', null=True, verbose_name='Command raw data')),
                ('command_processed_data', models.JSONField(blank=True, help_text='CLI command FSM proccess data.', null=True, verbose_name='Command processed data')),
                ('device_update', models.ForeignKey(help_text='Corelated update model.', on_delete=django.db.models.deletion.CASCADE, to='automation.deviceupdate', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'Device collected data',
                'verbose_name_plural': 'Device collected data',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(blank=True, help_text='Type of network device system.', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.devicetype', verbose_name='Device type'),
        ),
    ]
