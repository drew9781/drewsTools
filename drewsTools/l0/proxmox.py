from proxmoxer import ProxmoxAPI
from drewsTools.l0 import functions
import json

proxmoxApiCreds = "secrets/proxmoxApi.json"

# Proxmox API https://pve.proxmox.com/pve-docs/api-viewer/index.html
class Proxmox():
    def __init__(self, **kwargs):
        creds = functions.getCreds(filename=proxmoxApiCreds)
        try:
            proxmoxHost = creds['proxmoxHost']
            user        = creds['user']
            secret      = creds['pass']
        except KeyError:
            proxmoxHost = kwargs.get("proxmoxHost", "pve")
            user        = kwargs.get("user", "root@pam")
            secret      = kwargs.get("secret")

        self.connection = ProxmoxAPI(proxmoxHost, user=user,
                            password=secret, verify_ssl=False)
    
    ######################
    # Nodes
    def getNodes(self, node=""):
        return self.connection.nodes.get(node)

    def getNodeStatus(self, nodeName):
        node = self.connection.nodes(nodeName)
        return node.status()
    
    # reboot or shutdown
    def setNodeStatus(self, nodeName, status):
        node = self.connection.nodes(nodeName)
        print("Rebooting pve node %s" % nodeName)
        return node.status.post(command=status)

    #######################
    # VMs

    def getVms(self):
        return self.connnection.cluster.resources.get(type='vm')

    # Status types:
    #   reboot reset resume shudown start stop suspend
    def setVmPowerStatus(self, node, vmId, status):
        return self.connnection.post('nodes/%s/qemu/%s/status/%s' % (node, vmId, status))

    def getVmPowerStatus(self, node, vmId, status):
        return self.connnection.get('nodes/%s/qemu/%s/status/%s' % (node, vmId, status))

        
