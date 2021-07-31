# save dat money
# Scale infra down to bare-bones

from drewsTools.l0 import proxmox
from drewsTools.l0 import functions
from drewsTools.l1 import proxmoxFunctions
import time


def readConf():
    return functions.readFile( filetype="yaml", filename="config/pveLowState.yml")

def shutdownNotNeededVms(Proxmox, conf):
    done=False
    iteration=0
    while not done:
        print("Doing iteration %s" % iteration)
        iteration += 1
        running=False
        for vm in Proxmox.getVms():
            if vm['template'] != 1 and vm['status'] == 'running' and vm['name'] not in conf['vms']:
                running=True
                print("powering down %s" % vm['name'])
                status=Proxmox.setVmPowerStatus(vm['node'], vm['vmid'], 'shutdown')
        if not running:
            done=True
        else:
            time.sleep(30)

def migrateVmsToGoodNodes(Proxmox, conf):
    # Migrate all Vms to nodes to keep on
    toMigrateList=[]
    # getVms to migrate
    for vm in Proxmox.getVms():
        if vm['name'] not in conf['vms'] or vm['node']  in conf['nodes']:
            continue
        else:
            toMigrateList.append(vm)

    for vm in toMigrateList:
        proxmoxFunctions.migrateVm(vm, conf['nodes'])
    # migrate VM
        # evaluate node usage
        # pick lower used node by % 
        # if no space evacuate some not-needed VMs



# Shutdown nodes

def main():
    conf=readConf()
    Proxmox=proxmox.Proxmox()

    shutdownNotNeededVms(Proxmox, conf)
    migrateVmsToGoodNodes(Proxmox,conf)

main()