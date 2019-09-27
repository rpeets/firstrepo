#
#
#
import requests, json, time, datetime 
from collections import namedtuple

def readData(url):
    try:
        response = json.loads(requests.get(url).text)['features']
        #response = json.loads(requests.get(url).text)
        #print(json.dumps(response, indent=4))
        #exit(0)
        #response = json.loads(jsondata)['features']
    except requests.exceptions.RequestException as reqerr:
        print(reqerr)
        exit(1)
    except json.decoder.JSONDecodeError as jsonerr:
        print('Decoding JSON has failed', jsonerr)
        exit(1)
    data = sorted(response, key=lambda k: k['properties']['time'])
    return data


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def utcTime(epochTime):
    utc = time.strftime('%Y-%m-%dT%H:%M:%S+00:00',\
                time.localtime(float(epochTime)/1000))
    return utc


def stateName(place):
    return place.replace(', CA', ', California')


def main():
    #url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
    url = 'https://tinyurl.com/y34hprk5'
    
    #print(json.dumps(readData(url), indent=4))
    
    newlist = readData(url)
    for i in newlist:
        s = Struct(**i['properties'])
        if s.place.endswith(', CA') and s.type == 'earthquake':
            #utctime = utcTime(s.time)
            print(utcTime(s.time),'|',stateName(s.place),'| Magnitude:',s.mag)


if __name__ == '__main__':
    main()
