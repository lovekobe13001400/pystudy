import configparser
import os
import sys
cf = configparser.ConfigParser()
test = cf.read(sys.path[0]+'/inv')

def getConfig():
    conf = {}
    conf['local_ip'] = cf.get('env','local_ip')
    conf['proxy_ip'] = cf.get('env','proxy_ip')
    return conf
