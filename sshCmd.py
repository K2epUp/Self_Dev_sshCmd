#!/usr/bin/python

import paramiko
import threading

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout = 3)
        for m in cmd:
            stdin,stdout,stderr = ssh.exec_command(m)
            stdin.write("Y")
            out = stdout.readlines()
            for o in out:
                print o,
        #print '%s\tok\n'%(ip)
        ssh.close()
    except:
        print '%s\tError'%(ip)


if __name__ == '__main__':
    hosts = {}
    hosts = {
                'IP0':"192.168.180.128",
                'IP1':"192.168.181.128",
                'IP2':"192.168.182.128",
                'IP3':"192.168.183.128",
            }
    cmd = ['cal','uname -a']
    username = "root"
    passwd = "12345678"
    threads = []
    for ip in hosts.values():
        a = threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
        #ssh2(ip,username,passwd,cmd)
        a.start()
