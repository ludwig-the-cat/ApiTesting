import configparser
from pathlib import Path

cfgfile = 'petqa.ini'
cnffolder = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIGFILE = BASE_DIR.joinpath(cnffolder).joinpath(cfgfile)

config.read(CONFIGFILE)

def getPetAPIURL():
    return config['pet']['url']

def getStoreAPIURL():
    return config['store']['url']

print(getPetAPIURL())
