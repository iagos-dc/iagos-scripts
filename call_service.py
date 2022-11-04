import json
import requests
import authentication as auth

def getHeader():
    return {'Authorization': 'Bearer ' + auth.getToken()['access_token'], 'Accept': 'application/json'}

def getPublic(url):
    return requests.get(url)
    
def getPrivate(url):
    return requests.get(url, headers=getHeader())
        
if __name__ == '__main__':
    response = getPublic("https://services.iagos-data.fr/prod/v2.0/parameters/public")
    data = json.loads(response.text)
    with open("C:/Users/dboulang/Documents/response.json", "w") as f:
        f.write(json.dumps(data, indent=2))
        
    response = getPrivate("https://services.iagos-data.fr/prod/v2.0/parameters")
    data = json.loads(response.text)
    with open("C:/Users/dboulang/Documents/response2.json", "w") as f:
        f.write(json.dumps(data, indent=2))