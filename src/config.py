'''from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='cmdArgs')
parser.add_argument('--output', type=str, default='slack_data.csv',
                help='filename to write analysis output in CSV format')
parser.add_argument('--path', required=True, type=str, help='directory where slack data reside')
parser.add_argument('--channel', type=str, default='', help='which channel we parsing')
parser.add_argument('--userfile', type=str, default='users.json', help='users profile information')

cfg = parser.parse_args()'''
# config.py

class Config:
    OUTPUT_FILE = 'slack_data.csv'
    DATA_PATH = ''
    CHANNEL = ''
    USER_FILE = 'users.json'
  
# script.py

from __future__ import print_function
import argparse
from config import Config  # Import the Config class from the config.py file

parser = argparse.ArgumentParser(description='cmdArgs')
parser.add_argument('--output', type=str, default=Config.OUTPUT_FILE,
                    help='filename to write analysis output in CSV format')
parser.add_argument('--path', required=True, type=str, help='directory where slack data reside')
parser.add_argument('--channel', type=str, default=Config.CHANNEL, help='which channel we parsing')
parser.add_argument('--userfile', type=str, default=Config.USER_FILE, help='users profile information')

cfg = parser.parse_args()

# print(cfg)
