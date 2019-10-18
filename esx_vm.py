#
#
#
import time
import atexit
from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim

class Arguments():
    def __init__(self):
        self.host = "10.18.17.113"
        self.user = "root"
        self.password = "NetApp123!"
        self.port = 443
        self.ssl_verification = False

def esxconnect():
    args = Arguments()
    try:
        if args.ssl_verification == False:
            si = connect.SmartConnectNoSSL(host=args.host,
                user=args.user,pwd=args.password,port=int(args.port))
        else:
            si = connect.SmartConnect(host=args.host,
                user=args.user,pwd=args.password,port=int(args.port))

    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return -1
    atexit.register(connect.Disconnect, si)
    return si

def vm_status(vm):
    print(vm.runtime.powerState)
    #print(vm.)
    print()

def vm_poweroff(vm):
    vm.PowerOff()
    time.sleep(2)
    print(vm.runtime.powerState)


def vm_poweron(vm):
    vm.PowerOn()
    time.sleep(2)
    print(vm.runtime.powerState)


def main():
    #state = input('Enter system state [On/Off]: ').lower()
    #print(state)
    si = esxconnect()
    content = si.RetrieveContent()
    vms = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.VirtualMachine], True).view
    #print(containers)
    for vm in vms:
        #vm_status(vm)
        print(vm.layout)
        #print(dir(vm))
        #print(vm.__dir__())
        #print(vm.__dict__)
        if vm.config.name == 'str104' and vm.runtime.powerState == 'boo':
            #print(vm.runtime)
            #print(vm.config)
            print(vm.summary)
            print(vm.runtime.powerState)
            print(vm.config.uuid)
            print(vm.config.name)
            #vm_poweroff(vm)
        elif vm.config.name == 'str104' and vm.runtime.powerState == 'boo':
            print(vm.runtime.powerState)
            print(vm.config.uuid)
            print(vm.config.name)
            #vm_poweron(vm)


if __name__ == "__main__":
    main()
