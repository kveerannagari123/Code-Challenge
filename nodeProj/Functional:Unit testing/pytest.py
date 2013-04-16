
import os
import unittest
#import HTMLTestRunner
#import Utility as u
import requests
import json
from requests.auth  import HTTPBasicAuth


class TestServerResponse(unittest.TestCase):
    
    def setUp(self):
        
        print "before test case"
        
    def test_ResponseCode(self):
        
        print("-------------------------------------------------------")
        print("Test Summary:")
        print("\nVerify the status code")
        print("-------------------------------------------------------")

        base_headers={'content-type':'application/json'}

        response =requests.get("http://localhost:8845/",headers=base_headers,verify=False)

        self.failUnlessEqual(response.status_code,200,"Test status code")
        
    def test_ResponceContentType(self):
        
        print("-------------------------------------------------------")
        print("Test Summary:")
        print("\nVerify the JSON transmitted data")
        print("-------------------------------------------------------")

        base_headers={'content-type':'application/json'}

        response =requests.get("http://localhost:8845/",headers=base_headers,verify=False)
        
        print response.headers['content-type']
        
        self.failUnlessEqual(response.headers['content-type'],"application/json","test the PID for static data")
    
    def test_JSONResponce(self):
        
        print("-------------------------------------------------------")
        print("Test Summary:")
        print("\nVerify the JSON transmitted data")
        print("-------------------------------------------------------")

        base_headers={'content-type':'application/json'}

        response =requests.get("http://localhost:8845/",headers=base_headers,verify=False)
        
        print response.headers['content-type']
        
        self.failUnlessEqual(response.headers['content-type'],"application/json","test the PID for static data")
        
        self.failUnlessEqual(json.loads(response.content)[1]["PID"],171,"test the PID for static data")
        
        self.failUnlessEqual(json.loads(response.content)[1]["CPU"],3.4,"test the CPU for static data")
        
        
    