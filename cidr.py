#
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni
from netaddr import IPAddress
print(ni.interfaces())
print(ni.ifaddresses('eth0'))
print(IPAddress('255.255.255.0').netmask_bits())
