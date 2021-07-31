from drewsTools.l0 import proxmox

def migrateVm(vm, allowedNodes=[]):
    candidateList = getNodeCandidateList(allowedNodes)
    
    for nodeName in candidateList['candidateList']:
        print('filler')
        #validate candidate

    # if no space evacuate some not-needed VMs




# returns node stats and candidate list
# {
#     'nodeName' :{
#         'availablecpu': 7.997061127069271, 
#         'maxcpu': 8, 
#         'percentFreecpu': 0.9996326408836589, 
#         'availablemem': 15209676800, 
#         'maxmem': 16649740288,
#         'percentFreemem': 0.913508351296152, 
#         'availabledisk': 25744662528, 
#         'maxdisk': 29194506240, 
#         'percentFreedisk': 0.8818324350602205, 
#         'averageFreePercent': 0.9316578090800105
#     },
#     'candidateList' : ['mostFreeNode', 'notAsFreeNode']
# }
def getNodeCandidateList(allowedNodes=[]):
    Proxmox=proxmox.Proxmox()

    nodeStats={}
    for node in Proxmox.getNodes():
        if node['node'] not in allowedNodes:
            continue
            
        sysType=['cpu','mem','disk']
        percentFreeList=[]
        nodeStats[node['node']] = {}
        for type in sysType:
            nodeStats[node['node']]['available'+type]  = node['max'+type]  - node[type]
            nodeStats[node['node']]['max'+type]  = node['max'+type]
            nodeStats[node['node']]['percentFree'+type]  = (node['max'+type] - node[type]) / node['max'+type]
            percentFreeList.append( nodeStats[node['node']]['percentFree'+type] )
        
        nodeStats[node['node']]['averageFreePercent'] = sum(percentFreeList) / len(percentFreeList)
    
    # Sort candidate list with most Free resources first
    candidateList= list(nodeStats.keys())
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(candidateList) - 1):
            if nodeStats[ candidateList[i] ]['averageFreePercent'] < nodeStats[ candidateList[i + 1] ]['averageFreePercent']:
                candidateList[i], candidateList[i+1] = candidateList[i+1], candidateList[i]
                swapped=True

    nodeStats['candidateList'] = candidateList
    return nodeStats 

def validateVmToCandidate():
    Proxmox=proxmox.Proxmox()
