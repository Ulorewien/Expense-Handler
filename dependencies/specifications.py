from configparser import ConfigParser

def getSpecifications():
    file = "dependencies/specifications.ini"
    specs = ConfigParser()
    specs.read(file)
    return specs