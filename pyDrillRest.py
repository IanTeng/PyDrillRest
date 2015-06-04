# -*- coding: utf-8 -*- 
#Copyright (c) 2015 - Ian <dengxw@eship.com.cn> 

import requests
import logging

class DrillClient:
    def __init__(self,server):
        self.url='http://'+server+'/query.json'
        self.headers={'Content-type': 'application/json'}
        
    def sqlQuery(self,sql):
        payload={"queryType":"SQL","query":sql}
        r=requests.post(self.url,headers=self.headers,json=payload)
        if r.status_code!=200:
            print('Query Failed:'+str(r.status_code)+str(r.content))
        return r.content if r.status_code==200 else None
        
