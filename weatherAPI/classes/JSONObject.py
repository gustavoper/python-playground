import json

class JSONObject:
    def __init__(self,d):
        self.__dict__ = d

    def loadJson(requestResponse):
        response = json.loads(requestResponse,object_hook=JSONObject)
        return response

        