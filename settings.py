import os

from read_env import read_env
read_env()  # read .env into os.environ

CHROMECAST_NAME = os.environ['CHROMECAST_NAME']
DASH_HMAC = os.environ['DASH_HMAC']
BRIDGE_IP = os.environ['BRIDGE_IP']
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
