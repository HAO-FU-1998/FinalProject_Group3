# Hao Fu
# Vanderbilt University
# Fall 2022
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import httplib2
import time

class OdlUtil:
    http = httplib2.Http()
    url = ''
    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + port
    def install_flow(self, container_name='default',username="admin", password="admin"):
        self.http.add_credentials(username, password)
        flow_name = 'flow_' + str(int(time.time()*1000))
        h4_s3_s1_s2_1 = '''
            {"flow-node-inventory:flow": [
            {"id": "0","flow-name": "h4_s3_s1_s2_1","cookie": 256,
            "hard-timeout":4,"instructions": {
            "instruction": [{"order": 0,"apply-actions": {
            "action": [{"order": 0,"output-action": {
            "output-node-connector": "2"}}]}}]},
            "priority": 1000,"table_id": 0,"match": {
            "ipv4-destination": "10.0.0.1/32","in-port": "2",
            "ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
         '''

        h3_s3_s1_s2_1 = '''
           {"flow-node-inventory:flow": [
           {"id": "1","flow-name": "h3_s3_s1_s2_1","cookie": 256,
           "hard-timeout":3,"instructions": {
           "instruction": [{"order": 0,"apply-actions": {
           "action": [{"order": 0,"output-action": {
           "output-node-connector": "2"}}]}}]},
           "priority": 1000,"table_id": 0,"match": {
           "ipv4-destination": "10.0.0.1/32","in-port": "1",
            ethernet-match": {"ethernet-type": {"type": 2048}}}}]}
        '''

        headers = {'Content-type': 'application/json'}
        num = 0
        while num < 4:
            response, content = self.http.request(uri='http://10.0.2.15:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:3/flow-node-inventory:table/0/flow/0', body=h4_s3_s1_s2_1, method='PUT',headers=headers)
            print("Success 1")
            time.sleep(4)
            #print(content.decode())

            response, content = self.http.request(uri='http://10.0.2.15:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:3/flow-node-inventory:table/0/flow/1', body=h3_s3_s1_s2_1, method='PUT',headers=headers)
            print("Success 4")
            time.sleep(4)
            #print(content.decode())


if __name__=='__main__':
	
	odl = OdlUtil('10.0.2.15', '8181')
	odl.install_flow()
