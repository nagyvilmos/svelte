import json;
import os;
settings=None
#os.environ.get()
def loadSettings(settingsFile="settings.json"):
    global settings
    f = open(settingsFile)
    settings = json.load(f)
    f.close()

def getSetting(setting, default=None):
    value = settings[setting]
    if value != None:
        return value
    return os.environ.get(setting,default)
