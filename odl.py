# Hao Fu
# Vanderbilt University
# Fall 2022
#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
def http_put(url,jstr):
  url= url
  headers = {'Content-Type':'application/json'}
  resp = requests.put(url,jstr,headers=headers,auth=HTTPBasicAuth('admin', 'admin'))
  return resp 
 
if __name__ == "__main__":
  url = 'http://10.0.2.15:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/table/0/flow/25'
  with open('odl.json') as f:
    jstr = f.read()
    resp = http_put(url,jstr)
    print (resp.content)