# Start PVE cluster from power off
# Ensure certain VMs are powered on and running

from drewsTools.l0 import proxmox
from drewsTools.l0 import functions

# Get desired stat conf
conf=functions.readFile( filetype="yaml", filename="config/pveFullState.yml")

# Make sure cluster is online
Proxmox=proxmox.Proxmox()
for node in Proxmox.getNodes():
    if (node['status'] != "online") and (node['node'] in conf['nodes']):
        print("node %s is not online" % node['node'])
        exit(1)

#power up VMs
for vm in Proxmox.getVms():
    if vm['template'] != 1 and vm['status'] == 'stopped':
        print("powering on %s" % vm['vmid'])
        status=Proxmox.setVmPowerStatus(vm['node'], vm['vmid'], 'start')

