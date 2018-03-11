import requests

class RequestObject: 
    def __init__(self):
        self.url = ""
        self.args = []

    def setMainUrl(self,url):
        self.url = url

    def setArgs(self,argKey,argValue):
        self.args.append([argKey,argValue])

    def doRequest(self):
        request = requests.get(self.url,self.args)
        return self.responseAsText(request)
    
    def responseAsText(self,requests):
        return requests.text