from drewsTools.l0 import proxmox
from drewsTools.l0 import functions

Proxmox = proxmox.Proxmox()

for vm in Proxmox.connection.cluster.resources.get(type='vm'):
    print(vm)
