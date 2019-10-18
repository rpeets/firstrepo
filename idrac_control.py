#
#
#
import requests, json, sys, re, time, warnings

warnings.filterwarnings("ignore")

try:
    idrac_ip = 'buttress-c'         #  login: root    (7ScA%[Bx.k2duf
    idrac_username = 'root'
    idrac_password = '(7ScA%[Bx.k2duf'

except:
    print("- FAIL: You must pass in script name along with iDRAC IP / iDRAC username / iDRAC password. Example: \"script_name.py 192.168.0.120 root calvin\"")
    sys.exit()



response = requests.get('https://%s/redfish/v1/Systems/System.Embedded.1/' % idrac_ip,verify=False,auth=(idrac_username, idrac_password))
data = response.json()
print(data)
print("\n- WARNING, Current server power state is: %s\n" % data[u'PowerState'])

print("- Supported values for server power control are:\n")
for i in data[u'Actions'][u'#ComputerSystem.Reset'][u'ResetType@Redfish.AllowableValues']:
    print(i)


# https://github.com/dell/iDRAC-Redfish-Scripting/tree/master/Redfish%20Python
# https://github.com/dell/iDRAC-Redfish-Scripting/blob/master/Redfish%20Python/SetPowerStateREDFISH.py
