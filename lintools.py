#! /usr/bin/python3
import subprocess
def user():
    p = subprocess.Popen(['w'], stdout=subprocess.PIPE)
    result = p.communicate()
    return result
#    for data in result:
#        print(data)

def vmstat():
    p = subprocess.Popen(['vmstat'], stdout=subprocess.PIPE)
    result = p.communicate()
    return result

def reb():
    p = subprocess.Popen(['reboot'], stdout=subprocess.PIPE)
    result = p.communicate()
    return result
#    for data in result:
#
def ifconfig():
    p = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE)
    result = p.communicate()
    return result
#    for data in result:

def disk():
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    result = p.communicate()
    return result
#    for data in result:
def service(comm, name):
    p = subprocess.run(['systemctl', comm, name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.stdout
    return result



