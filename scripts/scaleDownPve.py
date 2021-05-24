# save dat money
# Scale infra down to bare-bones

from drewsTools.l0 import proxmox
from drewsTools.l0 import functions

# Get desired stat conf
conf=functions.readFile( filetype="yaml", filename="config/pveLowState.yml")

# shutdown everything but core VMs
Proxmox=proxmox.Proxmox()
for vm in Proxmox.getVms():
    if vm['template'] != 1 and vm['status'] == 'running' and vm['name'] not in conf['vms']:
        print("powering down %s" % vm['name'])
        # status=Proxmox.setVmPowerStatus(vm['node'], vm['vmid'], 'shutdown')

# Migrate all Vms to nodes to keep on

# Shutdown nodes