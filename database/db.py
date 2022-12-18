import configparser
import pathlib


file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB-DEV', 'user')
password = config.get('DB-DEV', 'password')
db_name = config.get('DB-DEV', 'db_name')

URL = f'mongodb://localhost:27017/HW'
