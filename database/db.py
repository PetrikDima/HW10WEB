import configparser
import pathlib


file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB-DEV', 'user')
password = config.get('DB-DEV', 'password')

URL = f'mongodb+srv://{username}:{password}@web.hn36cfm.mongodb.net/?retryWrites=true&w=majority'

