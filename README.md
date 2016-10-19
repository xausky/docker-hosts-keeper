# docker-hosts-keeper
The docker image keep upgrade docker container IP to your hosts file.

# QuickStart

```
docker run --name hosts-keeper -v /etc/hosts:/etc/hosts -v /var/run/docker.sock:/var/run/docker.sock xausky/hosts-keeper
```
