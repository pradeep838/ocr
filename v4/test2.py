import psutil
def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        #    pinfo['vms'] = proc.memory_full_info().vms/(1024*1024)
           print(proc.status)
           listOfProcObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['pid'], reverse=True)
    return listOfProcObjects

print(list(filter(lambda item:'com.apple.hiservices' in  item['name'] ,getListOfProcessSortedByMemory())))
# print(getListOfProcessSortedByMemory())
