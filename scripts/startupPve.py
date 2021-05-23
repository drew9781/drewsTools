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

# Get list of VMs to ensure 


# power up VMs