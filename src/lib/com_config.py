"""
com_config.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 09/01/2018
"""

import configparser
import os.path

config_file = "config/config.ini"


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
    
    def setconfig(self):
        # Version
        self.config['APPLICATION'] = {}
        self.config['APPLICATION']['name'] = 'GoogleHome Server'
        self.config['APPLICATION']['version'] = '1.0.0'
        self.config['APPLICATION']['author'] = '(C) - Bruno DELATTRE'

        # LOGGER
        self.config['LOGGER'] = {}
        self.config['LOGGER']['levelconsole'] = '10'  # DEBUG=10 INFO=20 WARNING=30 ERROR=40 #CRITICAL=50
        self.config['LOGGER']['levelfile'] = '20'  # DEBUG=10 INFO=20 WARNING=30 ERROR=40 #CRITICAL=50
        self.config['LOGGER']['logfile'] = 'log.txt'
        self.config['LOGGER']['logfilesize'] = '1000000'

        # server
        self.config['server'] = {}
        self.config['server']['port'] = '1880'

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, config_file)
        with open(db_path, 'w') as configfile:
            self.config.write(configfile)
    
    def getconfig(self):
        self.config = configparser.RawConfigParser()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, config_file)
        self.config.read(db_path)
        return self.config
