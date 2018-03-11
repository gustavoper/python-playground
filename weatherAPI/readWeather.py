
from classes.JSONObject import JSONObject
from classes.RequestObject import RequestObject
from classes.Config import Config

configObj = Config("./config.json")

weatherUrl = configObj.getConfig("weatherUrl") 

requestObj = RequestObject()
requestObj.setMainUrl(weatherUrl)
requestObj.setArgs("id","3465059")
requestObj.setArgs("APPID",configObj.getConfig("APPID"))
response = JSONObject.loadJson(requestObj.doRequest())

#cityname
print(response.name)
#coords
print(response.coord.lon)
print(response.coord.lat)

