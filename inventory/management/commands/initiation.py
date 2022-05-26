# Python Import:
import os

# Django Import:
from django.core.management.base import BaseCommand
from django.apps import apps

# Yaml reader import:
from inventory.yaml_reader import yaml_read
from inventory.file_reader import file_read

# Model Import:
from inventory.models.device_type_template_model import DeviceTypeTemplate
from inventory.models.device_type_model import DeviceType
from inventory.models.device_model import Device

# Constant Import:
from inventory.constants import INITIATION_DATA_PATH


# Command class:
class Command(BaseCommand):

    help = 'Xxx.'
    # update_data = None

    def handle(self, *args, **options):
        # Create device type objects:
        created_device_type_objects = {}
        device_type_files = yaml_read(f'{INITIATION_DATA_PATH}/device_type.yml')['output']
        for device_type in device_type_files:
            device_type_name = device_type['name']
            try:
                new_device_type = DeviceType.objects.create(**device_type)
            except:
                print(f'Object {device_type_name} already exist.')
            else:
                created_device_type_objects[new_device_type.pk] = new_device_type
                print(f'Object {device_type_name} was created.')
        
        # Create device type template objects:
        device_type_template_files = yaml_read(f'{INITIATION_DATA_PATH}/device_type_template.yml')['output']
        for device_type_template in device_type_template_files:
            device_type_template_name = device_type_template['name']
            # Collect device type template relations with device type:
            device_type_template_relations = device_type_template['device_type']
            # Delete device type template relations with device type:
            device_type_template.pop('device_type')
            # Replace sfm_expression file path by file.
            sfm_expression_path = device_type_template['sfm_expression']
            device_type_template['sfm_expression'] = file_read(f'{INITIATION_DATA_PATH}/{sfm_expression_path}')['output']
            # Create device type template:
            try:
                new_device_type = DeviceTypeTemplate.objects.create(**device_type_template)
            except:
                print(f'Object {device_type_template_name} already exist.')
            else:
                for device_type_id in device_type_template_relations:
                    created_device_type_objects[device_type_id].device_type_templates.add(new_device_type)
                print(f'Object {device_type_template_name} was created.')

    # def handle(self, *args, **options):

    #     # Collect data from files:
    #     self._collect_data()
    #     # Declare updated models list:
    #     updated_models = []

    #     for class_data_name in self.update_data:
    #         # Collect basic data:
    #         class_data = self.update_data[class_data_name]
    #         dependencies = class_data.get('collected_dependencies_class_name', False)
    #         # Check if current class posses dependencies:
    #         if dependencies:
    #             # Check type of dependencies:
    #             if isinstance(dependencies, list):
    #                 for dependence_class_name in dependencies:
    #                     # Create dependence model first:
    #                     class_dependence_data = self.update_data.get(dependence_class_name, False)
    #                     if class_dependence_data:
    #                         if not class_data_name in updated_models:
    #                             self._create_object(class_dependence_data)
    #                             updated_models.append(dependence_class_name)
    #         # If do not contains dependencies or dependencies was satisfied:
    #         if not class_data_name in updated_models:
    #             self._create_object(class_data)
    #             updated_models.append(class_data_name)

    # def _create_object(self, class_data):
    #     self._collect_object_parameter_path(class_data)
    #     # Collect data:
    #     objects = class_data['collected_objects']
    #     collected_class = class_data['collected_class']
    #     for one_object in objects:
    #         # Check if object contains many to many relation:
    #         many_to_many_list = one_object.get('many_to_many', False)
    #         if many_to_many_list:
    #             one_object.pop('many_to_many')
    #         # Create object:
    #         try:
    #             new_object = collected_class.objects.create(**one_object)
    #         except:
    #             pass
    #         # Create many to mary relation:
    #         if many_to_many_list:
    #             for many_to_many in many_to_many_list:
    #                 # Collect parent class data:
    #                 parent_class_name = many_to_many.get('class_name', False)
    #                 if parent_class_name:
    #                     parent_class = apps.get_model('inventory', parent_class_name)
    #                 parent_object_id = many_to_many.get('pk', False)
    #                 parameter_name = many_to_many.get('parameter_name', False)
    #                 # Check if collected data are valid:
    #                 if parent_class and parent_object_id and parameter_name:
    #                     # Collect parent object:
    #                     parent_object = parent_class.objects.get(pk=parent_object_id)
    #                     parent_object.
    #                     new_object.add(parent_object)

    # def _collect_object_parameter_path(self, class_data):
    #     # Collect data:
    #     object_parameter_path = class_data['object_parameter_path']
    #     objects = class_data['collected_objects']
    #     for one_object in objects:
    #         # Check type of object parameter path:
    #         if isinstance(object_parameter_path, list):
    #             for parameter in object_parameter_path:
    #                 # Collect basic data:
    #                 path = one_object[parameter]
    #                 # Collect data from path:
    #                 collected_data = file_read(f'{INITIATION_DATA_PATH}/{path}')['output']
    #                 # Save data to dictionary:
    #                 one_object[parameter] = collected_data
    #     class_data['collected_objects'] = objects
    #     return class_data
    
    # def _collect_data(self) -> dict:

    #     # Main data dictionary:
    #     update_data = {}

    #     # Collect all initial files:
    #     files = os.listdir(INITIATION_DATA_PATH)
    #     # Iterate thru files:
    #     for file in files:
    #         # Collect file output:
    #         file_output = yaml_read(f'{INITIATION_DATA_PATH}/{file}')['output']
    #         # Check if ile output is valid:
    #         if file_output:
    #             # Collect model class:
    #             collected_class_name = file_output.get('class_name', False)
    #             if collected_class_name:
    #                 collected_class = apps.get_model('inventory', collected_class_name)
    #             # Collect objects:
    #             collected_objects = file_output.get('objects', False)
    #             # Collect rest data if mandatory collected:
    #             if collected_objects and collected_class_name:
    #                 # Collect dependencies:
    #                 collected_dependencies_class_name = file_output.get('dependencies', False)
    #                 # Collect object parameter path:
    #                 object_parameter_path = file_output.get('object_parameter_path', False)
    #                 # Save data to dictionary:
    #                 update_data[collected_class_name] = {
    #                     'collected_class_name': collected_class_name,
    #                     'collected_class': collected_class,
    #                     'collected_dependencies_class_name': collected_dependencies_class_name,
    #                     'collected_objects': collected_objects,
    #                     'object_parameter_path': object_parameter_path
    #                 }
    #     # Return collected data:
    #     self.update_data = update_data
