#
#
#
import requests, json, time, datetime 
from collections import namedtuple

def readData(url):
    #url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
    #url = 'https://tinyurl.com/y34hprk5' 
    try:
        response = json.loads(requests.get(url).text)['features']
    except requests.exceptions.RequestException as e:
        print(e)
        exit(1)
    except json.decoder.JSONDecodeError as je:
        print('Decoding JSON has failed', je)
        exit(1)
    #return response
    data = sorted(response, key=lambda k: k['properties']['time'])
    return data


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def main():
    url = 'https://tinyurl.com/y34hprk5'
    #print(json.dumps(readData(), indent=4))
    newlist = readData(url)
    for i in newlist:
        s = Struct(**i['properties'])
        if s.place.endswith(', CA') and s.type == 'earthquake':
            quaketime = time.strftime('%Y-%m-%dT%H:%M:%S+00:00',\
                time.localtime(float(s.time)/1000))
            print(quaketime,'|',s.place,'| Magnitude:',s.mag)

if __name__ == '__main__':
    main()
