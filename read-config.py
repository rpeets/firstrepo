#!/usr/bin/env python3
#
# https://github.com/psf/requests
# requests 2.22.0 (2019-05-15) 
# https://requests.kennethreitz.org/en/master/
# https://pypi.org/project/requests/
# 
import yaml, requests

# def readconfig(filename):
#     with open(filename) as yamlfile:
#         try:
#             config = (yaml.safe_load(yamlfile))
#         except yaml.YAMLError as exc:
#             print(exc)
#     return config

def readconfig(url):
    try:
        response = requests.get(url)
        config = yaml.safe_load(response.text)
    except requests.exceptions.RequestException as e:
        print(e)
        exit(1)
    # print(dir(response))
    print(yaml.dump(config, default_flow_style=False))
    exit(0)
    return config

def main():
    #config = readconfig('/Users/rpeter/repo/python-yaml/lif-config.yaml')
    url = 'https://raw.githubusercontent.com/rpeets/firstrepo/master/testfile.yaml'
    config = readconfig(url)
    #print(yaml.dump(config['cluster'], default_flow_style=False))
    #print(config)
    for cluster in config['cluster']:
        #print(cluster)
        #print(cluster['clusterName'])
        for vserver in cluster['vserver']:
            print(vserver['vserverName'])
            for lif in vserver['networkInterface']:
                print(lif['interfaceName'])
                print(lif['ipAddress'])
                print(lif['netmask'])
                print(lif['gateway'])
                print(lif['home-node'])
                print("")


if __name__ == "__main__":
    main()
