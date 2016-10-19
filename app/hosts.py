import docker
import config

class Hosts:
    def __init__(self):
        self.oldHost = []
    def upgrade(self,client):
        newLines = []
        #loop through runing container
        rewrite = False
        newHost = []
        for container in client.containers():
            inspect = client.inspect_container(container['Id'])
            IP = inspect['NetworkSettings']['Networks'].items()[0][1]['IPAddress']
            name = inspect['Name'][1:]
            hostname = inspect['Config']['Hostname']
            newLines.append('%s    %s %s\n'%(IP,hostname,name))
            newHost.append(hostname)
        if cmp(self.oldHost,newHost) != 0:
            print ''.join(newLines)
            newLines.insert(0,config.DOCKER_HOSTS_START)
            newLines.append(config.DOCKER_HOSTS_END)
            hostsFile = open(config.HOSTS_FILE_PATH,'r')
            oldLines = hostsFile.readlines()
            hostsFile.close()
            #delete docker-hosts session
            copyable = True
            for line in oldLines:
                if line == config.DOCKER_HOSTS_START:
                    copyable = False
                if copyable:
                    newLines.append(line)
                if line == config.DOCKER_HOSTS_END:
                    copyable = True
            #upgrade hosts file
            hostsFile = open(config.HOSTS_FILE_PATH,'w')
            hostsFile.writelines(newLines)
            hostsFile.close()
            self.oldHost = newHost
