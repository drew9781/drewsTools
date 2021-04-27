from drewsTools.l0 import functions

proxmoxApiCreds = "secrets/proxmoxApi.json"

creds = functions.getCreds(filename=proxmoxApiCreds)
try:
    proxmoxHost = creds['proxmoxHost']
    user        = creds['user']
    secret      = creds['pass']

except:
    #didnt find file
    raise Exception("failed to read file "+filename)

