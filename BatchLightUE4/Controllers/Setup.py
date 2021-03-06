import os

from configparser import ConfigParser
from os.path import dirname, join, exists, expanduser

"""This files include the Object to work with the INI files, read, writes 
and more"""
# TODO The User path are good, but not inside the Document Folder


class Setup(object):
    config = ConfigParser()
    config_name = 'settings.ini'
    config_path = join(expanduser('~'), 'BBLUE4', config_name)

    if not exists(dirname(config_path)):
        os.makedirs(dirname(config_path))

    def __init__(self):
        if exists(self.config_path):
            self.read()
        else:
            self.write()

    def write(self):
        self.config.add_section('Project Work')
        self.config.add_section('All Projects')
        self.config.add_section('Default')
        self.config.add_section('Version')

        self.config['Project Work'] = {'Run': '', }
        self.config['Version'] = {'Release': '0.9.0', }
        self.config['Default'] = {
            'Editor': '',
            'Project': '',
            'Sub Folder': '',
            'CSV': False,
        }

        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def read(self):
        data = self.config.read(self.config_path)

        return data

    def base(self, option):
        self.config.read(self.config_path)
        data = self.config.get('Default', option)

        return data

    def last_job_run(self):
        self.config.read(self.config_path)
        data = self.config.get('Project Work', 'run')

        return data

    def last_job_add(self, filename):
        self.config.read(self.config_path)
        self.config.set('Project Work', 'Run', filename)

        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def version(self, update=None):
        self.config.read(self.config_path)
        data = self.config.get('Version', 'release')

        if update is not None:
            print('Update the Version to : ', update)
            self.config.set('Version', 'release', update)

            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)

        return data
