import requests
import urllib3
from collections import OrderedDict
urllib3.disable_warnings()

class sonicapi:
    def __init__(self, hostname, port, username, password) -> None:
        self.baseurl = f"https://{hostname}:{port}/api/sonicos"
        self.authinfo = (username, password)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Encoding": "application/json",
            "Charset": "UTF-8", 
        }
        
    def auth(self) -> None:
        route = "/auth"
        url = self.baseurl + route
        r = requests.post(url, auth = self.authinfo, headers=self.headers)
        
        if r.status_code != 200:
            print("FAILED")
            return f"{r.status_code}\n{r.json}"
        else:
            print("SUCCESSFUL")
            response = r.json()
            return response
    
    def tenant_count(self):
        route = "/tenants/count"
        url = self.baseurl + route
        r = requests.get(url, auth = self.authinfo, headers=self.headers)

        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response
    """     
    def new_tenant(self, payload):
        route = "/tenants"
        url = self.baseurl + route
        r = requests.post(url, payload, self.headers)

        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response  """
import requests
import urllib3
from collections import OrderedDict
urllib3.disable_warnings()

class sonicapi:
    def __init__(self, hostname, username, password) -> None:
        self.baseurl = f"https://{hostname}:444/api/sonicos"
        self.authinfo = (username, password)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Encoding": "application/json",
            "Charset": "UTF-8", 
        }
        
    def auth(self) -> None:
        route = "/auth"
        url = self.baseurl + route
        r = requests.post(url, auth = self.authinfo, headers=self.headers, verify=False)
        
        if r.status_code != 200:
            print("FAILED")
            return f"{r.status_code}\n{r.json}"
        else:
            print("SUCCESSFUL")
            response = r.json()
            return response
    
    def tenant_count(self):
        route = "/tenants/count"
        url = self.baseurl + route
        r = requests.get(url, auth = self.authinfo, headers=self.headers)

        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response
    """     
    def new_tenant(self, payload):
        route = "/tenants"
        url = self.baseurl + route
        r = requests.post(url, payload, self.headers)

        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response  """