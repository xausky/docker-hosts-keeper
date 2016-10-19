import time
import docker
import threading

import hosts
import config

hosts = hosts.Hosts()
client = docker.Client(base_url=config.DOCKER_UNIX_SOCK)
while True:
    print('Scanning new containers')
    hosts.upgrade(client)
    time.sleep(config.SCAN_INTERVAL)
