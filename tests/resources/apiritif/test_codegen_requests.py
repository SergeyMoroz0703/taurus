
import logging
import random
import string
import sys
import time
 
import apiritif
 
 

class TestAPIRequests:

    def test_requests(self):
        with apiritif.transaction('apiritif'):
            response = apiritif.http.get('http://localhost:8000/')
         
