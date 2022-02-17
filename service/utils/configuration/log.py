import os
import sys
import logging
from logging.config import fileConfig

cur_dir = os.getcwd()
if 'service' in cur_dir:
    fileConfig(os.getcwd() + '/logging.ini')
else:
    fileConfig(os.getcwd() + '/service/logging.ini')
logger = logging.getLogger('dev')
