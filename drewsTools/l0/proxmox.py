from proxmoxer import ProxmoxAPI
from drewsTools.l0 import functions
import json

proxmoxApiCreds = "secrets/proxmoxApi.json"

# Proxmox API https://pve.proxmox.com/pve-docs/api-viewer/index.html
class ProxmoxApi():
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
        else:
            raise Exception("failed to get proxmox creds")

        self.connection = ProxmoxAPI(proxmoxHost, user=user,
                            password=secret, verify_ssl=False)
    
    def getNodes(self):
        return self.connection.nodes.get()

    # power up VM

    # power down VM

        
