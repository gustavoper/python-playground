import json

class Config:
    def __init__(self,filePath):
        self.configInfo = []
        self.filePath = filePath
        self.readFile()



    def readFile(self):
        self.configInfo = json.load(open(self.filePath))


    def getConfig(self,key):
        return self.configInfo[key]    