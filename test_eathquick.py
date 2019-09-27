##!/usr/bin/env python -W ignore::DeprecationWarning
#import warnings
import requests
#with warnings.catch_warnings():
#    warnings.simplefilter("ignore")
import httpretty
import earthquick
    

#@httpretty.activate
# def test_one():
#     # define your patch:
#     httpretty.register_uri(httpretty.GET, "http://yipit.com/",
#                         body="Find the best daily deals")
#     # use!
#     response = requests.get('http://yipit.com')
#     assert response.text == "Find the best daily deals"

@httpretty.activate
def test_readData():
    httpretty.register_uri(httpretty.GET, "http://foo.com/y34hprk5",
                        #body='{"origin": "127.0.0.1", "features": "test"}')
                        body='{"origin": "127.0.0.1", "features": [{"properties": {"time": 1569555787345}}]}')
    data = earthquick.readData('http://foo.com/y34hprk5')
    assert data == [{"properties": {"time": 1569555787345}}]
    httpretty.disable() 
    httpretty.reset() 
